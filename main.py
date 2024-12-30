MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

# TODO 3: Print a report of all coffee machine resources
def resource_levels():
    """Return string with Water, milk, coffee, and money levels"""
    return (f"Water: {resources['water']}ml\n"
            f"Milk: {resources['milk']}ml\n"
            f"Coffee: {resources['coffee']}g\n"
            f"Money: ${round(resources['money'],2)}")

def reduce_resources(menu_item):
    """reduces the resource amount based on provided menu items ingredients"""
    return

# TODO 4: Check resources sufficient?
def is_menu_item(item_to_check):
    return item_to_check == "latte" or item_to_check == "cappuccino" or item_to_check == "espresso"

def input_cleanup(string_to_cleanup):
    """Corrects misspelling of menu items as long as the first char is correct"""
    corrected_input = string_to_cleanup
    if string_to_cleanup[0] == "o":
        corrected_input = "off"
    elif string_to_cleanup[0] == "r":
        corrected_input = "report"
    elif string_to_cleanup[0] == "e":
        corrected_input = "espresso"
    elif string_to_cleanup[0] == "l":
        corrected_input = "latte"
    elif string_to_cleanup[0] == "c":
        corrected_input = "cappuccino"
    return corrected_input

def check_resources_for_order(menu_item):
    """Check if the machine has the resources to fill the order"""
    adequate_resources = True
    required_water = menu_item["ingredients"]["water"]
    required_milk = menu_item["ingredients"]["milk"]
    required_coffee = menu_item["ingredients"]["coffee"]
    inadequate = "Not enough "
    if required_water > resources['water']:
        adequate_resources = False
        inadequate += "Water "
    if required_milk > resources['milk']:
        adequate_resources = False
        inadequate += "Milk "
    if required_coffee > resources['coffee']:
        adequate_resources = False
        inadequate += "Coffee "
    if not adequate_resources:
        print(inadequate + "to fill order.")
    return adequate_resources

def update_resources_after_sale(menu_item):
    resources["water"] -= menu_item["ingredients"]["water"]
    resources["milk"] -= menu_item["ingredients"]["milk"]
    resources["coffee"] -= menu_item["ingredients"]["coffee"]
    resources["money"] += menu_item["cost"]

# TODO 5: Process coins.
# TODO 6: Check transaction successful
def coin_processing(cost, given_quarters, given_dimes, given_nickels, given_pennies):
    value = (given_quarters * .25) + (given_dimes * .1) + (given_nickels * .05) + (given_pennies * .01)
    paid_enough = False
    if value >= cost:
        print(f"Here is your change: ${round(value - cost,2)}")
        paid_enough = True
    else:
        print("Sorry that was not enough to purchase that product. Refunding Money.")
    return paid_enough



def coffee_machine():
    on = True
    while on:
        selection = input_cleanup(input("What would you like? (espresso/latte/cappuccino): ").lower())
# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
        if selection == "off":
            on = False
        elif selection == "report":
            print(resource_levels())
        elif is_menu_item(selection):
            order = MENU[selection]
            if check_resources_for_order(order):
                if coin_processing(order["cost"],
                                int(input("How many quarters?: ")),
                                int(input("How many dimes?: ")),
                                int(input("How many nickels?: ")),
                                int(input("How many pennies?: "))):
                    print(f"Here is your {selection} ☕. Enjoy!")
                    update_resources_after_sale(order)
        else:
            print("please make a valid selection")

coffee_machine()
