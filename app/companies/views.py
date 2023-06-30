from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from .models import Company


class CreateCompany(CreateView):
    """Default create company view"""

    model = Company
    fields = ["name", "description"]

    def form_valid(self, form):
        """Attachs the created company to the current user"""
        company_object = form.save()
        employee = self.request.user.employee
        employee.company = company_object
        employee.save()
        return HttpResponse("Ok")


class EditCompany(UpdateView):
    """Update company information"""

    model = Company
    fields = ["name", "description"]
    pk_url_kwarg = "id"
