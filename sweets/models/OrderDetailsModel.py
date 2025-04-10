from django.db import models
from sweets.models.FullOrderModel import FullOrder
from sweets.models.ProductModel import Product

class OrderDetails(models.Model):
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    full_order = models.ForeignKey(FullOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order detail {self.pk}"
