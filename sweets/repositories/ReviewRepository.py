from sweets.models.ReviewModel import Review
from sweets.repositories.Repository import Repository   

class ReviewRepository(Repository):
    
    def __init__(self):
        super().__init__(Review)
