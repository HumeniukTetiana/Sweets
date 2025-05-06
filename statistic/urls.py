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

urlpatterns = [
    path('products-quantity/', product_total_quantity),
    path('persons-spent/', person_total_spent),
    path('persons-orders/', person_orders),
    path('ingredients-products/', ingredients_products),
    path('products-rating/', product_average_rating),
    path('sales-by-category/', sales_by_category),

    path('api/ingredients-products-dashboard/', ingredients_products_dashboard),
    path('api/person-orders-dashboard/', person_orders_dashboard),
    path('api/person-total-spent-dashboard/', person_total_spent_dashboard),
    path('api/product-total-quantity-dashboard/', product_total_quantity_dashboard),
    path('api/product-average-rating-dashboard/', product_average_rating_dashboard),
    path('api/sales-by-category-dashboard/', sales_by_category_dashboard),
]


