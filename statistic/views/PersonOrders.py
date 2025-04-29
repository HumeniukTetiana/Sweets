from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from django.db.models import Count
from sweets.models import Person


@api_view(['GET'])
def person_orders(request):
    persons = Person.objects.annotate(
        order_count=Count('fullorder')
    ).filter(order_count__gt=1).order_by('-order_count')

    df = pd.DataFrame(list(persons.values('id', 'first_name', 'last_name', 'order_count')))
    return Response(df.to_dict(orient='records'))