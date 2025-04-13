from rest_framework import serializers
from sweets.models.CategoryModel import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']
