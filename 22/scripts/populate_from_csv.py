import csv
from os import path

from ..modelz_member import Person, Course, Membership


def run() -> None:
    path_to_file = path.join(path.pardir, "load.csv")
    file_handle = open(path_to_file)
    reader = csv.reader(file_handle)

    for model in Person, Course, Membership:
        model.objects.all().delete()

    for row in reader:
        print(row)

        person, created = Person.objects.get_or_create(email=row[0])
        course, created = Course.objects.get_or_create(title=row[2])

        if not row[1] == "I":
            role = Membership.LEARNER
        else:
            role = Membership.INSTRUCTOR

        membership = Membership(role=role, person=person, course=course)
        membership.save()
