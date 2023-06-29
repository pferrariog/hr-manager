from django.db import models
from django.urls import reverse


class Company(models.Model):
    """Default company model"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.name

    def get_absolute_url(self):
        """Redirect to homepage"""
        return reverse("home")
