from django import forms  # ? we'll inherit from forms.Forms
from django.core.exceptions import ValidationError
from django.core import validators  # ? to validate user inputs


class BasicForm(forms.Form):
    # ? adding a character field called title. we're adding validators for setting a minimum length and adding an error message
    title = forms.CharField(
        validators=[
            validators.MinLengthValidator(
                limit_value=2, message="Please enter 2 or more characters"
            )
        ]
    )
    # ? integer field just like the html one
    mileage = forms.IntegerField()
    # ? date field is a datefield
    purchase_date = forms.DateField()
