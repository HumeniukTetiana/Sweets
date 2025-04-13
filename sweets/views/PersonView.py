from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sweets.serializers.PersonSerializer import PersonSerializer
from sweets.repositories.PersonRepository import PersonRepository

repository = PersonRepository()

@api_view(['GET'])
def get_all_people(request):
    people = repository.get_all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_person_by_id(request, pk):
    person = repository.get_by_id(pk)
    if not person:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PersonSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])
def create_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        person = repository.create(**serializer.validated_data)
        return Response(PersonSerializer(person).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_person(request, pk):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        person = repository.update(pk, **serializer.validated_data)
        if person:
            return Response(PersonSerializer(person).data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_person(request, pk):
    success = repository.delete(pk)
    if success:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
