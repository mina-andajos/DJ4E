# Create your views here.
from django.db.models import F
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


def owner(request: HttpRequest):
    return HttpResponse("Hello, world. 8fe69eac is the polls index.")


# ! UNUSED
def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    response = render(
        request=request, template_name="polls/index.html", context=context
    )
    return HttpResponse(response)


# ! UNUSED
def detail(request: HttpRequest, question_id: str):
    question = get_object_or_404(Question, pk=question_id)

    # !Equivalent of:
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # !There's also get_list_or_404() that work as filter()
    # !and returns 404 if list is empty

    return render(request, "polls/detail.html", {"question": question})


# ! UNUSED
def results(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(
        request=request,
        template_name="polls/results.html",
        context={"question": question},
    )


def vote(request: HttpRequest, question_id: str):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):  # ? Incase no choice is submitted
        # ? Redisplay the question voting form.
        return render(
            request=request,
            template_name="polls/detail.html",
            context={
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )

    else:  # ? I selected a choice
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # ! ALWAYS RETRUN HttpResponseRedirect after a successful post
        # ! because of POST refresh cycle

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    # ? default template name is <app name>/<model name>_list.html
    context_object_name = "latest_question_list"
    # ? default context name would've been "question_list"

    def get_queryset(self):
        """Return the last five published questions"""

        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    # ? default template name is "<appname>/<modelname>_detail.html"
    # ? for context, variable "question" is already provided in context


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
