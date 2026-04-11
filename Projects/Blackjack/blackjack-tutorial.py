import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print("Welcome to my own BlackJack game")
answer=input("Do you want to play a game?(y/n) ")
def give_card():
    """This function gives a random card to the user"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """This function calculates the game score"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(playerScore,dealerScore):
    """This function compares the player score and dealer score"""
    if playerScore==dealerScore:
        return "Draw"
    elif dealerScore==0:
        return "Lose opponent BlackJack"
    elif playerScore==0:
        return "Win with a BlackJack!"
    elif playerScore>21:
        return "You went over, you lose!"
    elif dealerScore>21:
        return "Opponent went over, you win!"
    elif playerScore>dealerScore:
        return "You win!"
    else:
        return"You lose!"

#main
def play_game():
    dealer_card=[]
    player_card=[]
    dealerScore=-1
    playerScore=-1
    gameOver=False
    print(logo)
    for i in range(2):
        player_card.append(give_card())
        dealer_card.append(give_card())
    while not gameOver:
        playerScore=calculate_score(player_card)
        dealerScore=calculate_score(dealer_card)
        print(f"Your cards: {player_card}, current score: {playerScore}")
        print(f"Computer's first card {dealer_card[0]}")
        if playerScore==0 or dealerScore==0 or playerScore>21:
            gameOver=True
        else:
            get_card=input("Type 'deal' to deal a card, type 'stand' to stand:")
            get_card=get_card.lower()
            if get_card=="stand":
                player_card.append(give_card())
            else:
                gameOver=True
    while dealerScore!=0 and dealerScore<17:
        dealer_card.append(give_card())
        dealerScore=calculate_score(dealer_card)
    print(f"Your final hand: {player_card}, final score: {playerScore}")
    print(f"Computer's final hand {dealer_card} final score: {dealerScore}")
    print(compare(playerScore,dealerScore))

    while input("Do you want to play a game?(y/n) ")=="y":
        print("\n*20")
        play_game()