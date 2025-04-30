from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sweets import serializers
from sweets import repositories

repository = repositories.ProductRepository

@api_view(['GET'])
def get_all_products(request):
    products = repository.get_all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_by_id(request, pk):
    product = repository.get_by_id(pk)
    if not product:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = repository.create(**serializer.validated_data)
        return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_product(request, pk):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = repository.update(pk, **serializer.validated_data)
        if product:
            return Response(ProductSerializer(product).data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request, pk):
    success = repository.delete(pk)
    if success:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
