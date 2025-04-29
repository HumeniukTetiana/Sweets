from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from django.db.models import Sum
from sweets.models import Product

@api_view(['GET'])
def product_total_quantity(request):
    products = Product.objects.annotate(
        total_quantity_ordered=Sum('orderdetails__quantity')
    ).filter(total_quantity_ordered__gt=50).order_by('-total_quantity_ordered')

    df = pd.DataFrame(list(products.values('id', 'product_name', 'total_quantity_ordered')))
    return Response(df.to_dict(orient='records'))