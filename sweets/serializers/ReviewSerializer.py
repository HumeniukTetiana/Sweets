from rest_framework import serializers
from sweets.models.ReviewModel import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
