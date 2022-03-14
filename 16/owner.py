from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models


class OwnerListView(ListView):
    pass


class OwnerDetailView(DetailView):
    pass


class OwnerCreateView(LoginRequiredMixin, CreateView):
    """we add the owner to the form through this view"""

    def form_valid(self, form):
        """modifying the inherited form_valid method"""

        object = form.save(commit=False)  # ? getting the form data
        object.owner = self.request.user  # ? adding the owner attribute to the model
        object.save()

        return super(OwnerCreateView, self).form_valid(
            form=form
        )  # ? making the super inherit from OwnerCreateView and saving the form


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """pass the request to form and limit the queryset to the requesting user"""

    def get_queryset(self) -> models.query.QuerySet:
        """limit the the user to only modifying their data"""

        query_set = super(OwnerUpdateView, self).get_queryset()
        return query_set.filter(owner=self.request.user)


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    def get_queryset(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)
