from django.db import models
from sweets.models.PersonModel import Person
from sweets.models.ProductModel import Product

class Review(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

