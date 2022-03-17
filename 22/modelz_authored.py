from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)

    # ? mentioning the junction table (using the "through" param)

    authors = models.ManyToManyField(to="Author", through="Authored")


class Author(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(to="Book", through="Authored")


class Authored(models.Model):
    """The junction table, child of both tables"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
