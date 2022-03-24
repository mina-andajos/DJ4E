"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

# ? Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, "site")


# ? You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.
urlpatterns = [
    # ? admin dashboard
    path("admin/", admin.site.urls),
    # ? for user authentication
    path("accounts/", include("django.contrib.auth.urls")),
    # ? for social logins
    url(r"^oauth/", include("social_django.urls", namespace="social")),
    # ? home
    path("", include("home.urls")),
    # ?installed apps
    path("hello/", include("hello.urls")),
    path("polls/", include("polls.urls")),
    path("autos/", include("autos.urls")),
    path("cats/", include("cats.urls")),
    path("ads/", include("ads.urls")),
    path("homework/", include("homework.urls")),
    # ? for static sites
    url(
        r"^site/(?P<path>.*)$",
        serve,
        {"document_root": SITE_ROOT, "show_indexes": True},
        name="site_path",
    ),
    # ? for favicons
    path(
        "favicon.ico",
        serve,
        {"path": "favicon.ico", "document_root": os.path.join(BASE_DIR, "home/static")},
    ),
]

# ? use social logins if configured
try:
    from . import github_settings

    social_login = "registration/login_social.html"
    urlpatterns.insert(
        0,
        path(
            "accounts/login/", auth_views.LoginView.as_view(template_name=social_login)
        ),
    )
except Exception as e:
    print(
        f"------------\nSOCIAL LOGINS ERROR\n{e}\nUsing the default login template\n------------"
    )
