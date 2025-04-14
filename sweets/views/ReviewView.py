from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from sweets.serializers.ReviewSerializer import ReviewSerializer
from sweets.repositories.ReviewRepository import ReviewRepository
from rest_framework.permissions import IsAuthenticated

repository = ReviewRepository()

@api_view(['GET'])
def get_all_reviews(request):
    reviews = repository.get_all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_review_by_id(request, pk):
    review = repository.get_by_id(pk)
    if not review:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        review = repository.create(**serializer.validated_data)
        return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_review(request, pk):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        review = repository.update(pk, **serializer.validated_data)
        if review:
            return Response(ReviewSerializer(review).data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_review(request, pk):
    success = repository.delete(pk)
    if success:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
