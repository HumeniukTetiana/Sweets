from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from django.db.models import Avg
from sweets.models import Review

@api_view(['GET'])
def product_average_rating(request):
    ratings = Review.objects.values('product__product_name').annotate(
        avg_rating=Avg('rating')
    ).order_by('-avg_rating')

    df = pd.DataFrame(list(ratings))
    return Response(df.to_dict(orient='records'))
















