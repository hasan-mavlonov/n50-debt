from rest_framework import serializers
from models import UserModel, DebtModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtModel
        fields = '__all__'
