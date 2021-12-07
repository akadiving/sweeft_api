from rest_framework import serializers
from .models import Category, Activity

class ActivitySerializer(serializers.Serializer):
    """
    Serializer for Acitivities
    """
    activity = serializers.CharField()
    type = serializers.CharField()
    price = serializers.FloatField()
    

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Acitivities
    """

    total_activities = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'total_activities']

