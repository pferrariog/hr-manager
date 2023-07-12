from django.db import models
from django.urls import reverse_lazy
from employees.models import Employee


# Create your models here.
class Report(models.Model):
    """Default report model"""

    owner = models.ForeignKey(Employee, on_delete=models.PROTECT)
    description = models.CharField(max_length=100)
    file = models.FileField(upload_to="reports")

    def __str__(self) -> str:
        """Return a string representation"""
        return self.description

    def get_absolute_url(self):
        """Return to the document's owner page"""
        return reverse_lazy("edit_employee", args=[self.owner.id])
