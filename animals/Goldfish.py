from overrides import overrides
from animals.WaterAnimal import WaterAnimal

class Goldfish(WaterAnimal):
    @overrides
    def eat(self):
        print('The goldfish eats fish flakes.')

    @overrides
    def sleep(self):
        print('The goldfish sleeps at the bottom of the bowl.')

    @overrides
    def swim_to(self):
        print('The goldfish swims to the castle in the bowl.')

    def hide_from_cat(self):
        print('The goldfish hides from the cat.')
