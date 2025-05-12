from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.transform import cumsum
from math import pi
from django.shortcuts import render
import pandas as pd
import requests
from bokeh.resources import CDN

def dashboard_bokeh(request):
    min_spent = float(request.GET.get("min_spent", 0))
    params = request.GET.urlencode()

    url = f"http://localhost:8000/statistic/ingredients-products-dashboard/?{params}"
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    df = df.sort_values("product_count", ascending=True)
    source1 = ColumnDataSource(df)
    p1 = figure(y_range=list(df['ingredient_name']), height=400,
                title="Number of Products per Ingredient", toolbar_location=None)
    p1.hbar(y='ingredient_name', right='product_count', height=0.7, source=source1)

    url = f"http://localhost:8000/statistic/person-orders-dashboard/?{params}"
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    df["full_name"] = (df["first_name"] + " " + df["last_name"]).str.strip()
    source2 = ColumnDataSource(df)
    p2 = figure(x_range=list(df['full_name']), height=400, title="Number of Orders per Person")
    p2.vbar(x='full_name', top='order_count', width=0.9, source=source2)
    p2.xaxis.major_label_orientation = pi/4

    url = f"http://localhost:8000/statistic/person-total-spent-dashboard/?{params}"
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    df["total_spent"] = pd.to_numeric(df["total_spent"])
    df = df[df["total_spent"] >= min_spent].sort_values("total_spent", ascending=False)
    df["full_name"] = (df["first_name"] + " " + df["last_name"]).str.strip()
    source3 = ColumnDataSource(df)
    p3 = figure(x_range=list(df["full_name"]), height=400, title="Total Spending per Person (Filtered)")
    p3.line(x='full_name', y='total_spent', line_width=2, source=source3)
    p3.circle(x='full_name', y='total_spent', size=8, source=source3, color="green")
    p3.xaxis.major_label_orientation = pi/4

    url = f"http://localhost:8000/statistic/product-total-quantity-dashboard/?{params}"
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    source4 = ColumnDataSource(df)
    p4 = figure(x_range=list(df['product_name']), height=400, title="Total Quantity of Ordered Products")
    p4.circle(x='product_name', y='total_quantity_ordered', size=12, source=source4, color="navy", alpha=0.7)
    p4.xaxis.major_label_orientation = pi/4

    url = f"http://localhost:8000/statistic/product-average-rating-dashboard/?{params}"
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    df["avg_rating"] = pd.to_numeric(df["avg_rating"])
    df = df.sort_values(by="avg_rating", ascending=False)
    source5 = ColumnDataSource(df)
    p5 = figure(x_range=list(df['product_name']), height=400, title="Average Product Ratings (Filtered)")
    p5.step(x='product_name', y='avg_rating', mode="after", source=source5, line_width=2, color="orange")
    p5.xaxis.major_label_orientation = pi/4

    url = f"http://localhost:8000/statistic/sales-by-category-dashboard/?{params}"
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    df = df.sort_values("total_sales", ascending=False)
    df["angle"] = df["total_sales"] / df["total_sales"].sum() * 2 * pi
    palette = ["#f72585", "#7209b7", "#3a0ca3", "#4361ee", "#4cc9f0"]
    df["color"] = [palette[i % len(palette)] for i in range(len(df))]
    source6 = ColumnDataSource(df)
    p6 = figure(height=400, width=400, title="Sales by Category", toolbar_location=None,
                tools="hover", tooltips="@category_name: @total_sales")
    p6.wedge(x=0, y=0, radius=0.4, start_angle=cumsum('angle', include_zero=True),
             end_angle=cumsum('angle'), line_color="white", fill_color='color',
             legend_field='category_name', source=source6)
    p6.axis.visible = False
    p6.grid.visible = False

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
        "min_spent": min_spent,
        "bokeh_resources" : CDN.render(),
    })
