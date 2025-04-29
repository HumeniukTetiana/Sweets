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

    @property
    def person_name(self):
        return self.person.name

    @staticmethod
    def get_reviews_by_rating(product_id, min_rating):
        return Review.objects.filter(product_id=product_id, rating__gte=min_rating)

    @staticmethod
    def get_average_rating(product_id):
        result = Review.objects.filter(product_id=product_id).aggregate(avg_rating=Avg('rating'))
        avg_rating = result['avg_rating']
        if avg_rating is not None:
            return round(avg_rating, 2)
        return None