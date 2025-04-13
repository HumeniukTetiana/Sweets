from rest_framework import serializers
from sweets.models.OrderDetailsModel import OrderDetails

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'
