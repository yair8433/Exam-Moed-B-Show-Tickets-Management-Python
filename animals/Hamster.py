from overrides import overrides
from animals.LandAnimal import LandAnimal

class Hamster(LandAnimal):
    @overrides
    def eat(self):
        print('The hamster eats seeds.')

    @overrides
    def sleep(self):
        print('The hamster sleeps in the sawdust.')

    @overrides
    def move_to(self):
        print('The hamster runs to its wheel.')

    def plan_escape(self):
        print('The hamster plans its escape.')
