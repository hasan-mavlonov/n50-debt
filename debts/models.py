from django.contrib.auth.models import AbstractUser
from django.db import models



class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

