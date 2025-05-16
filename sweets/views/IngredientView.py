from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sweets.serializers import IngredientSerializer
from sweets import repositories

repository = repositories.IngredientRepository()

@api_view(['GET'])
def get_all_ingredients(request):
    ingredients = repository.get_all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_ingredient_by_id(request, pk):
    ingredient = repository.get_by_id(pk)
    if not ingredient:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = IngredientSerializer(ingredient)
    return Response(serializer.data)

@api_view(['POST'])
def create_ingredient(request):
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid():
        ingredient = repository.create(**serializer.validated_data)
        return Response(IngredientSerializer(ingredient).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_ingredient(request, pk):
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid():
        ingredient = repository.update(pk, **serializer.validated_data)
        if ingredient:
            return Response(IngredientSerializer(ingredient).data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_ingredient(request, pk):
    success = repository.delete(pk)
    if success:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
