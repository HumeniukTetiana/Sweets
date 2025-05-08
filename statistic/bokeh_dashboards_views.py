from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource, Select, Slider
from bokeh.layouts import column, row
from bokeh.resources import CDN
from django.shortcuts import render
import pandas as pd
import requests

# 1. Інгредієнти й продукти

def ingredients_products_dashboard_bokeh(request):
    response = requests.get('http://localhost:8000/statistic/ingredients-products-dashboard/')
    df = pd.DataFrame(response.json())

    df = df.sort_values("product_count", ascending=False)
    source = ColumnDataSource(df)

    p = figure(x_range=list(df['ingredient_name']), height=400, title="Кількість продуктів у яких використовується інгредієнт",
               toolbar_location=None, tools="")
    p.vbar(x='ingredient_name', top='product_count', width=0.9, source=source)
    p.xaxis.major_label_orientation = 1

    script, div = components(p)
    return render(request, "ingredients_products.html", {"script": script, "div": div})

# 2. Замовлення на особу

def person_orders_dashboard_bokeh(request):
    response = requests.get('http://localhost:8000/statistic/person-orders-dashboard/')
    df = pd.DataFrame(response.json())

    slider = Slider(start=1, end=int(df['order_count'].max()), value=2, step=1, title="Мінімальна кількість замовлень")
    filtered = df[df['order_count'] >= slider.value]
    source = ColumnDataSource(filtered)

    p = figure(x_range=list(filtered['first_name'] + " " + filtered['last_name']), height=400,
               title="Кількість замовлень на особу")
    p.vbar(x='first_name', top='order_count', width=0.9, source=source)

    script, div = components(column(slider, p))
    return render(request, "person_orders.html", {"script": script, "div": div})

# 3. Сума витрат на особу

def person_total_spent_dashboard_bokeh(request):
    response = requests.get('http://localhost:8000/statistic/person-total-spent-dashboard/')
    df = pd.DataFrame(response.json())

    df = df.sort_values("total_spent", ascending=False)
    source = ColumnDataSource(df)

    p = figure(x_range=list(df['first_name'] + " " + df['last_name']), height=400, title="Сума витрат на особу")
    p.vbar(x='first_name', top='total_spent', width=0.9, source=source)

    script, div = components(p)
    return render(request, "person_total_spent.html", {"script": script, "div": div})

# 4. Кількість замовленого товару

def product_total_quantity_dashboard_bokeh(request):
    response = requests.get('http://localhost:8000/statistic/product-total-quantity-dashboard/')
    df = pd.DataFrame(response.json())

    source = ColumnDataSource(df)
    p = figure(x_range=list(df['product_name']), height=400, title="Загальна кількість замовленого товару")
    p.vbar(x='product_name', top='total_quantity_ordered', width=0.9, source=source)

    p.xaxis.major_label_orientation = 1
    script, div = components(p)
    return render(request, "product_total_quantity.html", {"script": script, "div": div})

# 5. Середній рейтинг продуктів

def product_average_rating_dashboard_bokeh(request):
    response = requests.get('http://localhost:8000/statistic/product-average-rating-dashboard/')
    df = pd.DataFrame(response.json())

    df = df.sort_values("avg_rating", ascending=False)
    source = ColumnDataSource(df)

    p = figure(x_range=list(df['product_name']), height=400, title="Середній рейтинг продуктів")
    p.vbar(x='product_name', top='avg_rating', width=0.9, source=source)
    p.xaxis.major_label_orientation = 1

    script, div = components(p)
    return render(request, "product_average_rating.html", {"script": script, "div": div})

# 6. Продажі по категоріях

def sales_by_category_dashboard_bokeh(request):
    response = requests.get('http://localhost:8000/statistic/sales-by-category-dashboard/')
    df = pd.DataFrame(response.json())

    df = df.sort_values("total_sales", ascending=False)
    source = ColumnDataSource(df)

    p = figure(x_range=list(df['category_name']), height=400, title="Продажі по категоріях")
    p.vbar(x='category_name', top='total_sales', width=0.9, source=source)
    p.xaxis.major_label_orientation = 1

    script, div = components(p)
    return render(request, "sales_by_category.html", {"script": script, "div": div})
