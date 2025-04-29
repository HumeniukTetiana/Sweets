from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from django.db.models import  Sum
from sweets.models import Person

@api_view(['GET'])
def person_total_spent(request):
    persons = Person.objects.annotate(
        total_spent=Sum('fullorder__total_amount')
    ).filter(total_spent__gt=500).order_by('-total_spent')

    df = pd.DataFrame(list(persons.values('id', 'first_name', 'last_name', 'total_spent')))
    return Response(df.to_dict(orient='records'))