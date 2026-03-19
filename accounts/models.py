from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    '''Custom user'''

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        help_text="User's birth date"
    )

    def __str__(self):
        return self.username