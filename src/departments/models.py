from django.db import models


class Department(models.Model):
    """Default department model"""

    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.name
