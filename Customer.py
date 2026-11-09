from CustomerType import CustomerType
from validations import check_id, check_text, check_email, check_customer_type, check_discount

class Customer:
    used_ids = []

    def __init__(self, customer_id, first_name, last_name, email, delivery_address, customer_type: CustomerType, discount=None):
        check_id(customer_id, Customer.used_ids, 'Customer')
        check_text(first_name, 'First name')
        check_text(last_name, 'Last name')
        check_email(email)
        check_text(delivery_address, 'Delivery address')
        check_customer_type(customer_type)
        check_discount(discount)
        self.__id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__delivery_address = delivery_address
        self.__customer_type = customer_type
        self.__discount = discount
        self.__voucher = None
        Customer.used_ids.append(customer_id)

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        check_text(first_name, 'First name')
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        check_text(last_name, 'Last name')
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        check_email(email)
        self.__email = email

    @property
    def delivery_address(self):
        return self.__delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        check_text(delivery_address, 'Delivery address')
        self.__delivery_address = delivery_address

    @property
    def customer_type(self):
        return self.__customer_type

    @customer_type.setter
    def customer_type(self, customer_type):
        check_customer_type(customer_type)
        self.__customer_type = customer_type

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        check_discount(discount)
        self.__discount = discount

    @property
    def voucher(self):
        return self.__voucher

    @voucher.setter
    def voucher(self, voucher):
        self.__voucher = voucher

    def get_full_name(self):
        return self.__first_name + ' ' + self.__last_name

    def get_voucher_name(self):
        voucher_name = None
        if self.__voucher is not None:
            voucher_name = self.__voucher.get_name()
        return voucher_name

    def eat_food(self):
        if self.__voucher is None:
            print(self.get_full_name(), 'has no food voucher.')
        else:
            self.__voucher.eat()
            self.__voucher = None

    def print_customer(self):
        print('customer', self.__id, ':', self.get_full_name(), '|', self.__email, '|', self.__delivery_address)
        print('type:', self.__customer_type.name, '| discount:', self.__discount, '| voucher:', self.get_voucher_name())
