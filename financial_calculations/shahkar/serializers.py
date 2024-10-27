from rest_framework import serializers
from .models import ShahkarBasicModel, ShahkarIncomeModel


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShahkarIncomeModel
        fields = '__all__'


class BasicSerializer(serializers.ModelSerializer):
    basic = IncomeSerializer(read_only=True)
    
    class Meta:
        model = ShahkarBasicModel
        fields = ['year', 'month', 'amount', 'basic']
