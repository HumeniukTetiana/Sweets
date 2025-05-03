from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from django.db.models import Count, Sum, Avg
from sweets.models import Ingredient, Person, Product, Review, OrderDetails

@api_view(['GET'])
def ingredients_products(request):
    ingredients = Ingredient.objects.annotate(
        product_count=Count('productingredient__product', distinct=True)
    ).filter(product_count__gt=2).order_by('-product_count')

    df = pd.DataFrame(list(ingredients.values('id', 'ingredient_name', 'product_count')))
    return Response(df.to_dict(orient='records'))


@api_view(['GET'])
def person_orders(request):
    persons = Person.objects.annotate(
        order_count=Count('fullorder')
    ).filter(order_count__gt=1).order_by('-order_count')

    df = pd.DataFrame(list(persons.values('id', 'first_name', 'last_name', 'order_count')))
    return Response(df.to_dict(orient='records'))


@api_view(['GET'])
def person_total_spent(request):
    persons = Person.objects.annotate(
        total_spent=Sum('fullorder__total_amount')
    ).filter(total_spent__gt=500).order_by('-total_spent')

    df = pd.DataFrame(list(persons.values('id', 'first_name', 'last_name', 'total_spent')))
    return Response(df.to_dict(orient='records'))


@api_view(['GET'])
def product_total_quantity(request):
    products = Product.objects.annotate(
        total_quantity_ordered=Sum('orderdetails__quantity')
    ).filter(total_quantity_ordered__gt=50).order_by('-total_quantity_ordered')

    df = pd.DataFrame(list(products.values('id', 'product_name', 'total_quantity_ordered')))
    return Response(df)

#.to_dict(orient='records')


@api_view(['GET'])
def product_average_rating(request):
    ratings = Review.objects.values('product__product_name').annotate(
        avg_rating=Avg('rating')
    ).order_by('-avg_rating')

    df = pd.DataFrame(list(ratings))
    return Response(df.to_dict(orient='records'))


@api_view(['GET'])
def sales_by_category(request):
    sales = OrderDetails.objects.values('product__category__category_name').annotate(
        total_sales=Sum('price')
    ).order_by('-total_sales')

    df = pd.DataFrame(list(sales))
    return Response(df.to_dict(orient='records'))
