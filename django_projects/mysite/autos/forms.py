from django.forms import ModelForm
from autos.models import Make


class MakeForm(ModelForm):
    """making a form that is utilizing the model, all the work and validation is going to be on the model"""

    class Meta:
        """we make a Meta class so the field can adapt to the model"""

        model = Make  # ? selecting the model to be displayed on the form
        fields = "__all__"  # ? selecting all the models fields
