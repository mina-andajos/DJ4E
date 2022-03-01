from django.urls import path
from django.views.generic import TemplateView

import viewz

app_name = "tmpl"
urlpatterns = [
    path("", TemplateView.as_view(template_name="path/to/template")),
    path("simple", viewz.simple),
    path("guess_shitty", viewz.guess_shitty),
    path("another_guess_shitty/<int:param>", viewz.another_guess_shitty),
    path("guess_dtl", viewz.guess_dtl),
    path("sophisticated", viewz.sophisticated.as_view()),
]
