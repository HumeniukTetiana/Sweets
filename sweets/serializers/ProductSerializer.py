from rest_framework import serializers
from sweets.models.ProductModel import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
