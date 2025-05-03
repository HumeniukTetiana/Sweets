"""
URL configuration for sweets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sweets.views import CategoryView, FullOrderView, IngredientView, OrderDetailsView, PersonView, ProductIngredientView, ProductView, ReviewView, IngredientListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('product/', include('products.urls')),
    path('ingredients/list/', IngredientListView.ingredient_list, name='ingredient_list'),
    path('statistic/', include('statistic.urls')),

    path('categories/', CategoryView.get_all_categories, name='get_all_categories'),
    path('categories/<int:pk>/', CategoryView.get_category_by_id, name='get_category_by_id'),
    path('categories/create/', CategoryView.create_category, name='create_category'),
    path('categories/update/<int:pk>/', CategoryView.update_category, name='update_category'),
    path('categories/delete/<int:pk>/', CategoryView.delete_category, name='delete_category'),

    path('orders/', FullOrderView.get_all_orders, name='get_all_orders'),
    path('orders/<int:pk>/', FullOrderView.get_order_by_id, name='get_order_by_id'),
    path('orders/create/', FullOrderView.create_order, name='create_order'),
    path('orders/update/<int:pk>/', FullOrderView.update_order, name='update_order'),
    path('orders/delete/<int:pk>/', FullOrderView.delete_order, name='delete_order'),

    path('ingredients/', IngredientView.get_all_ingredients, name='get_all_ingredients'),
    path('ingredients/<int:pk>/', IngredientView.get_ingredient_by_id, name='get_ingredient_by_id'),
    path('ingredients/create/', IngredientView.create_ingredient, name='create_ingredient'),
    path('ingredients/update/<int:pk>/', IngredientView.update_ingredient, name='update_ingredient'),
    path('ingredients/delete/<int:pk>/', IngredientView.delete_ingredient, name='delete_ingredient'),

    path('order-details/', OrderDetailsView.get_all_order_details, name='get_all_order_details'),
    path('order-details/<int:pk>/', OrderDetailsView.get_order_detail_by_id, name='get_order_detail_by_id'),
    path('order-details/create/', OrderDetailsView.create_order_detail, name='create_order_detail'),
    path('order-details/update/<int:pk>/', OrderDetailsView.update_order_detail, name='update_order_detail'),
    path('order-details/delete/<int:pk>/', OrderDetailsView.delete_order_detail, name='delete_order_detail'),

    path('customers/', PersonView.get_all_people, name='get_all_people'),
    path('customers/<int:pk>/', PersonView.get_person_by_id, name='get_person_by_id'),
    path('customers/create/', PersonView.create_person, name='create_person'),
    path('customers/update/<int:pk>/', PersonView.update_person, name='update_person'),
    path('customers/delete/<int:pk>/', PersonView.delete_person, name='delete_person'),

    path('product-ingredients/', ProductIngredientView.get_all_product_ingredients, name='get_all_product_ingredients'),
    path('product-ingredients/<int:pk>/', ProductIngredientView.get_product_ingredient_by_id, name='get_product_ingredient_by_id'),
    path('product-ingredients/create/', ProductIngredientView.create_product_ingredient, name='create_product_ingredient'),
    path('product-ingredients/update/<int:pk>/', ProductIngredientView.update_product_ingredient, name='update_product_ingredient'),
    path('product-ingredients/delete/<int:pk>/', ProductIngredientView.delete_product_ingredient, name='delete_product_ingredient'),

    path('products/', ProductView.get_all_products, name='get_all_products'),
    path('products/<int:pk>/', ProductView.get_product_by_id, name='get_product_by_id'),
    path('products/create/', ProductView.create_product, name='create_product'),
    path('products/update/<int:pk>/', ProductView.update_product, name='update_product'),
    path('products/delete/<int:pk>/', ProductView.delete_product, name='delete_product'),

    path('reviews/', ReviewView.get_all_reviews, name='get_all_reviews'),
    path('reviews/<int:pk>/', ReviewView.get_review_by_id, name='get_review_by_id'),
    path('reviews/create/', ReviewView.create_review, name='create_review'),
    path('reviews/update/<int:pk>/', ReviewView.update_review, name='update_review'),
    path('reviews/delete/<int:pk>/', ReviewView.delete_review, name='delete_review'),
]
