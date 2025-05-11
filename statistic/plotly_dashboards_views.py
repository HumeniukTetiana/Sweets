from django.shortcuts import render
import pandas as pd
import plotly.express as px
import requests


def dashboard_plotly(request):
    ingredient_min_count = int(request.GET.get("ingredient_min_count", 0))
    order_sort = request.GET.get("order_sort", "asc")
    spent_min = float(request.GET.get("spent_min", 0))
    quantity_min = int(request.GET.get("quantity_min", 0))
    rating_sort = request.GET.get("rating_sort", "desc")

    response = requests.get('http://localhost:8000/statistic/ingredients-products-dashboard/')
    df = pd.DataFrame(response.json())
    df = df[df["product_count"] >= ingredient_min_count]

    fig = px.scatter(df, x='product_count', y='ingredient_name',
                     title='Number of Products per Ingredient (Dot Plot)',
                     size='product_count', color='ingredient_name')
    fig.update_traces(marker=dict(symbol='circle'))
    fig.update_layout(yaxis=dict(categoryorder='total ascending'))
    graph1 = fig.to_html(full_html=False)

    response = requests.get('http://localhost:8000/statistic/person-orders-dashboard/')
    df = pd.DataFrame(response.json())
    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    df = df.sort_values("order_count", ascending=(order_sort == "asc"))

    fig = px.bar(df, x='full_name', y='order_count', title='Number of Orders per Person')
    fig.update_layout(xaxis_title='Person', yaxis_title='Number of Orders', xaxis_tickangle=-45)
    graph2 = fig.to_html(full_html=False)

    response = requests.get('http://localhost:8000/statistic/person-total-spent-dashboard/')
    df = pd.DataFrame(response.json())
    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    df = df[df['total_spent'] >= spent_min]

    fig = px.bar(df, x='full_name', y='total_spent', title='Total Spending per Person')
    fig.update_layout(xaxis_title='Person', yaxis_title='Spent, UAH', xaxis_tickangle=-45)
    graph3 = fig.to_html(full_html=False)

    response = requests.get('http://localhost:8000/statistic/product-total-quantity-dashboard/')
    df = pd.DataFrame(response.json())
    df = df[df['total_quantity_ordered'] >= quantity_min]

    fig = px.bar(df, y='product_name', x='total_quantity_ordered', orientation='h',
                 title='Number of Orders per Product')
    fig.update_layout(xaxis_title='Quantity', yaxis_title='Product', yaxis=dict(categoryorder='total ascending'))
    graph4 = fig.to_html(full_html=False)

    response = requests.get('http://localhost:8000/statistic/product-average-rating-dashboard/')
    df = pd.DataFrame(response.json())
    df = df.sort_values("avg_rating", ascending=(rating_sort == "asc"))

    fig = px.line(df, x='product_name', y='avg_rating', title='Average Product Rating', markers=True)
    fig.update_layout(xaxis_title='Product', yaxis_title='Average Rating', xaxis_tickangle=-45)
    graph5 = fig.to_html(full_html=False)

    response = requests.get('http://localhost:8000/statistic/sales-by-category-dashboard/')
    df = pd.DataFrame(response.json())

    fig = px.pie(df, values='total_sales', names='category_name', title='Sales by Category')
    graph6 = fig.to_html(full_html=False)

    return render(request, "dashboard_plotly.html", {
        "graph1": graph1,
        "graph2": graph2,
        "graph3": graph3,
        "graph4": graph4,
        "graph5": graph5,
        "graph6": graph6,
        "ingredient_min_count": ingredient_min_count,
        "order_sort": order_sort,
        "spent_min": spent_min,
        "quantity_min": quantity_min,
        "rating_sort": rating_sort,
    })
