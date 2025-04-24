from django.db import models
from sweets.models.CategoryModel import Category

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(null=True)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name