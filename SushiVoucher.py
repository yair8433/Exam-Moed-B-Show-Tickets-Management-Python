from overrides import overrides
from FoodVoucher import FoodVoucher

class SushiVoucher(FoodVoucher):
    @overrides
    def eat(self):
        print('Here is your food, enjoy!')

    @overrides
    def get_name(self):
        return 'Sushi Voucher'
