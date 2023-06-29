# Generated by Django 4.2.2 on 2023-06-28 22:16

import django.db.models.deletion

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    """Default migration"""

    dependencies = [
        ("companies", "0001_initial"),
        ("employees", "0003_alter_employee_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="companies.company",
            ),
        ),
    ]
