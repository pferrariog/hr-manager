from django.db import models


class Company(models.Model):
    """Default company model"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text="Company name")
    description = models.CharField(
        max_length=100, help_text="Tiny company description", blank=True
    )

    def __str__(self) -> str:
        """Return a string representation"""
        return self.name
