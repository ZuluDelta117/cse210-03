import random
from game.guesser import Guesser
from game.jumper import Jumper
from game.terminal_service import TerminalService
# First we want to import all of the classes we need - Jordan

class Director:
    def __init__(self):
        # Assign classes to variables/ attributes - Jordan
        self.list_of_words = []
        self.terminal_service = TerminalService()
        self.guesser = Guesser()
        self.jumper = Jumper("")
        self.is_playing = True


    # I was unable to get the word list to work in any other file so I just kept it here
    def create_wordList(self):
        """
        establish a wordlist from which a word is chosen at random.
        """
        self._list_of_words = [
            "class", "horse", "basketball", "swimmer", "ship",
            "development", "python", "student", "arguments",
            "teamwork", "encapsulate", "abstract", "jumper"
            ]
        word = random.choice(self._list_of_words)
        # run the word through the Jumper class to hide the word
        return Jumper(word)
    
    
    # This function runs the game until game over (Zack D.)
    def start_game(self):
        """ 
        loops until the game is won or lost 
        and loops while the player wants to keep playing.
        """
        self.jumper = self.create_wordList()
        # total number of incorrect tries before game over
        tries = 4
        
        # If the player is playing continue game
        while self.is_playing:
            game_over = False
            
            while not game_over:
                # Display the parachute 
                self.guesser.print_parachute(tries)

                # If it is not game over then ask for another letter
                if tries != 0:
                    self.jumper.show_hidden_word()
                    guessed_correctly = self.jumper.check_guess(self.terminal_service.guess())

                    # If the player did not guess correctly subtract one try
                    if (not guessed_correctly):
                        tries -= 1

                # If the user is at 0 tries then it will tell the user game over
                elif self.guesser.remove_parachute(0) == self.guesser.remove_parachute(tries):
                    print("\nOh no!  Your parachute is gone!\n Game Over!")
                    self.guesser.print_parachute(0)
                    print(f"The word was: {self.jumper.show_word()}")
                    # The player lost so it is game over
                    game_over = True
                    print("\nThank you for playing!\n")
                    # Player is not longer playing
                    self.is_playing = False

                # If the user got the word correct it will congratulate the player
                elif (self.jumper.is_word_complete()):
                    print("\nCongratulations!  You guessed the word!\n")
                    print(f"The word was: {self.jumper.show_word()}")
                    print()
                    # The player won so it is game over
                    game_over = True   
                    print("\nThank you for playing!\n")     
                    # Player is no longer playing
                    self.is_playing = False
                
            
            
            # Could not get play again to work so I commented it out (Zack D.)

            # play_again = self.terminal_service.play_again()
            # if play_again == "y" and game_over:
            #     tries = 4
            #     self.guesser.reset_drawing()
            #     self.jumper = random.choice(self._list_of_words)
            # else:
            #     print("\nThank you for playing!\n")

