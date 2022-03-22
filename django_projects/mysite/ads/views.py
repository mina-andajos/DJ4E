from ads.models import Ad, Comment
from ads.owner import (
    OwnerListView,
    OwnerDetailView,
    OwnerDeleteView,
)
from ads.forms import CommentForm, CreateForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "myarts/Ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "ads/ad_detail.html"

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        ad = get_object_or_404(klass=self.model, id=pk)
        comments = Comment.objects.filter(ad=ad).order_by("-updated_at")

        comment_form = CommentForm()
        context = {
            "ad": ad,
            "comments": comments,
            "comment_form": comment_form,
        }

        return render(
            request=request,
            template_name=self.template_name,
            context=context,
        )


class AdCreateView(LoginRequiredMixin, View):
    template_name = "ads/ad_form.html"
    success_url = reverse_lazy("ads:all")

    def get(self, request: HttpRequest, pk=None) -> HttpResponse:
        form = CreateForm()
        context = {"form": form}

        return render(
            request=request,
            template_name=self.template_name,
            context=context,
        )

    def post(self, request: HttpRequest, pk=None) -> HttpResponse:
        form = CreateForm(
            data=request.POST,
            files=request.FILES or None,
        )

        if not form.is_valid():
            context = {"form": form}
            return render(
                request=request,
                template_name=self.template_name,
                context=context,
            )

        else:
            ad = form.save(commit=False)
            ad.owner = self.request.user
            ad.save()

            return redirect(to=self.success_url)


class AdUpdateView(LoginRequiredMixin, View):
    template_name = "ads/ad_form.html"
    success_url = reverse_lazy("ads:all")

    def get(self, request: HttpRequest, pk) -> HttpResponse:
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        context = {"form": form}

        return render(
            request=request,
            template_name=self.template_name,
            context=context,
        )

    def post(self, request: HttpRequest, pk) -> HttpResponse:
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(data=request.POST, files=request.FILES, instance=ad)

        if not form.is_valid():
            context = {"form": form}
            return render(
                request=request,
                template_name=self.template_name,
                context=context,
            )

        ad = form.save()

        return redirect(to=self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad


def stream_file(request: HttpRequest, pk: int) -> HttpResponse:
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response["Content-Type"] = ad.content_type
    response["Content-Length"] = len(ad.picture)
    response.write(ad.picture)
    return response


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest, pk: int):
        ad = get_object_or_404(klass=Ad, id=pk)

        comment = Comment(text=request.POST["comment"], owner=request.user, ad=ad)
        comment.save()

        return redirect(to=reverse_lazy("ads:ad_detail", args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    def get_success_url(self) -> str:
        ad = self.object.ad
        return reverse_lazy("ads:ad_detail", args=[ad.id])
