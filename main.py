MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

money = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

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

def resource_levels():
    """Return string with Water, milk, coffee, and money levels"""
    return (f"Water: {resources['water']}ml\n"
            f"Milk: {resources['milk']}ml\n"
            f"Coffee: {resources['coffee']}g\n"
            f"Money: ${round(money,2)}")

def is_menu_item(item_to_check):
    return item_to_check == "latte" or item_to_check == "cappuccino" or item_to_check == "espresso"

def check_resources_for_order(menu_item):
    """Check if the machine has the resources to fill the order"""
    adequate_resources = True
    for item in menu_item:
        if menu_item[item] >= resources[item]:
            print(f"Sorry there is not enough {item.upper()} to fill the order.")
            adequate_resources = False
    print("Refunding Money.")
    return adequate_resources

def make_coffee(name_of_drink, menu_item,):
    """Make the coffee, remove the used ingredients from resources"""
    for item in menu_item["ingredients"]:
        resources[item] -= menu_item["ingredients"][item]
    print(f"Here is your {name_of_drink} ☕. Enjoy!")

def coin_processing():
    """Calculate the value of given coins"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(paid, cost):
    """Return true if provided enough money for transaction"""
    global money
    paid_enough = False
    if paid >= cost:
        print(f"Here is your change: ${round(paid - cost, 2)}")
        money += cost
        paid_enough = True
    else:
        print("Sorry that was not enough to purchase that product. Refunding Money.")
    return paid_enough

def coffee_machine():
    on = True
    while on:
        selection = input_cleanup(input("What would you like? (espresso/latte/cappuccino): ").lower())
        if selection == "off":
            on = False
        elif selection == "report":
            print(resource_levels())
        elif is_menu_item(selection):
            order = MENU[selection]
            if check_resources_for_order(order["ingredients"]):
                money_given = coin_processing()
                if is_transaction_successful(money_given, order["cost"]):
                    make_coffee(selection, order)
        else:
            print("please make a valid selection")

coffee_machine()
