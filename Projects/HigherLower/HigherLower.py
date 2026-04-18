import random
logo = r"""
    ______                        __  __                                  __             
  / ____/_  _____  __________   / /_/ /_  ___     ____  __  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / / / / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                    
"""

def comp_guess(guess,num):
    """This function compares the user guess with the number and if found returns true"""
    if guess==num:
        return True
    else:
        if guess>num:
            print("Your guess is too high, try lower.")
        elif guess<num:
            print("Your guess is too low, try higher.")
        return False


def play_game():
    attempts=5
    print(logo)
    print("Guess a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    randnum= random.randint(1,100)

    guess = input("Make a guess: ")
    guess = int(guess)
    while guess>100 or guess<0:
        print("Number must be between 1 and 100...")
        guess = input("Make a guess: ")
        guess = int(guess)
    found = comp_guess(guess, randnum)

    while not found and attempts>0:
        guess = input("Make a guess: ")
        guess= int(guess)
        found=comp_guess(guess,randnum)
        attempts-=1
    if found:
        print("Congratulations! You guessed the number correctly.")
    else:
        print(f"Sorry, you ran out of guesses. The number was {randnum}.")

play_game()

while input("Do you want to play a game?(y/n) ")=="y":
    print("\n" * 20)
    play_game()

