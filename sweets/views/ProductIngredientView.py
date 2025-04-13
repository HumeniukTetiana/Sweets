from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sweets.serializers.ProductIngredientSerializer import ProductIngredientSerializer
from sweets.repositories.ProductIngredientRepository import ProductIngredientRepository

repository = ProductIngredientRepository()

@api_view(['GET'])
def get_all_product_ingredients(request):
    items = repository.get_all()
    serializer = ProductIngredientSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_ingredient_by_id(request, pk):
    item = repository.get_by_id(pk)
    if not item:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductIngredientSerializer(item)
    return Response(serializer.data)

@api_view(['POST'])
def create_product_ingredient(request):
    serializer = ProductIngredientSerializer(data=request.data)
    if serializer.is_valid():
        item = repository.create(**serializer.validated_data)
        return Response(ProductIngredientSerializer(item).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_product_ingredient(request, pk):
    serializer = ProductIngredientSerializer(data=request.data)
    if serializer.is_valid():
        item = repository.update(pk, **serializer.validated_data)
        if item:
            return Response(ProductIngredientSerializer(item).data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product_ingredient(request, pk):
    success = repository.delete(pk)
    if success:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
