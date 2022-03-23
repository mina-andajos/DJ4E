from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

from taggit.managers import TaggableManager

# Create your models here.


class Ad(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(
                2,
                "Title must be greater than 2 characters",
            )
        ],
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
    )
    text = models.TextField()

    # ? auto-generated
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(
        max_length=256, null=True, help_text="the MIME_TYPE of the file"
    )

    comments = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through="Comment",
        related_name="comments_owner",
    )

    favorites = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through="Favorite",
        related_name="favorite_ads",
    )

    tags=TaggableManager(blank=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    text = models.TextField(
        validators=[
            MinLengthValidator(
                limit_value=3,
                message="Comment must be greater than 3 characters",
            )
        ]
    )

    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        if len(self.text) < 15:
            return self.text
        else:
            return f"{self.text[:11]} ..."


class Favorite(models.Model):
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites_users",
    )

    class Meta:
        unique_together = ["ad", "user"]  # ? only one combination

    def __str__(self) -> str:
        return f"{self.user.username} likes {self.ad.title[:10]}"
