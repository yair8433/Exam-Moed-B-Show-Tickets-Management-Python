from abc import ABC, abstractmethod
from Customer import Customer
from validations import check_id, check_text, check_date, check_seat, check_amount

class Ticket(ABC):
    used_ids = []

    def __init__(self, ticket_id, show_name, show_date, row_number, sit_number, customer, price):
        check_id(ticket_id, Ticket.used_ids, 'Ticket')
        check_text(show_name, 'Show name')
        check_date(show_date)
        check_seat(row_number, 'Row number')
        check_seat(sit_number, 'Sit number')
        if not isinstance(customer, Customer):
            raise ValueError('Ticket customer must be a customer.')
        check_amount(price, 'Ticket price')
        self.__id = ticket_id
        self.__show_name = show_name
        self.__show_date = show_date
        self.__row_number = row_number
        self.__sit_number = sit_number
        self.__customer = customer
        self.__given_price = price
        self.__price = self.calculate_price()
        Ticket.used_ids.append(ticket_id)

    @property
    def id(self):
        return self.__id

    @property
    def show_name(self):
        return self.__show_name

    @property
    def show_date(self):
        return self.__show_date

    @property
    def row_number(self):
        return self.__row_number

    @property
    def sit_number(self):
        return self.__sit_number

    @property
    def customer(self):
        return self.__customer

    @property
    def given_price(self):
        return self.__given_price

    @property
    def price(self):
        return self.__price

    @abstractmethod
    def calculate_price(self):
        pass

    def calculate_discount(self):
        return self.__given_price - self.__price

    def print_ticket(self):
        print('ticket', self.__id, ':', self.__show_name, '|', self.__show_date, '|', self.__customer.get_full_name())
        print('row', self.__row_number, 'sit', self.__sit_number, '| price:', self.__given_price, '->', self.__price)
