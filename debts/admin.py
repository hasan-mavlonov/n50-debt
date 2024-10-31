# debts/admin.py

from django.contrib import admin
from .models import UserModel, DebtModel

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'is_active')  # Customize fields to display
    search_fields = ('username', 'phone_number')  # Enable search functionality

@admin.register(DebtModel)
class DebtModelAdmin(admin.ModelAdmin):
    list_display = ('giver', 'receiver', 'amount', 'status')  # Customize fields to display
    list_filter = ('status',)  # Enable filtering by status
    search_fields = ('giver__username', 'receiver__username')  # Enable searching by username
