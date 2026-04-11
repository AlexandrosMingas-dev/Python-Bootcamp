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
def give_card(cardList,times):
    for i in range(0,times):
        cardList.append(random.choice(cards))
    return cardList


while answer=="Y" or answer=="y":
    k=0
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_cards=[]
    player_cards=[]
    playerScore=0
    dealerScore=0
    inGame=True
    print("\n" * 20)
    print(logo)
    give_card(dealer_cards,2)
    dealerScore+=sum(dealer_cards)
    give_card(player_cards,2)
    playerScore+=sum(player_cards)
    if playerScore==21:
        print("BLACKJACK!")
    elif dealerScore==21:
        print("Dealer BLACKJACK you lose!")
        inGame=False
        answer = input("Do you want to play a game?(y/n) ")
    if inGame:
        print(f"Your cards: {player_cards}, current score: {playerScore}")
        print(f"Computer's first card {dealer_cards[0]}")
        flag=False
        while not flag:
            get_card=input("Type 'deal' to deal a card, type 'stand' to stand:")
            while get_card=="deal":
                getcard=get_card.lower()
                if getcard == "deal":
                    player_cards.append(random.choice(cards))
                    if sum(player_cards) > 21 and 11 in player_cards:
                        player_cards.remove(11) # Take out the 11
                        player_cards.append(1)  # Put a 1 back in
                    playerScore = sum(player_cards)
                    if playerScore>21:
                        inGame=False
                        print(f"Your cards: {player_cards}, current score: {playerScore}")
                        print(f"Computer's final hand {dealer_cards} final score: {dealerScore}")
                        print("You lose!")
                        answer = input("Do you want to play a game?(y/n) ")
                        break
                    elif playerScore<=21:
                        print(f"Your cards: {player_cards}, current score: {playerScore}")
                        get_card = input("Type 'deal' to deal a card, type 'stand' to stand:")
            if get_card == "stand":
                if dealerScore>=17 and dealerScore<=21:
                    print(f"Computer's final hand {dealer_cards} final score: {dealerScore}")
                    if playerScore>dealerScore :
                        print("You win!")
                        answer = input("Do you want to play a game?(y/n) ")
                    elif playerScore==dealerScore:
                        print("Draw, Push!")
                        answer = input("Do you want to play a game?(y/n) ")
                    else:
                        print("You lose!")
                        answer = input("Do you want to play a game?(y/n) ")
                else:
                    while dealerScore<17:
                        dealer_cards.append(random.choice(cards))
                        dealerScore=sum(dealer_cards)
                    if dealerScore>21:
                        print(f"Computer's final hand {dealer_cards} final score: {dealerScore}")
                        print("You win!")
                        answer = input("Do you want to play a game?(y/n) ")
                    else:
                        print(f"Computer's final hand {dealer_cards} final score: {dealerScore}")
                        if playerScore>dealerScore:
                            print("You win!")
                            answer = input("Do you want to play a game?(y/n) ")
                        elif playerScore == dealerScore:
                            print("Draw, Push!")
                            answer = input("Do you want to play a game?(y/n) ")
                        else:
                            print("You lose!")
                            answer = input("Do you want to play a game?(y/n) ")
            elif answer!="deal":
                print("Wrong input!")
                flag=True
