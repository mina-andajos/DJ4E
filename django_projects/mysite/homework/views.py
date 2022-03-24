from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import MainForm
from .utils import combine_fields


# Create your views here.
class MainView(LoginRequiredMixin,View):
    template_name = "homework/main.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        form = MainForm()
        context = {"form": form}

        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = MainForm(request.POST)

        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template_name, context)

        fields = (form.cleaned_data["field1"], form.cleaned_data["field2"])
        result = combine_fields(*fields)

        context = {
            "form": form,
            "result": result,
        }

        return render(request, self.template_name, context)
