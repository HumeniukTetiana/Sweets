from django.db import models

class Person(models.Model): 
    first_name = models.CharField('імя', max_length=50)
    last_name = models.CharField('прізвище', max_length=50)
    phone = models.CharField('телефон', max_length=15, null=True, blank=True)
    email = models.EmailField('емеіл', max_length=100)

    def __str__(self):
        return self.first_name

