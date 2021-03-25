from rest_framework import serializers
from .models import *

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewTarget
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class ChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'date',
            'rating'
        ]