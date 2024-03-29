from companies.models import Company
from departments.models import Department
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Employee(models.Model):
    """Default employee model"""

    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    departments = models.ManyToManyField(Department)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.name

    def get_absolute_url(self):
        """Return to the employees list view"""
        return reverse("employees_information")

    @property
    def total_overtime_hours(self):
        """Sum the amount of overtime register hours"""
        registers = self.overtimeregister_set.all()
        total_dict = registers.aggregate(models.Sum("hours"))
        return total_dict["hours__sum"]
