from sweets.models.PersonModel import Person
from sweets.repositories.Repository import Repository  

class PersonRepository(Repository):
    
    def __init__(self):
        super().__init__(Person)
