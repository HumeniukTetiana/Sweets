from rest_framework import serializers
from sweets.models.ProductIngredientModel import ProductIngredient

class ProductIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductIngredient
        fields = '__all__'
