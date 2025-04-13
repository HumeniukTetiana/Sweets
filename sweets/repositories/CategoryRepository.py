from sweets.models.CategoryModel import Category
from sweets.repositories.Repository import Repository  

class CategoryRepository(Repository):

    def __init__(self):
        super().__init__(Category)