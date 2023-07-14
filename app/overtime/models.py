from django.db import models
from django.urls import reverse
from employees.models import Employee


class OvertimeRegister(models.Model):
    """Default overtime register model"""

    reason = models.CharField(max_length=150)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.reason

    def get_absolute_url(self):
        """Return to the register list view"""
        return reverse("overtime_list")
