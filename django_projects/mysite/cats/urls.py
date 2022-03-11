from django.urls import path
from . import views

app_name = "cats"
urlpatterns = [
    #? showing all objects
    path("", name="all",view=views.CatView.as_view()),
    path("breed/",name="breed_list",view=views.BreedView.as_view()),
    #? CRUD cats
    path("cat/create/", name="cat_create",view=views.CatCreate.as_view()),
    path("cat/<int:pk>/update", name="cat_update",view=views.CatUpdate.as_view()),
    path("cat/<int:pk>/delete", name="cat_delete",view=views.CatDelete.as_view()),
    #? CRUD breeds
    path("breed/create/", name="breed_create",view=views.BreedCreate.as_view()),
    path("breed/<int:pk>/update", name="breed_update",view=views.BreedUpdate.as_view()),
    path("breed/<int:pk>/delete", name="breed_delete",view=views.BreedDelete.as_view()),
]
