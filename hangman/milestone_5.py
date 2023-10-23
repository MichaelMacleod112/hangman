from random import choice as random_word_choice
import string
import warnings

word_list_short = ["apple", "banana", "orange", "mango", "pear"] # list of possible words


# import NLTK library to use a longer list of words to play with
nltk_import_successful = False  # initialise flag
try:
    import nltk
    nltk.download('words')
    from nltk.corpus import words
    word_list_long = words.words() # much longer list of possible words
    nltk_import_successful = True  # signal nltk has been imported succesfully
    
except ImportError as e:
    warnings.warn("NLTK is not installed. Limited to short possible word list without NLTK.")
except LookupError as e:
    warnings.warn("The 'words' corpus data is not found. Limited to short possible word list.")



class Hangman:
    """ Hangman class to hold all necessary functionality to play a single round of hangman
    """
    
    def __init__(self, num_lives=5):
        # thought it more sensible to select word list from within the class rather than pass it in, due to the choice between two lists
        self.__choose_word_list()
        self.num_lives = num_lives  # number of lives starting at 5
        self.word = random_word_choice(self.word_list)   # choice of word for current round
        self.word_guessed = ['_' for _ in self.word] # empty list to be filled by player guesses corresponding to the answer
        self.num_letters = len(set(self.word))   # number of unique letters left to guess
        self.list_of_guesses = []   # list of guesses by player
        
        if len(self.word)>5:
            # increase number of lives if word is long
            self.num_lives = len(self.word)
        
        print(f"Word has {len(self.word)} letters and {self.num_letters} unique letters")
    
    def __choose_word_list(self):
        """Sets internal word list based on user choice between two options
        """
        if nltk_import_successful:
            print("Would you to play with the long or short list of words? l/s")
            new_game = input()
            while new_game.lower() not in ['l', 's']:
                new_game = input()
            if new_game == 'l':
                self.word_list = word_list_long 
            else:
                self.word_list = word_list_short
        else:
            print("Using short word list")
            self.word_list = word_list_short

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
        
    def check_guess(self, guess, word)->None:
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
            bool : new round started if True, otherwise game exits
        """
        print("Play again? y/n")
        new_game = input()
        while new_game.lower() not in ['y', 'n']:
            new_game = input()
        if new_game == 'y': return True 
        else: return False
    
    def is_word_guessed(self)->bool:
        """Returns bool to check if the word has been correctly guessed
        """
        return ''.join(self.word_guessed) == self.word
        
        
def play_game()->bool:
    """Instantiates hangman class to play a single round of hangman

    Returns:
        bool: new round of game will start if returning True
    """
    game_instance = Hangman()
    
    while  not game_instance.is_word_guessed():
        if game_instance.num_lives == 0:
            print("You lost!")
            #TODO
            # print("Would you like to purchase more lives? y/n")
            # if input() == "y":
            #     print("Please enter your bank details")
            print(f"The correct word was {game_instance.word}!")
            return Hangman.play_again()
        
        game_instance.ask_for_input()
        
        if not game_instance.is_word_guessed():
            print(f"The word so far: {game_instance.word_guessed}")
            
    print(f"Congratulations! The correct word was {game_instance.word}!")
    return Hangman.play_again()



if __name__ == "__main__":
    print("Welcome to hangman!")
    play = True
    while play == True:
        play = play_game()
    print("Thanks for playing!")