from secrets import choice

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
Coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def checkResource(MENU,userChoice,resources):
    ingredients_needed = MENU[userChoice]["ingredients"]
    count=0
    for i in ingredients_needed:
        if resources[i] < ingredients_needed[i]:
            return False
        else:
            count+=1
            if count==len(ingredients_needed):
                return True
            
def report():
    for i in resources:
        print (i ,":",resources[i])

def checkMoney(MENU,userChoice,total):
    cost=MENU[userChoice]["cost"]   
    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        return True

def calcMoney(MENU,userChoice,total):
    cost=MENU[userChoice]["cost"]
    print("The cost of your coffee is: ",cost)
    quarter=int(input("How many quarters? "))
    dimes=int(input("How many dimes? "))
    nickels=int(input("How many nickels? "))
    pennies=int(input("How many pennies? "))
    total=quarter*Coins["quarters"]+dimes*Coins["dimes"]+nickels*Coins["nickels"]+pennies*Coins["pennies"]
    return total

def coffeemachine():
    total=0
    change=0
    flag=False
    userChoice=input("Select a coffee option (espresso/latte/cappuccino): ")
    if userChoice not in MENU:
        print("Invalid choice. Please select a valid coffee option.")
        
    else:
        if checkResource(MENU,userChoice,resources)==False:
            print("Sorry there are not enough resources contact staff for assistance.")
        else:
            if userChoice.lower()=="latte":
                total=calcMoney(MENU,userChoice,total)
                if checkMoney(MENU,userChoice,total)==True and checkResource(MENU,userChoice,resources)==True:
                    resources["water"]-=MENU["latte"]["ingredients"]["water"]
                    resources["milk"]-=MENU["latte"]["ingredients"]["milk"]
                    resources["coffee"]-=MENU["latte"]["ingredients"]["coffee"]
                    change=total-MENU["latte"]["cost"]
                    if change>0:
                        print("Your change is: ",round(change, 2))
                    print("Enjoy your latte!\n")
                    print("Current resources:")
                    report()
            elif userChoice.lower()=="espresso":
                total=calcMoney(MENU,userChoice,total)
                if checkMoney(MENU,userChoice,total)==True and checkResource(MENU,userChoice,resources)==True:
                    resources["water"]-=MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"]-=MENU["espresso"]["ingredients"]["coffee"]
                    change=total-MENU["espresso"]["cost"]
                    if change>0:
                        print("Your change is: ",round(change, 2))
                    print("Enjoy your espresso!\n")
                    print("Current resources:")
                    report()                    
            elif userChoice.lower()=="cappuccino":
                total=calcMoney(MENU,userChoice,total)
                if checkMoney(MENU,userChoice,total)==True and checkResource(MENU,userChoice,resources)==True:
                    resources["water"]-=MENU["cappuccino"]["ingredients"]["water"]
                    resources["milk"]-=MENU["cappuccino"]["ingredients"]["milk"]
                    resources["coffee"]-=MENU["cappuccino"]["ingredients"]["coffee"]
                    change=total-MENU["cappuccino"]["cost"]
                    if change>0:
                        print("Your change is: ",round(change, 2))
                    print("Enjoy your cappuccino!\n")
                    print("Current resources:")
                    report()    
    choice=(input("Do you want to continue? (yes/no) "))
    if choice.lower()=="yes":
        coffeemachine()
    else:
        print("Turning off coffee machine. Goodbye!")

#main
coffeemachine()
