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
    "money": 0,
}

quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

while True:
    user_Beverage = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_Beverage in MENU.keys():
        if (resources["water"]) >= MENU[user_Beverage].get("ingredients").get("water"):
            print("Please insert coins.")
            insert_Quarters = int(input("How many quarters? "))
            insert_Dimes = int(input("How many dimes? "))
            insert_Nickels = int(input("How many nickels? "))
            insert_Pennies = int(input("How many pennies? "))

            total = (insert_Quarters * quarter) + (insert_Dimes * dime) + (insert_Nickels * nickel) + \
                    (insert_Pennies * penny)

            if total >= MENU[user_Beverage].get("cost"):

                print(f"Here is ${total - MENU[user_Beverage].get('cost'):.2f} in change.")
                print(f"Here is your {user_Beverage} ☕. Enjoy!")

                resources["money"] += MENU[user_Beverage].get('cost')
                resources["water"] = resources.get("water") - MENU[user_Beverage].get("ingredients").get("water")
                resources["milk"] = resources.get("milk") - MENU[user_Beverage].get("ingredients").get("milk", 0)
                resources["coffee"] = resources.get("coffee") - MENU[user_Beverage].get("ingredients").get("coffee")

            else:
                print("Sorry that is not enough money. Money refunded.")
        else:
            print("Sorry there is not enough water.")
    elif user_Beverage == "report":
        measurement = "ml"

        for k, v in resources.items():
            k = k.capitalize()
            statement = f"{k}: {v}{measurement}"

            if k == "Coffee":
                measurement = "g"
            if k == "Money":
                statement = f"{k}: ${v}"
            print(statement)

    elif user_Beverage == "off":
        break


