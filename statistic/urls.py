from django.urls import path
from statistic.views.IngredientsProducts import ingredients_products
from statistic.views.PersonOrders import person_orders
from statistic.views.PersonOrders import person_orders
from statistic.views.ProductsRating import product_average_rating
from statistic.views.ProductQuantity import product_total_quantity
from statistic.views.SalesByCategory import sales_by_category

urlpatterns = [
    path('products-quantity/', product_total_quantity()),
    path('persons-spent/', person_total_spent()),
    path('persons-orders/', person_orders()),
    path('ingredients-products/', ingredients_products()),
    path('products-rating/', product_average_rating_view),
    path('sales/by-category/', sales_by_category_view),
]

