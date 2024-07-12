MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            return False
    return True


def process_coins ():
    quaters = int(input("How many quaters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickels = int(input("How many nickels: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    total_coins = quaters + dimes + nickels + pennies
    return total_coins

def transaction_succesful (payment_recived, actual_cost):
    if payment_recived >= actual_cost:
        change = round(payment_recived) - actual_cost
        print(f"Here is your change ${change}.")
        global profit
        profit += actual_cost
        return True
    else:
        print("You don't have sufficient amount, money refunded.")
        return False


def make_coffee (drink_chosen, drink_ingredients):
    for items in drink_ingredients:
        resources[items] -= drink_ingredients[items]
    print(f"Here's your {drink_chosen}. Enjoy your drink.")


is_on = True


while is_on:
    user_choice = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(f"Water = {resources['water']} ml")
        print(f"Milk = {resources['milk']} ml")
        print(f"Coffee = {resources['coffee']} gm")
        print(f"Profit = ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if transaction_succesful (payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])




