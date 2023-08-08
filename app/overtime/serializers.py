from rest_framework import serializers

from .models import OvertimeRegister


class OvertimeRegisterSerializer(serializers.ModelSerializer):
    """Overtime data serializer"""

    class Meta:
        """Overtime metadata"""

        model = OvertimeRegister
        fields = ["employee", "hours", "reason", "creation_date"]
