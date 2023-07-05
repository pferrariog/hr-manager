from django.views.generic import ListView

from .models import Department


class ListDepartments(ListView):
    """List all departments from current user's company"""

    model = Department

    def get_queryset(self):
        """Override the default method to filter the query and return only current company departments"""
        current_company = self.request.user.employee.company
        return Department.objects.filter(company=current_company)
