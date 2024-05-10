import random

word_list = ["orange", "kiwi", "melon", "apple", "mango"]
word = random.choice(word_list)

def ask_for_input():
    global guess
    while True:
        guess = input("Guess a letter: ") 
        if guess.isalpha() and len(guess) ==1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character")
ask_for_input() 

def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word {word}")
    else:
        print(f"Sorry, {guess} is not in the word")
check_guess(guess)