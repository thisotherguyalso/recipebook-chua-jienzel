"""Models configuration for accounts app"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.


class Profile(models.Model):
    """Profile model for user"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(validators=[MinLengthValidator(11)])
    name = models.CharField(max_length=50)
