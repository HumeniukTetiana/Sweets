from rest_framework import serializers
from sweets.models.CategoryModel import Category
from sweets.models.FullOrderModel import FullOrder
from sweets.models.ReviewModel import Review
from sweets.models.ProductModel import Product
from sweets.models.ProductIngredientModel import ProductIngredient
from sweets.models.PersonModel import Person
from sweets.models.OrderDetailsModel import OrderDetails
from sweets.models.IngredientModel import Ingredient


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class FullOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullOrder
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ProductIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductIngredient
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



