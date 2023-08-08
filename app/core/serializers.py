from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User data serializer"""

    class Meta:
        """User metadata"""

        model = User
        fields = ["url", "username", "email"]
