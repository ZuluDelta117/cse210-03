# Tried to model this file after the seeker.py file from the earlier assignment 

class Jumper:
    """
    The responsibility of Jumper is to keep track and hide the random word that 
    the jumper will be using
    """


    def __init__(self, random_word):
        """
        Constructs a new jumper
        """

        self.letters = []
        self._word_hidden = []
        self._word_complete = False
        
        # make a list of letters from the random word
        for letter in random_word:
            self.letters.append(letter)
        # take the list of letters from the random word and makes a list of underscore
        for letter in self.letters:
            letter = "_"
            # stablish a list of underscores to match the word.
            self._word_hidden.append(letter)
    
    def is_word_complete(self):
        """
        lets the Host know that the word has been completely guessed.
        """
        return(self._word_complete)

    def show_hidden_word(self): 
        """
        Hides the word from the guesser
        """
        word = ""
        for letter in range(len(self._word_hidden)):
            word += self._word_hidden[letter]
        print(word)               
        print()

    def show_word(self): 
        """
        Display the word the player has been trying to guess
        """

        word = ""
        for letter in range(len(self.letters)):
            word += self.letters[letter]
        return word

    def check_guess(self, guess):
        """
        take the letter passed as a parameter and see if it is in the hidden word
        """
        guessed_correctly = False
        position = 0
        for i in self.letters:
            if i == guess:
                self._word_hidden[position] = guess
                guessed_correctly = True
            position += 1

        position = 0
        self._word_complete = True
        
        # Check to see if the word is found
        if guessed_correctly:
            for i in self._word_hidden:
                if i == "_":
                    self._word_complete = False
                position += 1
            return (guessed_correctly)
