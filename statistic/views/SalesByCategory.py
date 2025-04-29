from rest_framework.decorators import api_view
from rest_framework.response import Response
from sweets.models import Product, OrderDetails
from django.db.models import Sum
import pandas as pd

@api_view(['GET'])
def sales_by_category(request):
    sales = OrderDetails.objects.values('product__category__category_name').annotate(
        total_sales=Sum('price')
    ).order_by('-total_sales')

    df = pd.DataFrame(list(sales))
    return Response(df.to_dict(orient='records'))