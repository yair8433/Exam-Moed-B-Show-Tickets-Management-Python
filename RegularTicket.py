from overrides import overrides
from Ticket import Ticket

class RegularTicket(Ticket):
    @overrides
    def calculate_price(self):
        return self.given_price

    @overrides
    def print_ticket(self):
        super().print_ticket()
        print('type: regular')
