from companies.models import Company
from departments.models import Department
from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    """Default employee model"""

    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    departments = models.ManyToManyField(Department)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.name
