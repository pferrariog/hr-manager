from django.db import models


class Employee(models.Model):
    """Default employee model"""

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.name
