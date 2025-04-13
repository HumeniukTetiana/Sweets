from rest_framework import serializers
from sweets.models.IngredientModel import Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
