import random

word_list = ["orange", "kiwi", "melon", "apple", "mango"]
print(word_list)

word = random.choice(word_list)
print(word)
guess = input("Enter a single letter: ")
if guess.isalpha() and len(guess) ==1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")