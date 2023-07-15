from django.forms import ModelForm
from employees.models import Employee

from .models import OvertimeRegister


class OvertimeRegisterForm(ModelForm):
    """Override the default Django ModelForm"""

    def __init__(self, user, *args, **kwargs):
        """Class initializer"""
        super().__init__(*args, **kwargs)
        # Get employees only from the current company
        self.fields["employee"].queryset = Employee.objects.filter(company=user.employee.company)

    class Meta:
        """Model metadata"""

        model = OvertimeRegister
        fields = "__all__"
