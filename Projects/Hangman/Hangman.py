import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list #imported a word list from another file
lives = 6

logo=hangman_art.logo #imported logo and some art from another file
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
wrong_letters = []

while not game_over:
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    flag=False
    while not flag:
        if guess in correct_letters or guess in wrong_letters: # basically if your guess the same you get looped
            print("Cant give the same letter twice!")   # could be optimised with one list of previous guesses[]
            guess = input("Guess a letter: ").lower()
        else:
            flag = True

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        wrong_letters.append(guess)
        print("letter " + guess + " is not in the word, you lose a life")
        print(f"**************************** {lives}/6 LIVES LEFT ****************************")
        if lives == 0:
            game_over = True
            print("The correct word was " + chosen_word +"\n YOU LOSE!")
            print(f"*********************** YOU LOSE **********************")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    stages=hangman_art.stages
    print(stages[lives])
