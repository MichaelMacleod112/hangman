
from random import choice as random_word_choice
# import string  ### used for string.ascii_letters, deprecated

def ask_for_input()->chr:
    """Function to take a single character input and check it against the correct word

    Returns:
        chr: user guess
    """
    print("Please make a single letter guess")
    while True:
        guess = input()
        if guess.isalpha:
            check_guess(guess, word)
            return guess
        else:
            "Invalid letter. Please, enter a single alphabetical character."

def check_guess(guess, word):
    """Check user guess against the correct answer

    Args:
        guess (chr): single character guess from the user
        word (string): correct word to be checked against
    """
    if guess.lower() in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        

word_list = ["apple", "banana", "orange", "mango", "pear"]
word = random_word_choice(word_list)
print(word)

guess = ask_for_input()

