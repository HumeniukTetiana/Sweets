from django.db import models
from django.contrib.auth.models import AbstractUser

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



