from abc import abstractmethod
from animals.Animal import Animal

class WaterAnimal(Animal):
    @abstractmethod
    def swim_to(self):
        pass
