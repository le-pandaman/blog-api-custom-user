from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):

    """
    Custom User Model
    """

    name = models.CharField(null=True, blank=True,  max_length=255)
