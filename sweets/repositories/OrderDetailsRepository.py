from sweets.models.OrderDetailsModel import OrderDetails
from sweets.repositories.Repository import Repository  

class OrderDetailsRepository(Repository):
    
    def __init__(self):
        super().__init__(OrderDetails)
