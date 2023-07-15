from companies.models import Company
from django.db import models
from django.urls import reverse


class Department(models.Model):
    """Default department model"""

    name = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.name

    def get_absolute_url(self):
        """Return to the departments list view"""
        return reverse("departments_list")
