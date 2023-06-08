from django.db import models


# Create your models here.
class Report(models.Model):
    """Default report model"""

    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.name
