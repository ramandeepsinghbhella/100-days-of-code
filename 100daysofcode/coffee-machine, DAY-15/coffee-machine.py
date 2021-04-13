MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 30
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 90,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def update_espresso():
    resources["water"] -= 50
    resources["coffee"] -= 18


def update_latte():
    resources["water"] -= 200
    resources["coffee"] -= 24
    resources["milk"] -= 100


def update_cappuccino():
    resources["water"] -= 250
    resources["coffee"] -= 24
    resources["milk"] -= 100


want_coffee = True
while want_coffee:
    user_choice = input("What would you like? espresso/latte/cappuccino\n").lower()
    if user_choice == "report":
        for key in resources:
            print(f"{key}: {resources[key]}\n")
    elif user_choice == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 14:
            coins = int(input("Please insert coins: "))
            if coins == 30:
                print("Here is your espresso enjoy")
                update_espresso()
            elif coins < 30:
                print("Coins are not sufficient")
            elif coins > 30:
                print(f"Here is {coins - 30} in change.\n Here is your espresso enjoy.")
                update_espresso()
        else:
            print("You don't have enough ingredient")

    elif user_choice == "latte":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            coins = int(input("Please insert coins: "))
            if coins == 50:
                print("Here is your latte enjoy")
                update_latte()
            elif coins < 50:
                print("Coins are not sufficient")
            elif coins > 50:
                print(f"Here is {coins - 50} in change.\n Here is your latte enjoy.")
                update_latte()
        else:
            print("You don't have enough ingredient")


    elif user_choice == "cappuccino":
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            coins = int(input("Please insert coins: "))
            if coins == 90:
                print("Here is your cappuccino enjoy")
                update_cappuccino()
            elif coins < 90:
                print("Coins are not sufficient")
            elif coins > 90:
                print(f"Here is {coins - 90} in change.\n Here is your cappuccino enjoy.")
                update_cappuccino()
        else:
            print("You don't have enough ingredient")
