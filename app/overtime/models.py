from django.db import models
from employees.models import Employee


class OvertimeRegister(models.Model):
    """Default overtime register model"""

    reason = models.CharField(max_length=150)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.employee.name
