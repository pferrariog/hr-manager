from django.contrib.auth.models import User
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
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


class DeleteEmployee(DeleteView):
    """Default delete employee view"""

    model = Employee
    pk_url_kwarg = "id"
    success_url = reverse_lazy("employees_information")


class CreateEmployee(CreateView):
    """Default create employee view"""

    model = Employee
    fields = ["name", "departments"]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Override base form_valid function"""
        employee_object = form.save(commit=False)
        employee_object.company = self.request.user.employee.company
        employee_object.user = User.objects.create(  # TODO add field to model form
            username="".join(employee_object.name.split(" "))
        )
        employee_object.save()
        return super(CreateEmployee, self).form_valid(form)
