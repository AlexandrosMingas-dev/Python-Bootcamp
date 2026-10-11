from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
is_on=True

while is_on:
    options=menu.get_items()
    user_choice=input(f"What would you like? ({options}): ")
    if user_choice.lower()=="off":
        is_on=False
    elif user_choice.lower()=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                print(f"Here is your {drink.name} ☕️. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Sorry, there are not enough resources to make that drink.")