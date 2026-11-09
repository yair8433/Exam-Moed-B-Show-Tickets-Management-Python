from abc import ABC, abstractmethod

class FoodVoucher(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
