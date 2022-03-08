from django.db import models


class Language(models.Model):  # ? ids are generated automatically
    name = models.CharField(max_length=200)


class Book(models.Model):
    """Referencing the Language model, and specify that it can be set to null (not a required field, all is required by default)"""

    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    # ? many books to 1 language
    # ? when you delete the row from the primary table, the language field gets set to null (can be set to default as well)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)


class BookInstancePhysical(models.Model):
    # ? many book-instances to 1 book
    # ? when you delete the row from the primary table, the whole row gets deleted
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    due_back = models.DateField(null=True, blank=True)


"""after that make the migrations (db-type agnostic) and migrate(depends on the db-type)"""
