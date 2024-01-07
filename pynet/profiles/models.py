from django.contrib.auth.models import AbstractUser
from django.db import models


class UserNet(AbstractUser):
    """Custom user model """
    middle_name = models.CharField(max_length=50, null=True)
    first_login = models.DateTimeField(null=True)
    phone_number = models.CharField(max_length=14, null=True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)

