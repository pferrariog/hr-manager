from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import OvertimeRegister


class ListOvertimeRegisters(ListView):
    """List all register of an employee"""

    model = OvertimeRegister

    def get_queryset(self):
        """
        Override the default method to filter the query and return only current company departments

        The dunder in employee__company drive the query to a second level
        allowing the filter to get company from register's employee
        """
        current_company = self.request.user.employee.company
        return OvertimeRegister.objects.filter(employee__company=current_company)


class CreateOvertimeRegister(CreateView):
    """Create a overtime register to an employee"""

    model = OvertimeRegister
    fields = ["hours", "reason"]


class EditOvertimeRegister(UpdateView):
    """Update a register's fields"""

    model = OvertimeRegister
    pk_url_kwarg = "id"
    fields = "__all__"


class DeleteOvertimeRegister(DeleteView):
    """Delete an employee's register"""

    model = OvertimeRegister
    pk_url_kwarg = "id"
    success_url = reverse_lazy("")
