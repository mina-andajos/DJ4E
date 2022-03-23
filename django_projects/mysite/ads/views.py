from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from ads.models import Ad, Comment, Favorite
from ads.owner import (
    OwnerListView,
    OwnerDetailView,
    OwnerDeleteView,
)
from ads.forms import CommentForm, CreateForm
from ads.utils import generate_search_query

# Create your views here.
class AdListView(OwnerListView):
    model = Ad
    template_name = "ads/ad_list.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        search_value = request.GET.get("search", False)

        if not search_value:
            ads = Ad.objects.all().order_by("-updated_at")[:10]
        else:
            query = generate_search_query(search_value=search_value)
            ads = Ad.objects.filter(query).select_related().order_by("-updated_at")[:10]

        for ad in ads:
            ad.natural_updated = naturaltime(value=ad.updated_at)

        favorites = []
        if request.user.is_authenticated:
            # ? rows=[{"id":2},...]
            rows = request.user.favorite_ads.values("id")
            # ?favorites=[2,...]
            favorites = [row["id"] for row in rows]

        context = {"ads": ads, "favorites": favorites}

        return render(
            request=request,
            template_name=self.template_name,
            context=context,
        )


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


@method_decorator(csrf_exempt, name="dispatch")
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        print(f"Add PK {pk}")

        ad = get_object_or_404(klass=Ad, id=pk)
        favorite = Favorite(user=request.user, ad=ad)

        try:
            favorite.save()
        except IntegrityError as e:
            pass

        return HttpResponse()


@method_decorator(csrf_exempt, name="dispatch")
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        print(f"Delete PK {pk}")

        ad = get_object_or_404(klass=Ad, id=pk)

        try:
            favorite = Favorite.objects.get(user=request.user, ad=ad).delete()
        except Favorite.DoesNotExist as e:
            pass

        return HttpResponse()
