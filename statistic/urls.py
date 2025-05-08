from django.urls import path
from statistic.views import (
    ingredients_products,
    person_orders,
    person_total_spent,
    product_average_rating,
    product_total_quantity,
    sales_by_category
)

from .views import (
    ingredients_products_dashboard,
    person_orders_dashboard,
    person_total_spent_dashboard,
    product_total_quantity_dashboard,
    product_average_rating_dashboard,
    sales_by_category_dashboard,
)

from .bokeh_dashboards_views import (
    ingredients_products_dashboard_bokeh,
    product_total_quantity_dashboard_bokeh,
    sales_by_category_dashboard_bokeh,
    product_average_rating_dashboard_bokeh,
    person_orders_dashboard_bokeh,
    person_total_spent_dashboard_bokeh,
)

from .plotly_dashboards_views import (
    person_orders_dashboard_plotly,
    product_average_rating_dashboard_plotly,
    product_total_quantity_dashboard_plotly,
    person_total_spent_dashboard_plotly,
    ingredients_products_dashboard_plotly,
    sales_by_category_dashboard_plotly,
)


urlpatterns = [
    path('products-quantity/', product_total_quantity),
    path('persons-spent/', person_total_spent),
    path('persons-orders/', person_orders),
    path('ingredients-products/', ingredients_products),
    path('products-rating/', product_average_rating),
    path('sales-by-category/', sales_by_category),

    path('ingredients-products-dashboard/', ingredients_products_dashboard),
    path('person-orders-dashboard/', person_orders_dashboard),
    path('person-total-spent-dashboard/', person_total_spent_dashboard),
    path('product-total-quantity-dashboard/', product_total_quantity_dashboard),
    path('product-average-rating-dashboard/', product_average_rating_dashboard),
    path('sales-by-category-dashboard/', sales_by_category_dashboard),

    path('ingredients-products-dashboard-plotly/', ingredients_products_dashboard_plotly,
         name='ingredients_products_dashboard_plotly'),
    path('person-orders-dashboard-plotly/', person_orders_dashboard_plotly,
         name='person_orders_dashboard_plotly'),
    path('person-total-spent-dashboard-plotly/', person_total_spent_dashboard_plotly,
         name='person_total_spent_dashboard_plotly'),
    path('product-total-quantity-dashboard-plotly/', product_total_quantity_dashboard_plotly,
         name='product_total_quantity_dashboard_plotly'),
    path('product-average-rating-dashboard-plotly/', product_average_rating_dashboard_plotly,
         name='product_average_rating_dashboard_plotly'),
    path('sales-by-category-dashboard-plotly/', sales_by_category_dashboard_plotly,
         name='sales_by_category_dashboard_plotly'),

    path('ingredients-products-dashboard-bokeh/', ingredients_products_dashboard_bokeh,
         name='ingredients_products_dashboard_bokeh'),
    path('person-orders-dashboard-bokeh/', person_orders_dashboard_bokeh,
         name='person_orders_dashboard_bokeh'),
    path('person-total-spent-dashboard-bokeh/', person_total_spent_dashboard_bokeh,
         name='person_total_spent_dashboard_bokeh'),
    path('product-total-quantity-dashboard-bokeh/', product_total_quantity_dashboard_bokeh,
         name='product_total_quantity_dashboard_bokeh'),
    path('product-avg-rating-dashboard-bokeh/', product_average_rating_dashboard_bokeh,
         name='product_avg_rating_dashboard_bokeh'),
    path('sales-by-category-dashboard-bokeh/', sales_by_category_dashboard_bokeh,
         name='sales_by_category_dashboard_bokeh'),
]


