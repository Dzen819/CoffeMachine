from data import MENU
from data import resources

espresso_ingr = MENU["espresso"]
latte_ingr = MENU["latte"]
cappuccino_ingr = MENU["cappuccino"]
machine_water = resources["water"]
machine_milk = resources["milk"]
machine_coffee = resources["coffee"]


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino).
def ask():
    res_yes = False
    while not res_yes:
        coffee = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee == "espresso":
            need_resources = espresso_ingr
            res_yes = True
        elif coffee == "latte":
            need_resources = latte_ingr
            res_yes = True
        elif coffee == "cappuccino":
            need_resources = cappuccino_ingr
            res_yes = True
        elif coffee == "report":
            report()
        elif coffee == "off":
            off()
    return need_resources


# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
def off():
    sys.exit()


# TODO: 3. Print report.
def report():
        print(f"Water: {machine_water}")
        print(f"Coffee: {machine_coffee}")
        print(f"Milk: {machine_milk}")


# TODO: 4. Check resources sufficient?
def check_res(need_water, need_coffee, need_milk):
    if machine_milk >= need_milk and machine_water >= need_water and machine_coffee >= need_coffee:
        can_do_coffee = True
    else:
        if machine_milk < need_milk:
            print("Sorry there is not enough milk.")
        elif machine_water < need_water:
            print("Sorry there is not enough water.")
        elif machine_coffee < need_coffee:
            print("Sorry there is not enough coffee.")

        can_do_coffee = False
    return can_do_coffee


# TODO: 5. Process coins.
def process_coins():
    print("Please insert coins")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total_insert = quarters + dimes + nickles + pennies
    return total_insert


# TODO: 6. Check transaction successful?
def is_trans_succ(total_insert, need_cost):
    if total_insert >= need_cost:
        enough_money = True
        print(f"Here is ${total_insert - need_cost} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")
        enough_money = False
    return enough_money


# TODO: 7. Make Coffee.
def def_res():
    needed_resources = ask()
    need_water = needed_resources["ingredients"]["water"]
    need_coffee = needed_resources["ingredients"]["coffee"]
    need_milk = needed_resources["ingredients"]["milk"]
    need_cost = needed_resources["cost"]
    return [need_water, need_coffee, need_milk, need_cost]


def play():
    global machine_water
    global machine_milk
    global machine_coffee

    res = def_res()

    can_do = check_res(res[0], res[1], res[2], )

    if can_do:
        process_coin = process_coins()
        cook = is_trans_succ(process_coin, res[3])
        if cook:
            print("Here is your latte ☕️. Enjoy!")
            machine_water -= res[0]
            machine_coffee -= res[1]
            machine_milk -= res[2]
            report()
            play()
        else:
            play()
    else:
        play()


play()
