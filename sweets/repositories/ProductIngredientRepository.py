from sweets.models.ProductIngredientModel import ProductIngredient
from sweets.repositories.Repository import Repository  

class ProductIngredientRepository(Repository):
    
    def __init__(self):
        super().__init__(ProductIngredient)
