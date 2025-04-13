from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from sweets.serializers.CategorySerializer import CategorySerializer
from sweets.repositories.CategoryRepository import CategoryRepository

repository = CategoryRepository()

@api_view(['GET'])
def get_all_categories(request):
    categories = repository.get_all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_category_by_id(request, pk):
    category = repository.get_by_id(pk)
    if not category:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        category = repository.create(**serializer.validated_data)
        return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_category(request, pk):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        category = repository.update(pk, **serializer.validated_data)
        if category:
            return Response(CategorySerializer(category).data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_category(request, pk):
    success = repository.delete(pk)
    if success:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
