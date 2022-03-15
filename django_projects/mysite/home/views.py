import logging

from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

logging.basicConfig(level=logging.DEBUG)


# Create your views here.
class AppsIndexUrls(View):
    def is_third_party(self, app: str) -> bool:
        filtered_apps: tuple = ("home.apps.HomeConfig",)
        result: bool = (
            (app not in filtered_apps)
            and (".apps." in app)
            and (app.endswith("Config"))
        )
        return result

    def get_third_party_apps(self):
        """returns a list of user-made and third-party app index urls"""

        app_index_urls = []
        for app in settings.INSTALLED_APPS:
            if self.is_third_party(app):
                app_index_url = app.split(".")  # ?app.apps.AppConfig
                app_index_urls.append(app_index_url[0])

        return app_index_urls

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name = "home/main.html"
        app_index_urls = self.get_third_party_apps()

        host = request.get_host()
        is_local: bool = "localhost" in host or "127.0.0.1" in host

        context = {
            "app_index_urls": app_index_urls,
            "islocal": is_local,
        }

        return render(
            request=request,
            template_name=template_name,
            context=context,
        )
