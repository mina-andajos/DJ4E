# Create your views here.
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template import loader

from .models import Question


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    response = render(
        request=request, template_name="polls/index.html", context=context
    )
    return HttpResponse(response)


def detail(request: HttpRequest, question_id: str):
    question = get_object_or_404(Question, pk=question_id)

    #!Equivalent of:
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    #!There's also get_list_or_404() that work as filter() and returns 404 if list is empty

    return render(request, "polls/detail.html", {"question": question})


def results(request: HttpRequest, question_id: str):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request: HttpRequest, question_id: str):
    return HttpResponse(f"You're voting on question {question_id}.")

def owner(request:HttpRequest):
    return HttpResponse("Hello, world. 8fe69eac is the polls index.")
