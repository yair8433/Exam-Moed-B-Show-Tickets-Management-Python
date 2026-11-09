from overrides import overrides
from FoodVoucher import FoodVoucher

class PizzaVoucher(FoodVoucher):
    @overrides
    def eat(self):
        print('Here is your food, enjoy!')

    @overrides
    def get_name(self):
        return 'Pizza Voucher'
