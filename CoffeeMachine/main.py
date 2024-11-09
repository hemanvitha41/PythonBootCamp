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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# Change Calculation
def calculate_change(type_of_coffee):
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))*0.25
    dimes = int(input("How many dimes?"))*0.10
    nickels = int(input("How many nickels?"))*0.05
    pennies = int(input("How many pennies?"))*0.01
    total = quarters + dimes + nickels + pennies
    cost = MENU[type_of_coffee]["cost"]
    if total >= cost:
        change = total - cost
        if change > 0:
            print(f"Your change is ${change:.2f}")
        return cost  # Return the cost to be added to the resources' money
    else:
        print("Not enough money! Money refunded.")
        return None  # Return None if insufficient funds

# Define Coffee function
def coffee_type(coffee):
    # Check if there are enough resources for the selected coffe
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        if resources.get(ingredient, 0) < amount:
            print(f"Sorry, not enough {ingredient}.")
            return
    # Calculate change and payment process
    money = calculate_change(coffee)
    if money is None:
        return  # Exit the function if the payment was insufficient
    # Deduct resources if payment was successful
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {coffee} ☕ Enjoy!")
    resources["money"] += money

# Define report function
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


machine_On = True
while machine_On:
    coffee = input("What would you like?(espresso/latte/cappuccino):").lower()

    if coffee in ["espresso", "latte", "cappuccino"]:
      coffee_type(coffee)
    elif coffee == "report":
       report()
    elif coffee == "quit":
        machine_On = False
    else:
        print("Invalid input! try again.")


