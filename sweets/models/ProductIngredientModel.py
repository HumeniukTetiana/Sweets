from django.db import models
from sweets.models.PersonModel import Person
from sweets.models.IngredientModel import Ingredient

class ProductIngredient(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantity_in_grams = models.PositiveIntegerField()

    class Meta:
        unique_together = ('product', 'ingredient')

    def __str__(self):
        return f"{self.ingredient} in {self.product}: {self.quantity_in_grams}g"
