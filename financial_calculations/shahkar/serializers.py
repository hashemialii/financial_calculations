from rest_framework import serializers
from .models import ShahkarModelBasic, ShahkarModelIncome


class BasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShahkarModelBasic
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    basic = BasicSerializer()

    class Meta:
        model = ShahkarModelIncome
        fields = '__all__'
