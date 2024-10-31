from rest_framework import serializers
from debts.models import UserModel, DebtModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class DebtSerializer(serializers.ModelSerializer):
    giver_phone_number = serializers.CharField(source='giver.phone_number', read_only=True)
    receiver_phone_number = serializers.CharField(source='receiver.phone_number', read_only=True)

    class Meta:
        model = DebtModel
        fields = '__all__'
