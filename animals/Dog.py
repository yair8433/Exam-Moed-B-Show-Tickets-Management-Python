from overrides import overrides
from animals.LandAnimal import LandAnimal

class Dog(LandAnimal):
    @overrides
    def eat(self):
        print('The dog eats a bone.')

    @overrides
    def sleep(self):
        print('The dog sleeps on the sofa.')

    @overrides
    def move_to(self):
        print('The dog runs to the door.')

    def chase_cars(self):
        print('The dog chases cars.')

    def drool(self):
        print('The dog drools.')
