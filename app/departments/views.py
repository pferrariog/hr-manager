from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import Department


class ListDepartments(ListView):
    """List all departments from current user's company"""

    model = Department

    def get_queryset(self):
        """Override the default method to filter the query and return only current company departments"""
        current_company = self.request.user.employee.company
        return Department.objects.filter(company=current_company)


class CreateDepartment(CreateView):
    """Create a department to the current user's company"""

    model = Department
    fields = ["name"]

    def form_valid(self, form):
        """Override base form_valid function"""
        employee_object = form.save(commit=False)
        employee_object.company = self.request.user.employee.company
        employee_object.save()
        return super(CreateDepartment, self).form_valid(form)


class EditDepartment(UpdateView):
    """Update a department of the current user's company"""

    model = Department
    fields = ["name"]
    pk_url_kwarg = "id"


class DeleteDepartment(DeleteView):
    """Delete a department of the current user's company"""

    model = Department
    pk_url_kwarg = "id"
    success_url = reverse_lazy("departments_list")
