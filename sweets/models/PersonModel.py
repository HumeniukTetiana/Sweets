from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser): 
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


