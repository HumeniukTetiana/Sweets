import pandas as pd
import plotly.express as px
import requests
from django.shortcuts import render

# 1. Ingredients Products Dashboard (Plotly)
def ingredients_products_dashboard_plotly(request):
    response = requests.get('http://localhost:8000/statistic/ingredients-products-dashboard/')
    df = pd.DataFrame(response.json())

    fig = px.bar(df, x='ingredient_name', y='product_count', title='Кількість продуктів на інгредієнт')
    fig.update_layout(xaxis_title='Інгредієнт', yaxis_title='Кількість продуктів', xaxis_tickangle=-45)

    graph = fig.to_html(full_html=False)
    return render(request, "ingredients_products.html", {"graph": graph})

# 2. Person Orders Dashboard (Plotly)
def person_orders_dashboard_plotly(request):
    response = requests.get('http://localhost:8000/statistic/person-orders-dashboard/')
    df = pd.DataFrame(response.json())

    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    fig = px.bar(df, x='full_name', y='order_count', title='Кількість замовлень по особах')
    fig.update_layout(xaxis_title='Особа', yaxis_title='Кількість замовлень', xaxis_tickangle=-45)

    graph = fig.to_html(full_html=False)
    return render(request, "person_orders.html", {"graph": graph})

# 3. Person Total Spent Dashboard (Plotly)
def person_total_spent_dashboard_plotly(request):
    response = requests.get('http://localhost:8000/statistic/person-total-spent-dashboard/')
    df = pd.DataFrame(response.json())

    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    fig = px.bar(df, x='full_name', y='total_spent', title='Загальні витрати по особах')
    fig.update_layout(xaxis_title='Особа', yaxis_title='Витрачено, грн', xaxis_tickangle=-45)

    graph = fig.to_html(full_html=False)
    return render(request, "person_total_spent.html", {"graph": graph})

# 4. Product Total Quantity Dashboard (Plotly)
def product_total_quantity_dashboard_plotly(request):
    response = requests.get('http://localhost:8000/statistic/product-total-quantity-dashboard/')
    df = pd.DataFrame(response.json())

    fig = px.bar(df, x='product_name', y='total_quantity_ordered', title='Загальна кількість замовлень по продуктах')
    fig.update_layout(xaxis_title='Продукт', yaxis_title='Кількість', xaxis_tickangle=-45)

    graph = fig.to_html(full_html=False)
    return render(request, "product_total_quantity.html", {"graph": graph})

# 5. Product Average Rating Dashboard (Plotly)
def product_average_rating_dashboard_plotly(request):
    response = requests.get('http://localhost:8000/statistic/product-average-rating-dashboard/')
    df = pd.DataFrame(response.json())

    fig = px.bar(df, x='product_name', y='avg_rating', title='Середній рейтинг продуктів')
    fig.update_layout(xaxis_title='Продукт', yaxis_title='Середній рейтинг', xaxis_tickangle=-45)

    graph = fig.to_html(full_html=False)
    return render(request, "product_average_rating.html", {"graph": graph})

# 6. Sales by Category Dashboard (Plotly)
def sales_by_category_dashboard_plotly(request):
    response = requests.get('http://localhost:8000/statistic/sales-by-category-dashboard/')
    df = pd.DataFrame(response.json())

    fig = px.pie(df, values='total_sales', names='category_name', title='Продажі по категоріях')
    graph = fig.to_html(full_html=False)

    return render(request, "sales_by_category.html", {"graph": graph})
