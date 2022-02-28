from html import escape
from urllib import request

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render  # ? function that renders http given to it
from django.utils.html import conditional_escape
from django.views import View  # ? to make class-based views you have to inherit it


# ? func-views always take request param
def simple(request: HttpRequest):
    return render(request=request, template_name="insert path to template here")


# ? use this when using params in GET
def guess_shitty(request: HttpRequest) -> HttpResponse:
    response = f"""<html><body>What the fuck is this guess {conditional_escape(request.GET['guess'])}</body></html>"""
    return HttpResponse(response)


# ? in urls.py: make "app/<int/slug/whatever_type:param>"
def another_guess_shitty(request: HttpRequest, param: int):
    response = f"Ok {conditional_escape(param)} HTML jargon"
    return HttpResponse(response)


def guess_dtl(request: HttpRequest):
    context: dict = {"place_holder": "42"}
    return render(request=request, template_name="path/to/template", context=context)


class Sophisticated(View):
    def get(self, request: HttpRequest, guess: int):
        context: dict = {"place_holder": "42"}

        return render(
            request=request, template_name="./templates/tmpl.html", context=context
        )


class Loop(View):
    fruits = [
        "apple",
        "banana",
        "orange",
    ]
    nuts = ["peanut", "cashew"]
    context = {
        "fruits": fruits,
        "nuts": nuts,
        "zap": "42",
    }

    def get(self, request):
        return render(
            request=request, template_name="./templates/tmpl.html", context=self.context
        )


def nested(request):
    x = {"outer": {"inner": "42"}}
    return render(request, "tmpl/nested.html")

