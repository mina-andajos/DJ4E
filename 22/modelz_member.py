from django.db import models


class Person(models.Model):
    email = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128, null=True)

    def __str__(self) -> str:
        return self.email


class Course(models.Model):
    title = models.CharField(max_length=128, unique=True)
    # ?
    members = models.ManyToManyField(
        to=Person,
        through="Membership",
        related_name="courses",
    )

    def __str__(self) -> str:
        return self.title


class Membership(models.Model):
    """The junction table with data in it"""

    # ? keys to the other tables
    person = models.ForeignKey(
        to=Person,
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #! IT WOULD'VE BEEN BETTER AS CLASS OR AN ENUM
    #! maybe a dict too
    # ? associating relations to integers are better than just strings
    LEARNER = 1
    IA = 1000
    GSI = 2000
    INSTRUCTOR = 5000
    ADMIN = 10000

    # ? verbose names for the UI
    MEMBER_CHOICES = (
        (LEARNER, "Learner"),
        (IA, "International Instructor"),
        (GSI, "Grad Student Instructor"),
        (INSTRUCTOR, "Instructor"),
        (ADMIN, "Administrator"),
    )

    # ? what we will show in the forms, in a select menu
    role = models.IntegerField(
        choices=MEMBER_CHOICES,
        default=LEARNER,
    )

    def __str__(self) -> str:
        return f"Person {self.person.id} <--> Course {self.course.id}"
