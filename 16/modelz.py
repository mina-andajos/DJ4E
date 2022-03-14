from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, ">2 pls")],
    )
    #? we only want to show this to the user, the rest is handeled internally
    text = models.TextField()

    #? setting up the owner for this field that can only edit,delete it
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
