from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from django.db.models import Count
from sweets.models import Ingredient

@api_view(['GET'])
def ingredients_products(request):
    ingredients = Ingredient.objects.annotate(
        product_count=Count('productingredient__product', distinct=True)
    ).filter(product_count__gt=2).order_by('-product_count')

    df = pd.DataFrame(list(ingredients.values('id', 'ingredient_name', 'product_count')))
    return Response(df.to_dict(orient='records'))