from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse

"""
Why We Use reverse_lazy:
Well, first of all, the URL resolver itself is lazy, so loading happens when the first call to resolve() or reverse() is made (usually on the first request). But that doesn't matter much in this case.

When the URL resolver is being initialized, it imports your URL configuration, which in turn imports your views. So at the time your view is imported and success_url is set, the resolver is only halfway through its initialization. Calling reverse() at this point would not work since the resolver doesn't have all the information yet to reverse the view name.
"""

from autos.models import Auto, Make
from autos.forms import MakeForm

# Create your views here.

"""
We want views for:
    - Showing a list of all autos. (we will put this on index)

    - Showing a list of all makes.
    - Creating a make.
    - Deleting a make.
    - Updating a make.

    - Creating an auto.
    - Deleting an auto.
    - Updating an auto.
"""


class MainView(LoginRequiredMixin, View):
    """view that's shown on the autos index, lists all autos."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """what's shown once we make a get request"""

        # ? shows number of all objects for the make model
        make_count = Make.objects.all().count()
        auto_list = Auto.objects.all()  # ? Iterable of all autos

        context = {"make_count": make_count, "auto_list": auto_list}

        return render(
            request=request, template_name="autos/auto_list.html", context=context
        )


class MakeView(LoginRequiredMixin, View):
    """view that's displayed to list makes"""

    def get(self, request: HttpRequest) -> HttpResponse:
        make_list = Make.objects.all()
        context = {"make_list": make_list}

        return render(
            request=request, template_name="autos/make_list.html", context=context
        )


class MakeCreate(LoginRequiredMixin, CreateView):
    """View that's shown when we create a make"""

    model = Make
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


"""
- Take the easy way out on the main table.
- These views do not need a form because CreateView, etc..
- Build a form object dynamically based on the fields value in the constructor attributes.
"""


class AutoCreate(LoginRequiredMixin, CreateView):
    """inheriting a built-in CreateView to auto generate the form"""

    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class AutoUpdate(LoginRequiredMixin, UpdateView):
    """inheriting a built-in UpdateView to auto generate the form"""

    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class AutoDelete(LoginRequiredMixin, DeleteView):
    """inheriting a built-in DeleteView to auto generate the form"""

    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


"""
We use reverse_lazy rather than reverse in the class attributes
because views.py is loaded by urls.py and in urls.py as_view() causes
the constructor for the view class to run before urls.py has been
completely loaded and urlpatterns has been processed.
"""
