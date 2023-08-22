from overtime.serializers import OvertimeRegisterSerializer
from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """Employee data serializer"""

    overtimeregister_set = OvertimeRegisterSerializer(many=True)

    class Meta:
        """Employee metadata"""

        model = Employee
        fields = [
            "id",
            "name",
            "departments",
            "company",
            "total_overtime_hours",
            "overtimeregister_set",
        ]
