from sweets.models.ProductModel import Product
from sweets.repositories.Repository import Repository  

class ProductRepository(Repository):
    
    def __init__(self):
        super().__init__(Product)
