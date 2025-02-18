# Generated by Django 4.0.2 on 2022-05-03 00:09

import BookCreator.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCreator',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('teacherId', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('order', models.IntegerField(primary_key=True, serialize=False)),
                ('dataType', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('pageNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('contentsList', djongo.models.fields.ArrayField(model_container=BookCreator.models.Content)),
            ],
        ),
    ]
