from django.db import models

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100, unique=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ingredient_name
