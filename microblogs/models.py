from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    username = models.CharField(
        max_length=30, 
        unique=True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='Username must consist of an @ followed by at least 3 alphanumericals'
        )]
    )
    bio = models.TextField()