from overrides import overrides
from CustomerType import CustomerType
from Ticket import Ticket

class VipTicket(Ticket):
    @overrides
    def calculate_price(self):
        if self.customer.customer_type != CustomerType.VIP:
            raise ValueError(self.customer.get_full_name() + ' is not a VIP customer.')
        discount = self.customer.discount
        if discount is None:
            discount = 0
        final_price = self.given_price - self.given_price * discount
        return final_price

    @overrides
    def print_ticket(self):
        super().print_ticket()
        print('type: VIP')
