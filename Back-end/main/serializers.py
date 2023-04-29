from rest_framework import serializers
from .models import Flight#, Data

class FlightSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Flight        # product 모델 사용
        fields = '__all__'            # 모든 필드 포함

# class DataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Data
#         fields = '__all__'