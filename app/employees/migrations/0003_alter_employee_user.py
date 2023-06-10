# Generated by Django 4.2.2 on 2023-06-08 17:06

import django.db.models.deletion

from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    """Migration"""

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("employees", "0002_employee_company_employee_departments_employee_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
