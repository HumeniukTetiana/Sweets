from django.urls import path
from .views import product_create, product_details, product_list, product_update

urlpatterns = [
    path('', product_list, name='ProductList'),
    path('<int:pk>/', product_details, name='ProductDetails'),
    path('<int:pk>/edit/', product_update, name='ProductUpdate'),
    path('new/', product_create, name='ProductCreate'),
]
