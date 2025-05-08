from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from django.db.models import Count, Sum, Avg
from sweets.models import Ingredient, Person, Product, Review, OrderDetails, FullOrder, Category

@api_view(['GET'])
def ingredients_products(request):
    ingredients = Ingredient.objects.annotate(
        product_count=Count('productingredient__product', distinct=True)
    ).filter(product_count__gt=2).order_by('-product_count')

    df = pd.DataFrame(list(ingredients.values('id', 'ingredient_name', 'product_count')))
    return Response(df)


@api_view(['GET'])
def person_orders(request):
    persons = Person.objects.annotate(
        order_count=Count('fullorder')
    ).filter(order_count__gt=1).order_by('-order_count')

    df = pd.DataFrame(list(persons.values('id', 'first_name', 'last_name', 'order_count')))
    return Response(df)


@api_view(['GET'])
def person_total_spent(request):
    persons = Person.objects.annotate(
        total_spent=Sum('fullorder__total_amount')
    ).filter(total_spent__gt=500).order_by('-total_spent')

    df = pd.DataFrame(list(persons.values('id', 'first_name', 'last_name', 'total_spent')))
    return Response(df)


@api_view(['GET'])
def product_total_quantity(request):
    products = Product.objects.annotate(
        total_quantity_ordered=Sum('orderdetails__quantity')
    ).filter(total_quantity_ordered__gt=50).order_by('-total_quantity_ordered')

    df = pd.DataFrame(list(products.values('id', 'product_name', 'total_quantity_ordered')))
    return Response(df)


@api_view(['GET'])
def product_average_rating(request):
    ratings = Review.objects.values('product__product_name').annotate(
        avg_rating=Avg('rating')
    ).order_by('-avg_rating')

    df = pd.DataFrame(list(ratings))
    return Response(df)


@api_view(['GET'])
def sales_by_category(request):
    sales = OrderDetails.objects.values('product__category__category_name').annotate(
        total_sales=Sum('price')
    ).order_by('-total_sales')

    df = pd.DataFrame(list(sales))
    return Response(df)



@api_view(['GET'])
def ingredients_products_dashboard(request):
    data = list(Ingredient.objects.values('id', 'ingredient_name'))
    df_ingredients = pd.DataFrame(data)

    data_links = list(Product.ingredients.through.objects.values('ingredient_id', 'product_id'))
    df_links = pd.DataFrame(data_links)

    grouped = df_links.groupby('ingredient_id').agg(product_count=('product_id', 'nunique')).reset_index()
    merged = df_ingredients.merge(grouped, left_on='id', right_on='ingredient_id')
    result = merged[merged['product_count'] > 2].sort_values('product_count', ascending=False)
    return Response(result.to_dict(orient='records'))


@api_view(['GET'])
def person_orders_dashboard(request):
    persons = pd.DataFrame(list(Person.objects.values('id', 'first_name', 'last_name')))
    orders = pd.DataFrame(list(FullOrder.objects.values('person_id')))

    order_counts = orders.groupby('person_id').size().reset_index(name='order_count')
    result = persons.merge(order_counts, left_on='id', right_on='person_id')
    result = result[result['order_count'] > 1].sort_values('order_count', ascending=False)
    return Response(result.to_dict(orient='records'))


@api_view(['GET'])
def person_total_spent_dashboard(request):
    persons = pd.DataFrame(list(Person.objects.values('id', 'first_name', 'last_name')))
    orders = pd.DataFrame(list(FullOrder.objects.values('person_id', 'total_amount')))

    total_spent = orders.groupby('person_id').agg(total_spent=('total_amount', 'sum')).reset_index()
    result = persons.merge(total_spent, left_on='id', right_on='person_id')
    result = result[result['total_spent'] > 500].sort_values('total_spent', ascending=False)
    return Response(result.to_dict(orient='records'))


@api_view(['GET'])
def product_total_quantity_dashboard(request):
    products = pd.DataFrame(list(Product.objects.values('id', 'product_name')))
    orderdetails = pd.DataFrame(list(OrderDetails.objects.values('product_id', 'quantity')))

    quantities = orderdetails.groupby('product_id').agg(total_quantity_ordered=('quantity', 'sum')).reset_index()
    result = products.merge(quantities, left_on='id', right_on='product_id')
    result = result[result['total_quantity_ordered'] > 50].sort_values('total_quantity_ordered', ascending=False)
    return Response(result.to_dict(orient='records'))


@api_view(['GET'])
def product_average_rating_dashboard(request):
    reviews = pd.DataFrame(list(Review.objects.values('product_id', 'rating')))
    products = pd.DataFrame(list(Product.objects.values('id', 'product_name')))

    avg_ratings = reviews.groupby('product_id').agg(avg_rating=('rating', 'mean')).reset_index()
    result = products.merge(avg_ratings, left_on='id', right_on='product_id')
    result = result.sort_values('avg_rating', ascending=False)
    return Response(result.to_dict(orient='records'))


@api_view(['GET'])
def sales_by_category_dashboard(request):
    details = pd.DataFrame(list(OrderDetails.objects.values('price', 'product_id')))
    products = pd.DataFrame(list(Product.objects.values('id', 'category_id')))
    categories = pd.DataFrame(list(Category.objects.values('id', 'category_name')))

    details = details.merge(products, left_on='product_id', right_on='id')
    sales = details.groupby('category_id').agg(total_sales=('price', 'sum')).reset_index()
    result = sales.merge(categories, left_on='category_id', right_on='id')
    result = result.sort_values('total_sales', ascending=False)
    return Response(result.to_dict(orient='records'))

