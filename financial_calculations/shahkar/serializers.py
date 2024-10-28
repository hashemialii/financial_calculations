from rest_framework import serializers
from .models import ShahkarBasicModel, ShahkarIncomeModel


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShahkarIncomeModel
        fields = ['year', 'month', 'income']


class BasicSerializer(serializers.ModelSerializer):
    basic = IncomeSerializer(read_only=True)
    
    class Meta:
        model = ShahkarBasicModel
        fields = '__all__'
