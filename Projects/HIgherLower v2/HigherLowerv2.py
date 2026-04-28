import random
import game_data
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def play_game():
    print(logo)
    optA=random.choice(game_data.data)
    optB=random.choice(game_data.data)
    while optB == optA:
        optB = random.choice(game_data.data)
    flag = False
    usrScore = 0
    while not flag:
        print(f"Compare A: {optA['name']}, a {optA['description']} from {optA['country']}")
        print(vs)
        print(f"Compare B: {optB['name']}, a {optB['description']} from {optB['country']}")
        usrChoice=input("Enter your choice A or B: ")
        flag=False
        if int(optA["follower_count"]) > int(optB["follower_count"]):
            if usrChoice=="A":
                usrScore+=1
                print(f"You are correct! Current score {usrScore}\n")
                optB=random.choice(game_data.data)
                while optB == optA:
                    optB = random.choice(game_data.data)

            else:
                print(f"Sorry, that's wrong. Final score: {usrScore}")
                flag=True
        elif int(optA["follower_count"]) < int(optB["follower_count"]):
            if usrChoice=="B":
                usrScore+=1
                print(f"You are correct! Current score {usrScore}\n")
                optA=optB
                optB=random.choice(game_data.data)
                while optB == optA:
                    optB = random.choice(game_data.data)
            else:
                print(f"Sorry, that's wrong. Final score: {usrScore}")
                flag=True
        else:
            print("They're the same, you tie")

play_game()
playChoice=input("Do you want to play again? (Y/N): ").upper()
while playChoice=="Y":
    play_game()
    playChoice = input("Do you want to play again? (Y/N): ")