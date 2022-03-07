from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class Visits(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        # ? get the num_visits key from the session keys, and default the value to zero if none found, and then add 1 to the variable
        num_visits: int = request.session.get("num_visits", 0) + 1
        # ? change the sessions num_visits key to the new value
        request.session["num_visits"] = num_visits
        # ? if the new variable is >4 then remove the num_visits key from the session resetting it
        if num_visits > 4:
            del request.session["num_visits"]

        response = HttpResponse(f"view count={str(num_visits)}")
        response.set_cookie("dj4e_cookie", "8fe69eac", max_age=1000)

        return response
