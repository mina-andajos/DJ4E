#! PUT THAT STUFF IN MODELS.PY IN YOUR PROJECT FOLDER

from django.db import models


class User(models.Model):
    """
    CREATE TABLE Users(
        name VARCHAR(128),
        email VARCHAR(128)
    );
    """

    # ? id field/attribute gets added automatically
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    """
    `django_projects/mysite $python manage.py makemigrations` -> makes migrations that can be added
    `$python manage.py migrate` -> adds the migrations, adding the user model to db.sqlite3
    """
    """
    `$python manage.py shell` -> ads
    """


def create_user_mina():
    mina = User(name="Mina", email="mina@eng.asu.edu.eg")
    # ? creates a user but doesn't write it to db yet
    # INSERT INTO Users (name,email) VALUES ("Mina","mina@eng.asu.edu.eg")
    mina.save()  # ? now writing
    print(mina.id)  # ? accessing the id attr


def show_queries():
    from django.db import connection

    return connection.queries


def user_CRUD(model: models.Model):
    print(model.objects.values())  # ? returns all rows from table
    print(
        model.objects.filter(email="kza kza").values()
    )  # ? filtering returns certain rows
    model.objects.filter(email="kza kza").delete()  # ? filtering then deletion
    model.objects.filter(email="kza@kza").update(
        name="name"
    )  # ? filtering then updating
    model.objects.order_by("email")  # ? ordering selection based on field
    model.objects.order_by("-name")  # ? ordering in descending order


def main():
    create_user_mina()
    show_queries()


if __name__ == "__main__":
    main()
