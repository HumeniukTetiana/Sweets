from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sweets.serializers.OrderDetailsSerializer import OrderDetailsSerializer
from sweets.repositories.OrderDetailsRepository import OrderDetailsRepository

repository = OrderDetailsRepository()

@api_view(['GET'])
def get_all_order_details(request):
    details = repository.get_all()
    serializer = OrderDetailsSerializer(details, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_order_detail_by_id(request, pk):
    detail = repository.get_by_id(pk)
    if not detail:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = OrderDetailsSerializer(detail)
    return Response(serializer.data)

@api_view(['POST'])
def create_order_detail(request):
    serializer = OrderDetailsSerializer(data=request.data)
    if serializer.is_valid():
        detail = repository.create(**serializer.validated_data)
        return Response(OrderDetailsSerializer(detail).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_order_detail(request, pk):
    serializer = OrderDetailsSerializer(data=request.data)
    if serializer.is_valid():
        detail = repository.update(pk, **serializer.validated_data)
        if detail:
            return Response(OrderDetailsSerializer(detail).data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_order_detail(request, pk):
    success = repository.delete(pk)
    if success:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
