# Yair Gurevich

from CustomerType import CustomerType
from Customer import Customer
from Ticket import Ticket
from RegularTicket import RegularTicket
from VipTicket import VipTicket
from Show import Show
from SushiVoucher import SushiVoucher
from PizzaVoucher import PizzaVoucher
from PopcornVoucher import PopcornVoucher
from animals.Animal import Animal
from animals.WaterAnimal import WaterAnimal
from animals.LandAnimal import LandAnimal
from animals.Goldfish import Goldfish
from animals.Whale import Whale
from animals.Hamster import Hamster
from animals.Dog import Dog
from animals.Cat import Cat

def main():
    # Customers
    yair = Customer(1, 'Yair', 'Gurevich', 'yair@gmail.com', 'Petah Tikva', CustomerType.VIP, 0.15)
    shelly = Customer(2, 'Shelly', 'Goldberg', 'shelly@gmail.com', 'New York', CustomerType.REGULAR)
    omar = Customer(3, 'Omar', 'Haddad', 'omar@gmail.com', 'Amman', CustomerType.VIP)
    bill = Customer(4, 'Bill', 'Gates', 'bill@gmail.com', 'Miami', CustomerType.VIP, 0.5)
    yair.print_customer()
    shelly.print_customer()
    omar.print_customer()
    bill.print_customer()

    print('address before:', shelly.delivery_address)
    shelly.delivery_address = 'Miami'
    print('address after:', shelly.delivery_address)

    try:
        Customer(1, 'Copy', 'Id', 'copy@gmail.com', 'Haifa', CustomerType.REGULAR)
    except ValueError as error:
        print(error)

    try:
        Customer(5, '', 'Name', 'empty@gmail.com', 'Haifa', CustomerType.REGULAR)
    except ValueError as error:
        print(error)

    try:
        Customer(5, 'Bad', 'Email', 'no email', 'Haifa', CustomerType.REGULAR)
    except ValueError as error:
        print(error)

    try:
        Customer(5, 'Bad', 'Type', 'bad@gmail.com', 'Haifa', 'VIP')
    except ValueError as error:
        print(error)

    try:
        Customer(5, 'Bad', 'Discount', 'bad@gmail.com', 'Haifa', CustomerType.VIP, 30)
    except ValueError as error:
        print(error)

    print('discount before:', bill.discount)
    bill.discount = 0.25
    print('discount after:', bill.discount)
    bill.discount = 0.5

    # Tickets
    regular_ticket = RegularTicket(1, 'Hamlet', '25/12/2026', 5, 10, shelly, 100)
    regular_ticket_of_vip = RegularTicket(2, 'Hamlet', '25/12/2026', 5, 11, yair, 100)
    vip_ticket = VipTicket(3, 'Hamlet', '25/12/2026', 1, 1, yair, 200)
    vip_ticket_no_discount = VipTicket(4, 'Hamlet', '25/12/2026', 1, 2, omar, 200)
    vip_ticket_half_price = VipTicket(5, 'Cats', '10/01/2027', 1, 1, bill, 150)
    regular_ticket.print_ticket()
    regular_ticket_of_vip.print_ticket()
    vip_ticket.print_ticket()
    vip_ticket_no_discount.print_ticket()
    vip_ticket_half_price.print_ticket()

    try:
        VipTicket(6, 'Hamlet', '25/12/2026', 1, 3, shelly, 200)
    except ValueError as error:
        print(error)

    try:
        RegularTicket(1, 'Hamlet', '25/12/2026', 1, 3, shelly, 200)
    except ValueError as error:
        print(error)

    try:
        VipTicket(1, 'Hamlet', '25/12/2026', 1, 3, yair, 200)
    except ValueError as error:
        print(error)

    try:
        RegularTicket(6, 'Hamlet', '25/12/2026', 1, 3, shelly, -50)
    except ValueError as error:
        print(error)

    try:
        Ticket(6, 'Hamlet', '25/12/2026', 1, 3, shelly, 50)
    except Exception as error:
        print(error)

    id_still_free_ticket = RegularTicket(6, 'Cats', '10/01/2027', 7, 7, shelly, 80)
    id_still_free_ticket.print_ticket()

    # Shows
    show = Show(1, 'Hamlet', '25/12/2026')
    print('before adding tickets')
    show.print_show()

    show.add_ticket(regular_ticket)
    show.add_ticket(regular_ticket_of_vip)
    show.add_ticket(vip_ticket)
    show.add_ticket(vip_ticket_no_discount)
    print('after adding tickets')
    show.print_show()

    show.add_ticket(vip_ticket)
    show.add_ticket('not a ticket')

    show.remove_ticket(vip_ticket)
    print('after removing a ticket')
    show.print_show()
    show.remove_ticket(vip_ticket)

    show.add_ticket(vip_ticket)
    print('after adding it back')
    show.print_show()

    try:
        Show(1, 'Copy Id', '10/01/2027')
    except ValueError as error:
        print(error)

    try:
        Show(2, '', '10/01/2027')
    except ValueError as error:
        print(error)

    # Food Vouchers
    sushi = SushiVoucher()
    print('voucher name:', sushi.get_name())

    print('before giving:', shelly.get_voucher_name(), '|', show.food_vouchers)
    show.give_food_voucher(shelly, sushi)
    print('after giving:', shelly.get_voucher_name(), '|', show.food_vouchers)
    show.give_food_voucher(shelly, PizzaVoucher())

    shelly.eat_food()
    print('after eating:', shelly.get_voucher_name(), '|', show.food_vouchers)
    shelly.eat_food()
    show.give_food_voucher(shelly, PizzaVoucher())
    show.take_food_voucher(shelly)

    print('before giving:', yair.get_voucher_name(), '|', show.food_vouchers)
    show.give_food_voucher(yair, PizzaVoucher())
    print('after giving:', yair.get_voucher_name(), '|', show.food_vouchers)
    show.take_food_voucher(yair)
    print('after taking back:', yair.get_voucher_name(), '|', show.food_vouchers)
    show.take_food_voucher(yair)
    show.give_food_voucher(yair, PizzaVoucher())

    show.take_food_voucher(omar)
    show.give_food_voucher(omar, 'free pizza')
    show.give_food_voucher('not a customer', PizzaVoucher())

    print('before giving:', omar.get_voucher_name(), '|', show.food_vouchers)
    show.give_food_voucher(omar, PopcornVoucher())
    print('after giving:', omar.get_voucher_name(), '|', show.food_vouchers)

    other_show = Show(2, 'Cats', '10/01/2027')
    other_show.give_food_voucher(omar, SushiVoucher())
    omar.eat_food()
    print('after eating:', omar.get_voucher_name(), '|', show.food_vouchers)
    other_show.give_food_voucher(omar, SushiVoucher())
    print('after giving:', omar.get_voucher_name(), '|', other_show.food_vouchers)
    show.take_food_voucher(omar)
    print('hamlet:', show.food_vouchers)
    print('cats:', other_show.food_vouchers)

def bonus():
    goldfish = Goldfish()
    whale = Whale()
    hamster = Hamster()
    dog = Dog()
    cat = Cat()

    for animal in [goldfish, whale, hamster, dog, cat]:
        animal.eat()
        animal.sleep()

    goldfish.swim_to()
    goldfish.hide_from_cat()
    whale.swim_to()
    whale.chase_sailboats()
    hamster.move_to()
    hamster.plan_escape()
    dog.move_to()
    dog.chase_cars()
    dog.drool()
    cat.move_to()
    cat.overthrow_humans()
    cat.cough_up_furballs()

    try:
        Animal()
    except Exception as error:
        print(error)

    try:
        WaterAnimal()
    except Exception as error:
        print(error)

    try:
        LandAnimal()
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()
    bonus()
