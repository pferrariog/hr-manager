from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .models import Employee


class ListEmployees(ListView):
    """Default employees list view"""

    model = Employee

    def get_queryset(self):
        """Override the default method to filter the query and return only current company employees"""
        current_company = self.request.user.employee.company
        return Employee.objects.filter(company=current_company)


class EditEmployee(UpdateView):
    """Default update employee view"""

    model = Employee
    fields = ["name", "departments"]
    pk_url_kwarg = "id"
