from sweets.models.FullOrderModel import FullOrder
from sweets.repositories.Repository import Repository  

class FullOrderRepository(Repository):
    
    def __init__(self):
        super().__init__(FullOrder)
