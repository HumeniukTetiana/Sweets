from django.db import models
from sweets.models.PersonModel import Person

class PaymentStatus(models.TextChoices):
    YES = 'yes', 'Yes'
    NO = 'no', 'No'

class FullOrder(models.Model):
    person = models.ForeignKey('Person', blank=True, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    payment = models.CharField(
        max_length=3,
        choices=PaymentStatus.choices
    )
    total_amount = models.DecimalField(max_digits=8, decimal_places=1)
    points_used = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.pk}"
