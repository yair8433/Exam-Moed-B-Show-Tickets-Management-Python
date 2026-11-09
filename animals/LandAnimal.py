from abc import abstractmethod
from animals.Animal import Animal

class LandAnimal(Animal):
    @abstractmethod
    def move_to(self):
        pass
