from django.urls import path
from .views.ProductCreateView import product_create
from .views.ProductDetailsView import product_details
from .views.ProductListView import product_list
from .views.ProductUpdateView import product_update

urlpatterns = [
    path('', product_list, name='ProductList'),
    path('<int:pk>/', product_details, name='ProductDetails'),
    path('<int:pk>/edit/', product_update, name='ProductUpdate'),
    path('new/', product_create, name='ProductCreate'),
]
