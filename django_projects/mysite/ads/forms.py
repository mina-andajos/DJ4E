from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

from ads.humanize import natural_size
from ads.models import Ad


class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = natural_size(max_upload_limit)

    picture = forms.FileField(
        required=False,
        label=f"File to upload <= {max_upload_limit_text}",
    )
    upload_field_name = "picture"

    class Meta:
        model = Ad
        fields = [
            "title",
            "text",
            "picture",
            "price",
        ]

    def clean(self):
        """
        inherited from the parent class
        We add further validation to it
        """

        # ? returns a mapping that has picture data
        cleaned_data = super().clean()
        if cleaned_data is None or cleaned_data.get("picture") is None:
            return None

        else:
            picture = cleaned_data.get("picture")

            if len(picture) > self.max_upload_limit:
                self.add_error(
                    field="picture",
                    error=f"File must be < {self.max_upload_limit_text} bytes",
                )

    def save(self, commit: bool = True):
        instance = super(CreateForm, self).save(commit=False)
        picture_in_memory = instance.picture

        # ? extracting data
        if isinstance(picture_in_memory, InMemoryUploadedFile):
            byte_array = picture_in_memory.read()
            instance.picture = byte_array
            instance.content_type = picture_in_memory.content_type

        if commit:
            instance.save()

        return instance


class CommentForm(forms.Form):
    comment = forms.CharField(
        required=True,
        max_length=500,
        min_length=3,
        strip=True,
    )
