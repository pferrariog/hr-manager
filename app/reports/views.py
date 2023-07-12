from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView

from .models import Report


class CreateDocument(CreateView):
    """Attach a document to an employee"""

    model = Report
    fields = ["description", "file"]
    pk_url_kwarg = "id"

    def post(self, request, *args, **kwargs):
        """Override post method to attach document to an employee"""
        self.object = None  # Innitiate the object
        form = self.get_form()
        form.instance.owner_id = self.kwargs["id"]

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DeleteDocument(DeleteView):
    """Delete an employee's document"""

    model = Report
    pk_url_kwarg = "id"

    def get_success_url(self):
        """Override the default success url method"""
        return reverse_lazy("edit_employee", args=[self.object.owner.id])
