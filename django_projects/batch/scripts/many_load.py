import csv
import unesco.models as models
from django.apps import apps
from unesco.urls import app_name


def clear_models() -> None:
    _app_models = apps.get_app_config(app_name).get_models()
    for model in _app_models:
        model.objects.all().delete()

    return None


def read_csv(path: str):
    _file_handle = open(path)
    _csv_reader = csv.reader(_file_handle)
    next(_csv_reader)

    return _csv_reader


def fill_float_fields(row) -> tuple:
    try:
        year = int(row[3])
    except Exception:
        year = None
    try:
        area_hectares = float(row[6])
    except Exception:
        area_hectares = None
    try:
        longitude = float(row[4])
    except Exception:
        longitude = None
    try:
        latitude = float(row[5])
    except Exception:
        latitude = None

    return year, area_hectares, longitude, latitude


def fill_foreign_fields(row) -> tuple:
    category, created = models.Category.objects.get_or_create(name=row[-4])
    state, created = models.State.objects.get_or_create(name=row[-3])
    region, created = models.Region.objects.get_or_create(name=row[-2])
    iso, created = models.Iso.objects.get_or_create(name=row[-1])

    return category, state, region, iso


def fill_models(csv_reader) -> None:
    # name,description,justification,year,longitude,latitude,area_hectares,category,state,region,iso

    for row in csv_reader:

        year, area_hectares, longitude, latitude = fill_float_fields(row)
        category, state, region, iso = fill_foreign_fields(row)

        site = models.Site(
            name=row[0],
            description=row[1],
            justification=row[2],
            year=year,
            longitude=longitude,
            latitude=latitude,
            area_hectares=area_hectares,
            category=category,
            state=state,
            region=region,
            iso=iso,
        )
        site.save()

    return None


def run():
    clear_models()
    csv_reader = read_csv("unesco/whc-sites-2018-clean.csv")
    fill_models(csv_reader)
