from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    my_coffee_maker = CoffeeMaker()
    my_menu = Menu()

    my_money_machine = MoneyMachine()

    on = True
    while on:
        selection = input(f"What would you like? ({my_menu.get_items()}): ").lower()
        if selection == "off":
            on = False
        elif selection == "report":
            my_coffee_maker.report()
            my_money_machine.report()
        else:
            drink = my_menu.find_drink(selection)
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)

coffee_machine()