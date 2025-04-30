from django.core.exceptions import ObjectDoesNotExist
from sweets.models.CategoryModel import Category
from sweets.models.FullOrderModel import FullOrder
from sweets.models.ReviewModel import Review
from sweets.models.ProductModel import Product
from sweets.models.ProductIngredientModel import ProductIngredient
from sweets.models.PersonModel import Person
from sweets.models.OrderDetailsModel import OrderDetails
from sweets.models.IngredientModel import Ingredient

class Repository:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, instance_id):
        try:
            return self.model.objects.get(id=instance_id)
        except ObjectDoesNotExist:
            return None

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        instance.save()
        return instance

    def update(self, instance_id, **kwargs):
        instance = self.get_by_id(instance_id)
        if instance:
            for attr, value in kwargs.items():
                setattr(instance, attr, value)
            instance.save()
            return instance
        return None

    def delete(self, instance_id):
        instance = self.get_by_id(instance_id)
        if instance:
            instance.delete()
            return True
        return False


class CategoryRepository(Repository):

    def __init__(self):
        super().__init__(Category)


class FullOrderRepository(Repository):

    def __init__(self):
        super().__init__(FullOrder)


class IngredientRepository(Repository):

    def __init__(self):
        super().__init__(Ingredient)


class OrderDetailsRepository(Repository):

    def __init__(self):
        super().__init__(OrderDetails)


class PersonRepository(Repository):

    def __init__(self):
        super().__init__(Person)


class ProductIngredientRepository(Repository):

    def __init__(self):
        super().__init__(ProductIngredient)


class ProductRepository(Repository):

    def __init__(self):
        super().__init__(Product)


class ReviewRepository(Repository):

    def __init__(self):
        super().__init__(Review)
