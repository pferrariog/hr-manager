# Generated by Django 4.2.2 on 2023-06-08 17:11

import django.db.models.deletion

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    """Migration"""

    dependencies = [
        ("employees", "0003_alter_employee_user"),
        ("reports", "0002_report_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="owner",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.PROTECT, to="employees.employee"
            ),
            preserve_default=False,
        ),
    ]
