from overrides import overrides
from animals.LandAnimal import LandAnimal

class Cat(LandAnimal):
    @overrides
    def eat(self):
        print('The cat eats tuna.')

    @overrides
    def sleep(self):
        print('The cat sleeps in the sun.')

    @overrides
    def move_to(self):
        print('The cat walks to the window.')

    def overthrow_humans(self):
        print('The cat plans to overthrow the humans.')

    def cough_up_furballs(self):
        print('The cat coughs up a furball.')
