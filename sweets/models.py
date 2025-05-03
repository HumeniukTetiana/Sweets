from django.db import models
import math
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique= True)

    def __str__(self):
        return self.category_name


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

    def __str__(self):
        return f"Order {self.pk}"

    def get_total_price(self):
        total = 0.0
        for item in self.orderdetails_set.all():
            total += float(item.price) * item.quantity
        return float(math.ceil(total))


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100, unique=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ingredient_name


class Person(AbstractUser):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    _phone = models.CharField(db_column='phone', max_length=15, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    def __new__(cls, *args, **kwargs):
        instance = super(Person, cls).__new__(cls)
        return instance

    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def phone(self):
        if not self._phone:
            return "Номер телефону не вказано"
        else:
            return self._phone

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


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


class ProductIngredient(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantity_in_grams = models.PositiveIntegerField()

    class Meta:
        unique_together = ('product', 'ingredient')

    def __str__(self):
        return f"{self.ingredient} in {self.product}: {self.quantity_in_grams}g"

    def net_price(self):
        price_per_kg = self.ingredient.price_per_kg
        quantity_in_kg = self.quantity_in_grams / 1000
        return price_per_kg * quantity_in_kg


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


class OrderDetails(models.Model):
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    full_order = models.ForeignKey(FullOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order detail {self.pk}"


