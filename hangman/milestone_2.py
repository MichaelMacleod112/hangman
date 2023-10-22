from random import choice as random_word_choice
import string


word_list = ["Apple", "Banana", "Orange", "Mango", "Pear"]

word = random_word_choice(word_list)


print("Please make a single letter guess")
while True:
    guess = input()
    if guess in string.ascii_letters:
        "Good guess!"
        break
    else:
        "Oops! That is not a valid input."

print(guess)
#test