""" Coffee maker main"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


MACHINE_ON = True

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while MACHINE_ON:
    menu_items = menu.get_items()
    choice = input(f"What would you like? ({menu_items}): ")

    if choice == 'off':
        MACHINE_ON = False
    elif choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)