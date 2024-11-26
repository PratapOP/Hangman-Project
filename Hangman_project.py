# PROJECT HANGMAN

import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | | THE GAME
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
      ''')
# word list
wordlist = ['umbrella', 'apple', 'orange', 'butterfly', 'mouse', 'wizard', 'keyboard', 'duck', 'tiger', 'firetruck']
random_word = random.choice(wordlist)

def meaning():
    # print word meaning
    print("The meaning of your word is:")
    if random_word == 'umbrella':
        print("Used to save people from getting wet.")
    elif random_word == 'apple':
        print("A red fruit.")
    elif random_word == 'orange':
        print("A color that also represents a fruit.")
    elif random_word == 'butterfly':
        print("A beautiful flying insect.")
    elif random_word == 'mouse':
        print("Cousins of hamsters who are homeless all the time.")
    elif random_word == 'wizard':
        print("A male magician.")
    elif random_word == 'keyboard':
        print("An important input device for your PC.")
    elif random_word == 'duck':
        print("Quack Quack.")
    elif random_word == 'tiger':
        print("A fearsome creature of the jungle.")
    elif random_word == 'firetruck':
        print("A red vehicle, always in a hurry.")

# initialize placeholders
placeholder = '_' * len(random_word)
print(placeholder)

neg_point = 0

def gamelogic():
    # draw hangman based on points
    if neg_point == 1:
        print('''  
        ________       
        |/     
        |      
        |      
        |      
        |
    ____|___''')
    if neg_point == 2:
        print('''
        _______
        |/    |
        |      
        |            
        |      
        |
    ____|___''')
    if neg_point == 3:
        print('''
        _______
        |/     |
        |     (_)
        |      
        |       
        |       
        |
    ____|___''')
    if neg_point == 4:
        print('''
        _______
        |/     |
        |     (_)
        |      |
        |      |
        |     
        |
    ____|___''')
    if neg_point == 5:
        print('''
        _______
        |/     |
        |     (_)
        |     \|/
        |      |
        |  
        |
    ____|___''')
    if neg_point == 6:
        print('''
        _______
        |/     |
        |     (_)
        |     \|/
        |      |
        |     //
        |
    ____|___''')
        print("--X-- YOU LOSE --X--")

# start game
choice = int(input("Do you want to play HANGMAN?\n1. Yes\n2. No\n"))
if choice == 1:
    while neg_point < 6 and '_' in placeholder:
        guess = input("Guess a letter or type 'meaning' to know the word's meaning: ").lower()

        if guess == 'meaning':
            meaning()
            neg_point += 2  # two points penalty for asking meaning
            gamelogic()

        elif guess in random_word:
            placeholder = ''.join([letter if letter == guess else placeholder[i] for i, letter in enumerate(random_word)])
        else:
            neg_point += 1
            gamelogic()

        print(placeholder)

    if '_' not in placeholder:
        print("-- Congratulations, you won! --")
