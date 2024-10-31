from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name="custom_user_groups",  # Custom related name to avoid conflicts
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="custom_user_permissions",  # Custom related name to avoid conflicts
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class DebtModel(models.Model):
    giver = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="debts_given"
    )
    receiver = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="debts_received"
    )
    receiver_phone_number = models.CharField(max_length=11)
    giver_phone_number = models.CharField(max_length=11)
    amount = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'from {self.giver.username} to {self.receiver.username}'

    class Meta:
        db_table = 'debts'
        verbose_name = 'Debt'
        verbose_name_plural = 'Debts'
