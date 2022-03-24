from django import forms


class MainForm(forms.Form):
    field1 = forms.CharField(
        max_length=200,
        min_length=2,
        strip=True,
        required=False,
        initial="",
        help_text="Please enter a word...",
        label="Field1",
    )
    field2 = forms.CharField(
        max_length=200,
        min_length=2,
        strip=True,
        required=False,
        initial="",
        help_text="Please enter a word...",
        label="Field2",
    )
