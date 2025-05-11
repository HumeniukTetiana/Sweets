from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from django.shortcuts import render
import pandas as pd
import requests

def dashboard_bokeh(request):

    response = requests.get('http://localhost:8000/statistic/ingredients-products-dashboard/')
    df = pd.DataFrame(response.json())
    df = df.sort_values("product_count", ascending=False)
    source1 = ColumnDataSource(df)
    p1 = figure(x_range=list(df['ingredient_name']), height=400, title="Кількість продуктів у яких використовується інгредієнт",
               toolbar_location=None, tools="")
    p1.vbar(x='ingredient_name', top='product_count', width=0.9, source=source1)
    p1.xaxis.major_label_orientation = 1


    response = requests.get('http://localhost:8000/statistic/person-orders-dashboard/')
    df = pd.DataFrame(response.json())
    df["full_name"] = (df["first_name"] + " " + df["last_name"]).str.strip()
    source2 = ColumnDataSource(df)
    p2 = figure(x_range=list(df['full_name']), height=400, title="Кількість замовлень на особу")
    p2.vbar(x='full_name', top='order_count', width=0.9, source=source2)


    response = requests.get('http://localhost:8000/statistic/person-total-spent-dashboard/')
    df = pd.DataFrame(response.json())
    df = df.sort_values("total_spent", ascending=False)
    df["full_name"] = (df["first_name"] + " " + df["last_name"]).str.strip()
    source3 = ColumnDataSource(df)
    p3 = figure(x_range=list(df['full_name']), height=400, title="Сума витрат на особу")
    p3.vbar(x='full_name', top='total_spent', width=0.9, source=source3)


    response = requests.get('http://localhost:8000/statistic/product-total-quantity-dashboard/')
    df = pd.DataFrame(response.json())
    source4 = ColumnDataSource(df)
    p4 = figure(x_range=list(df['product_name']), height=400, title="Загальна кількість замовленого товару")
    p4.vbar(x='product_name', top='total_quantity_ordered', width=0.9, source=source4)
    p4.xaxis.major_label_orientation = 1


    response = requests.get('http://localhost:8000/statistic/product-average-rating-dashboard/')
    df = pd.DataFrame(response.json())
    df = df.sort_values("avg_rating", ascending=False)
    source5 = ColumnDataSource(df)
    p5 = figure(x_range=list(df['product_name']), height=400, title="Середній рейтинг продуктів")
    p5.vbar(x='product_name', top='avg_rating', width=0.9, source=source5)
    p5.xaxis.major_label_orientation = 1


    response = requests.get('http://localhost:8000/statistic/sales-by-category-dashboard/')
    df = pd.DataFrame(response.json())
    df = df.sort_values("total_sales", ascending=False)
    source6 = ColumnDataSource(df)
    p6 = figure(x_range=list(df['category_name']), height=400, title="Продажі по категоріях")
    p6.vbar(x='category_name', top='total_sales', width=0.9, source=source6)
    p6.xaxis.major_label_orientation = 1

    script1, div1 = components(p1)
    script2, div2 = components(p2)
    script3, div3 = components(p3)
    script4, div4 = components(p4)
    script5, div5 = components(p5)
    script6, div6 = components(p6)

    return render(request, "dashboard_bokeh.html", {
        "script1": script1, "div1": div1,
        "script2": script2, "div2": div2,
        "script3": script3, "div3": div3,
        "script4": script4, "div4": div4,
        "script5": script5, "div5": div5,
        "script6": script6, "div6": div6,
    })
