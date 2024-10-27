from rest_framework import serializers
from .models import ShahkarBasicModel, ShahkarIncomeModel


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShahkarIncomeModel
        fields = '__all__'


class BasicSerializer(serializers.ModelSerializer):
    # Remove `basic` from being a required input, it will be created programmatically
    class Meta:
        model = ShahkarBasicModel
        fields = ['year', 'month', 'amount']  # Only keep necessary fields from user input
