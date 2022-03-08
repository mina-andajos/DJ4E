import logging

from django.conf import settings
from django.views.generic import ListView

logging.basicConfig(level=logging.DEBUG)


# Create your views here.
class AppsIndexUrls(ListView):
    template_name = "home/main.html"
    context_object_name = "app_index_urls"

    def is_third_party(self, app: str) -> bool:
        filtered_apps: tuple = ("home.apps.HomeConfig",)
        result: bool = (
            (app not in filtered_apps)
            and (".apps." in app)
            and (app.endswith("Config"))
        )
        return result

    def get_queryset(self):
        """returns a list of user-made and third-party app index urls"""
        app_index_urls = []
        for app in settings.INSTALLED_APPS:
            if self.is_third_party(app):
                app_index_url = app.split(".")  # ?app.apps.AppConfig
                app_index_urls.append(app_index_url[0])

        return app_index_urls
