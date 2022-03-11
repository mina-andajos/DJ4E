from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Breed(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a Cat Breed (e.g. Shirazi)",
        validators=[
            MinLengthValidator(
                limit_value=2,
                message="Breed names should contain at least 2 letters.",
            )
        ],
    )

    def __str__(self) -> str:
        return self.name


class Cat(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(
                limit_value=2,
                message="Cat names should contain at least 2 letters.",
            )
        ],
    )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=200)
    breed = models.ForeignKey(to=Breed, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.nickname
