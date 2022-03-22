from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from . import views


app_name = "ads"
urlpatterns = [
    path("", views.AdListView.as_view(), name="all"),
    path("ad/<int:pk>", views.AdDetailView.as_view(), name="ad_detail"),
    path(
        "ad/create",
        views.AdCreateView.as_view(success_url=reverse_lazy("ads:all")),
        name="ad_create",
    ),
    path(
        "ad/<int:pk>/update",
        views.AdUpdateView.as_view(success_url=reverse_lazy("ads:all")),
        name="ad_update",
    ),
    path(
        "ad/<int:pk>/delete",
        views.AdDeleteView.as_view(success_url=reverse_lazy("ads:all")),
        name="ad_delete",
    ),
    path("pic_picture/<int:pk>", views.stream_file, name="pic_picture"),
]
