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


class DebtModel(models.Model):
    giver = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    receiver_phone_number = models.CharField(max_length=11, unique=True)
    giver_phone_number = models.CharField(max_length=11, unique=True)
    amount = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'from {self.giver.username} to {self.receiver.username}'

    class Meta:
        db_table = 'debts'
        verbose_name = 'Debt'
        verbose_name_plural = 'Debts'
