from django.urls import path
from statistic.views import ingredients_products, person_orders, person_total_spent, product_average_rating, product_total_quantity, sales_by_category

urlpatterns = [
    path('products-quantity/', product_total_quantity),
    path('persons-spent/', person_total_spent),
    path('persons-orders/', person_orders),
    path('ingredients-products/', ingredients_products),
    path('products-rating/', product_average_rating),
    path('sales-by-category/', sales_by_category),
]

