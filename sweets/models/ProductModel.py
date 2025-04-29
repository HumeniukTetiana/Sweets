from django.db import models
from sweets.models.CategoryModel import Category

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(null=True)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    def display_price(self):
        print(f"Ціна: {self._price} грн")

    def price_with_discount(self, discount_percent):
        if 0 <= discount_percent <= 100:
            discount_amount = self.price * (discount_percent / 100)
            return self.price - discount_amount
        else:
            raise ValueError("Знижка має бути від 0 до 100.")

    def net_price(self):
        total_ingredient_price = 0.0

        for product_ingredient in self.productingredient_set.all():
            ingredient_price = product_ingredient.ingredient.price_per_kg
            total_ingredient_price += ingredient_price * (product_ingredient.quantity_in_grams / 1000)

        return total_ingredient_price