from . import views
from django.urls import path

app_name = "homework"
urlpatterns = [path("", views.MainView.as_view(), name="main")]
