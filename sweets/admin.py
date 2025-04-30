from django.contrib import admin
from .models import Person, Review, Category, FullOrder, Ingredient, OrderDetails, ProductIngredient, Product
from django.contrib.auth.admin import UserAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')  


@admin.register(FullOrder)
class FullOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'order_date', 'payment', 'total_amount')       


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient_name', 'price_per_kg')  


@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'price', 'full_order', 'product')  

     
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email')


@admin.register(ProductIngredient)
class ProductIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'ingredient', 'quantity_in_grams')  

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'product_description', 'category')  


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'product', 'rating', 'comment') 
