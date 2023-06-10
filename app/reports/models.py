from django.db import models
from employees.models import Employee


# Create your models here.
class Report(models.Model):
    """Default report model"""

    owner = models.ForeignKey(Employee, on_delete=models.PROTECT)
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.description
