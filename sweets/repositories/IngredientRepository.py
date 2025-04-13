from sweets.models.IngredientModel import Ingredient
from sweets.repositories.Repository import Repository   

class IngredientRepository(Repository):
    
    def __init__(self):
        super().__init__(Ingredient)
