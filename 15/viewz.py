from formz import BasicForm
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse


def example(request: HttpRequest):
    form = (
        BasicForm()
    )  # ? we made an instance of the BasicForm class we defines in formz
    return HttpResponse(
        form.as_table()
    )  # ? we're displaying the form instance as a table in html
    #! laying elements out in an html table is very bad


class DumpPostView(View):  # Reusable bit...
    def post(self, request):
        dump = dumpdata("POST", request.POST)
        ctx = {"title": "request.POST", "dump": dump}
        return render(request, "form/dump.html", ctx)


class SimpleCreate(DumpPostView):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = BasicForm()
        context = {"form": form}

        return render(request, "form/form.html", context)


class SimpleUpdate(DumpPostView):
    def get(self, request: HttpRequest) -> HttpResponse:
        old_data = {
            "title": model.title,
            "mileage": model.mileage,
            "purchase_date": model.purchase_date,
        }

        form = BasicForm(initial=old_data)
        context = {"form": form}

        return render(
            request,
            template_name="form/form.html",
            context=context,
        )


class Validate(DumpPostView):
    """same as SimpleUpdate but with validation"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """what gets sent once the user hits edit data"""

        old_data = {
            "title": model.title,
            "mileage": model.mileage,
            "purchase_date": model.purchase_date,
        }  # ? getting the old data in a mapping
        form = BasicForm(initial=old_data)  # ? filling a form with it
        context = {"form": form}  # ? adding to context to fill in the template

        return render(request, template_name="form/form.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        """once the user hits submit and finished editing"""

        form = BasicForm(
            initial=request.POST
        )  # ? filling a form with the data that the user submitted to validate it. (notice it came back to the BasicForm class). It contains the error messages too.
        if not form.is_valid():
            # ? if the submitted data is not valid just fill it back to the template and send it back to the user
            context = {"form": form}

            return render(request, "form/form.html", context)

        else:
            # ? we will save the date and redirect the user somewhere else
            model.save()

            return redirect(to=reverse(viewname="form:success"))


def success(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Thank You!")
