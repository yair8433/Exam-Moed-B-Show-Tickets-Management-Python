from Customer import Customer
from Ticket import Ticket
from validations import check_id, check_text, check_date

class Show:
    used_ids = []

    def __init__(self, show_id, show_name, show_date):
        check_id(show_id, Show.used_ids, 'Show')
        check_text(show_name, 'Show name')
        check_date(show_date)
        self.__id = show_id
        self.__name = show_name
        self.__date = show_date
        self.__tickets = []
        self.__food_vouchers = {}
        self.__given_vouchers = {}
        Show.used_ids.append(show_id)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def date(self):
        return self.__date

    @property
    def tickets(self):
        return self.__tickets

    @property
    def food_vouchers(self):
        return self.__food_vouchers

    def add_ticket(self, ticket):
        if not isinstance(ticket, Ticket):
            print('Only a ticket can be added to', self.__name)
        elif ticket in self.__tickets:
            print('Ticket', ticket.id, 'is already in', self.__name)
        else:
            self.__tickets.append(ticket)
            print('Ticket', ticket.id, 'was added to', self.__name)

    def remove_ticket(self, ticket):
        if ticket in self.__tickets:
            self.__tickets.remove(ticket)
            print('Ticket', ticket.id, 'was removed from', self.__name)
        else:
            print('This ticket is not in', self.__name)

    def calculate_revenue(self):
        total = 0
        for ticket in self.__tickets:
            total += ticket.price
        return total

    def calculate_total_discount(self):
        total = 0
        for ticket in self.__tickets:
            total += ticket.calculate_discount()
        return total

    def give_food_voucher(self, customer, food_voucher):
        if not isinstance(customer, Customer):
            print('A voucher can be given only to a customer.')
        elif getattr(food_voucher, 'eat', None) is None or getattr(food_voucher, 'get_name', None) is None:
            print('This is not a food voucher.')
        elif customer.id in self.__given_vouchers:
            print(customer.get_full_name(), 'already got a voucher for', self.__name)
        elif customer.voucher is not None:
            print(customer.get_full_name(), 'still has an unused voucher.')
        else:
            voucher_name = food_voucher.get_name()
            customer.voucher = food_voucher
            self.__food_vouchers[customer.id] = voucher_name
            self.__given_vouchers[customer.id] = food_voucher
            print(customer.get_full_name(), 'got a', voucher_name, 'for', self.__name)

    def take_food_voucher(self, customer):
        if not isinstance(customer, Customer):
            print('A voucher can be taken only from a customer.')
        elif customer.id not in self.__given_vouchers:
            print(customer.get_full_name(), 'did not get a voucher for', self.__name)
        elif customer.id not in self.__food_vouchers:
            print('The voucher of', customer.get_full_name(), 'was already taken back.')
        elif customer.voucher is not self.__given_vouchers[customer.id]:
            print(customer.get_full_name(), 'already used the voucher for', self.__name)
        else:
            customer.voucher = None
            del self.__food_vouchers[customer.id]
            print('The voucher of', customer.get_full_name(), 'was taken back.')

    def print_show(self):
        print('show', self.__id, ':', self.__name, '|', self.__date)
        for ticket in self.__tickets:
            ticket.print_ticket()
        print('revenue:', self.calculate_revenue())
        print('total discount:', self.calculate_total_discount())
        print('food vouchers:', self.__food_vouchers)
