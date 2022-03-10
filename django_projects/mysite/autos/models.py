from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Make(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a make (e.g. Dodge)",  # ? greyed-out text on field
        validators=[
            MinLengthValidator(
                limit_value=2,
                message="Make must at least have 2 characters.",
            )
        ],
    )

    def __str__(self) -> str:
        return self.name


class Auto(models.Model):
    nickname = models.CharField(
        max_length=200,
        help_text="Enter an Auto Nickname",  # ? greyed-out text on field
        validators=[
            MinLengthValidator(
                limit_value=2,
                message="Auto must at least have 2 characters.",
            )
        ],
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey(to=Make, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        """what shows up in the admin panel"""
        return self.nickname
