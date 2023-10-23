from random import choice as random_word_choice
import string

class Hangman:
    """ Hangman class to hold all necessary functionality to play a single round of hangman
    """
    
    def __init__(self, num_lives=5):
        
        self.word_list = ["apple", "banana", "orange", "mango", "pear"] # list of possible words
        self.num_lives = num_lives  # number of lives starting at 5
        self.word = random_word_choice(self.word_list)   # choice of word for current round
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
        """Check user guess against letters in the correct answer

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
            
    @staticmethod  
    def play_again()->bool:
        """ Gets user input to decide whether or not to start a new round

        Returns:
            bool: starts a new round on True, ends game on False
        """
        print("Play again? y/n")
        new_game = input()
        while new_game.lower() not in ['y', 'n']:
            new_game = input()
        if new_game == 'y': return True 
        else: return False
    
def play_game():
    game_instance = Hangman()
    print("Game started")
    while ''.join(game_instance.word_guessed) != game_instance.word:
        if game_instance.num_lives == 0:
            print("You lost!")
            return Hangman.play_again()
        game_instance.ask_for_input()
        print(f"The word so far: {game_instance.word_guessed}")
    return Hangman.play_again()


if __name__ == "__main__":
    play = True
    while play == True:
        play = play_game()
    print("Thanks for playing!")