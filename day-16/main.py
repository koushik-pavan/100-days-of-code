from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    choice = input("What drink would you like to have?")
    if choice == "off":
        is_on = False
    if choice == "report":
        maker.report()
    else:
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                maker.make_coffee(drink)








