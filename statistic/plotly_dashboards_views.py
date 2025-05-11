import pandas as pd
import plotly.express as px
import requests
from django.shortcuts import render


def dashboard_plotly(request):

    response = requests.get('http://localhost:8000/statistic/ingredients-products-dashboard/')
    df = pd.DataFrame(response.json())

    fig = px.bar(df, x='ingredient_name', y='product_count', title='Кількість продуктів на інгредієнт')
    fig.update_layout(xaxis_title='Інгредієнт', yaxis_title='Кількість продуктів', xaxis_tickangle=-45)

    graph1 = fig.to_html(full_html=False)


    response = requests.get('http://localhost:8000/statistic/person-orders-dashboard/')
    df = pd.DataFrame(response.json())

    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    fig = px.bar(df, x='full_name', y='order_count', title='Кількість замовлень по особах')
    fig.update_layout(xaxis_title='Особа', yaxis_title='Кількість замовлень', xaxis_tickangle=-45)

    graph2 = fig.to_html(full_html=False)


    response = requests.get('http://localhost:8000/statistic/person-total-spent-dashboard/')
    df = pd.DataFrame(response.json())

    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    fig = px.bar(df, x='full_name', y='total_spent', title='Загальні витрати по особах')
    fig.update_layout(xaxis_title='Особа', yaxis_title='Витрачено, грн', xaxis_tickangle=-45)

    graph3 = fig.to_html(full_html=False)


    response = requests.get('http://localhost:8000/statistic/product-total-quantity-dashboard/')
    df = pd.DataFrame(response.json())

    fig = px.bar(df, x='product_name', y='total_quantity_ordered', title='Загальна кількість замовлень по продуктах')
    fig.update_layout(xaxis_title='Продукт', yaxis_title='Кількість', xaxis_tickangle=-45)

    graph4 = fig.to_html(full_html=False)


    response = requests.get('http://localhost:8000/statistic/product-average-rating-dashboard/')
    df = pd.DataFrame(response.json())

    fig = px.bar(df, x='product_name', y='avg_rating', title='Середній рейтинг продуктів')
    fig.update_layout(xaxis_title='Продукт', yaxis_title='Середній рейтинг', xaxis_tickangle=-45)

    graph5 = fig.to_html(full_html=False)


    response = requests.get('http://localhost:8000/statistic/sales-by-category-dashboard/')
    df = pd.DataFrame(response.json())

    fig = px.pie(df, values='total_sales', names='category_name', title='Продажі по категоріях')
    graph6 = fig.to_html(full_html=False)

    return render(request, "dashboard_plotly.html", {
        "graph1": graph1,
        "graph2": graph2,
        "graph3": graph3,
        "graph4": graph4,
        "graph5": graph5,
        "graph6": graph6,
    })
