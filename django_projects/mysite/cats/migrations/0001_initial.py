# Generated by Django 3.2.5 on 2022-03-10 23:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinValueValidator(limit_value=2, message='Breed names should contain at least 2 letters.')])),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinValueValidator(limit_value=2, message='Cat names should contain at least 2 letters.')])),
                ('weight', models.PositiveIntegerField()),
                ('foods', models.CharField(max_length=200)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.breed')),
            ],
        ),
    ]