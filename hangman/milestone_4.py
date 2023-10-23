
from random import choice as random_word_choice
import string

word_list = ["apple", "banana", "orange", "mango", "pear"]

class Hangman:
    """ Hangman class to hold all necessary functionality to play a single round of hangman
    """
    
    def __init__(self, word_list, num_lives=5):
        
        self.word_list = word_list  # list of possible words
        self.num_lives = num_lives  # number of lives starting at 5
        self.word = random_word_choice(word_list)   # choice of word for current round
        self.word_guessed = ['_' for _ in self.word] # empty list to be filled by player guesses corresponding to the answer
        self.num_letters = len(set(self.word))   # number of unique letters left to guess
        self.list_of_guesses = []   # list of guesses by player
        
        print(f"Word has {len(self.word)} letters and {self.num_letters} unique letters")
    
    def ask_for_input(self)->chr:
        """Function to take a single character input and check it against the correct word

        Returns:
            chr: user guess
        """
        print("Please make a single letter guess")
        while True:
            guess = input()
            if guess not in string.ascii_letters:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess, self.word)
                return guess
        
    def check_guess(self, guess, word):
        """Check user guess against the correct answer

        Args:
            guess (chr): single character guess from the user
            word (string): correct word to be checked against
        """
        if guess.lower() in word:
            print(f"Good guess! {guess} is in the word.")
            for letter in range(len(word)):
                if guess == word[letter]:
                    self.word_guessed[letter] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
            
            
            
game_instance = Hangman(word_list)
print("Game started")
# while ''.join(game_instance.word_guessed) != game_instance.word:
#     game_instance.ask_for_input()
#     print(f"The word so far: {game_instance.word_guessed}")
# print("Congratulations dood")
# print("Guess entered")
# game_instance.ask_for_input()
# print("Guess entered")
