from overrides import overrides
from animals.WaterAnimal import WaterAnimal

class Whale(WaterAnimal):
    @overrides
    def eat(self):
        print('The whale eats krill.')

    @overrides
    def sleep(self):
        print('The whale sleeps near the surface.')

    @overrides
    def swim_to(self):
        print('The whale swims to the open sea.')

    def chase_sailboats(self):
        print('The whale chases sailboats.')
