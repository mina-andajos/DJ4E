from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from .models import Breed, Cat

# Create your views here.
class CatView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        breed_count = Breed.objects.all().count()
        cat_list = Cat.objects.all()

        context = {
            "breed_count": breed_count,
            "cat_list": cat_list,
        }

        return render(
            request=request, template_name="cats/cat_list.html", context=context
        )


class BreedView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        breed_list = Breed.objects.all()
        context = {"breed_list": breed_list}

        return render(
            request=request, template_name="cats/breed_list.html", context=context
        )


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:all")
