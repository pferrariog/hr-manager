from django.db import models


class OvertimeRegister(models.Model):
    """Default overtime register model"""

    reason = models.CharField(max_length=150)

    def __str__(self) -> str:
        """Return a string representation"""
        return self.name
