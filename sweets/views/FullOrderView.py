from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from sweets import serializers
from sweets import repositories

repository = repositories.FullOrderRepository

@api_view(['GET'])
def get_all_orders(request):
    orders = repository.get_all()
    serializer = FullOrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_order_by_id(request, pk):
    order = repository.get_by_id(pk)
    if not order:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = FullOrderSerializer(order)
    return Response(serializer.data)


@api_view(['POST'])
def create_order(request):
    serializer = FullOrderSerializer(data=request.data)
    if serializer.is_valid():
        order = repository.create(**serializer.validated_data)
        return Response(FullOrderSerializer(order).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_order(request, pk):
    serializer = FullOrderSerializer(data=request.data)
    if serializer.is_valid():
        order = repository.update(pk, **serializer.validated_data)
        if order:
            return Response(FullOrderSerializer(order).data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_order(request, pk):
    success = repository.delete(pk)
    if success:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
