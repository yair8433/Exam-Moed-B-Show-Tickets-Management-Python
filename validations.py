from CustomerType import CustomerType

def check_id(new_id, used_ids, label):
    if not isinstance(new_id, int) and not isinstance(new_id, str):
        raise ValueError(label + ' id must be a whole number or a text.')
    if new_id == '':
        raise ValueError(label + ' id can not be empty.')
    if new_id in used_ids:
        raise ValueError(label + ' id ' + str(new_id) + ' already exists.')

def check_text(text, label):
    if not isinstance(text, str):
        raise ValueError(label + ' must be a text.')
    if text.strip() == '':
        raise ValueError(label + ' can not be empty.')

def check_email(email):
    if not isinstance(email, str) or '@' not in email:
        raise ValueError('Email must contain @.')

def check_customer_type(customer_type):
    if not isinstance(customer_type, CustomerType):
        raise ValueError('Customer type must be REGULAR or VIP.')

def check_amount(amount, label):
    if not isinstance(amount, int) and not isinstance(amount, float):
        raise ValueError(label + ' must be a number.')
    if amount < 0:
        raise ValueError(label + ' can not be negative.')

def check_discount(discount):
    if discount is not None:
        if not isinstance(discount, int) and not isinstance(discount, float):
            raise ValueError('Customer discount must be a number.')
        if discount < 0 or discount > 1:
            raise ValueError('Customer discount must be between 0 and 1.')

def check_seat(seat, label):
    if not isinstance(seat, int):
        raise ValueError(label + ' must be a whole number.')
    if seat < 1:
        raise ValueError(label + ' must be from 1 and up.')

def check_date(show_date):
    if show_date is None or show_date == '':
        raise ValueError('Show date can not be empty.')
