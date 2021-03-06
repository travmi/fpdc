# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 03:24
from __future__ import unicode_literals

import computed_property.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Release",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("release_id", models.CharField(max_length=255, unique=True)),
                ("short", models.CharField(max_length=255)),
                ("version", models.IntegerField()),
                ("name", models.CharField(max_length=255)),
                ("release_date", models.DateField()),
                ("eol_date", models.DateField()),
                ("sigkey", models.CharField(max_length=255)),
                (
                    "status",
                    computed_property.fields.ComputedCharField(
                        compute_from="_status", editable=False, max_length=255, null=True
                    ),
                ),
                (
                    "active",
                    computed_property.fields.ComputedBooleanField(
                        compute_from="_active", default=True, editable=False
                    ),
                ),
            ],
        )
    ]
