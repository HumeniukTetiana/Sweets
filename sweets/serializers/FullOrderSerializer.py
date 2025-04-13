from rest_framework import serializers
from sweets.models.FullOrderModel import FullOrder

class FullOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullOrder
        fields = '__all__'
