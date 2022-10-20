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



    def create_wordList(self):
        """
        establish a wordlist from which a word is chosen at random.
        """
        self._list_of_words = [
            "class", "horse", "basketball", "swimmer", "ship",
            "development", "python"
            
            # Jumper('class'),
            # Jumper('horse'),
            # Jumper('basketball'),
            # Jumper('swimmer'),
            # Jumper('ship'),
            # Jumper('developement'), 
            # Jumper('python'), 
            # Jumper('student'), 
            # Jumper('arguments'), 
            # Jumper('teamwork'), 
            # Jumper('encapsulate'), 
            # Jumper('abstract'), 
            # Jumper('jumper'), 
            ]
        word = random.choice(self._list_of_words)
        return Jumper(word)
    
    
    # Copy code from the other director file over everything below still needs
    # to be edited for our file. (Zack D.)

    def start_game(self):
        """ 
        loops until the game is won or lost 
        and loops while the player wants to keep playing.
        """
        self.jumper = self.create_wordList()
        tries = 4

        while self.is_playing:
            game_over = False
            
            while not game_over:
                self.guesser.print_parachute(tries)
                if tries != 0:
                    self.jumper.show_hidden_word()
                    guessed_correctly = self.jumper.check_guess(self.terminal_service.guess())
                
                    if (not guessed_correctly):
                        tries -= 1
                        # game_over = self.guesser.remove_parachute(0)

                elif self.guesser.remove_parachute(0) == self.guesser.remove_parachute(tries):
                    print("\nOh no!  Your parachute is gone!\n Game Over!")
                    self.guesser.print_parachute(0)
                    print(f"The word was: {self.jumper.show_word()}")
                    game_over = True
                    print("\nThank you for playing!\n")
                    self.is_playing = False

                elif (self.jumper.is_word_complete()):
                    print("\nCongratulations!  You guessed the word!\n")
                    print(f"The word was: {self.jumper.show_word()}")
                    # self.jumper.show_hidden_word()
                    print()
                    game_over = True   
                    print("\nThank you for playing!\n")     
                    self.is_playing = False
                
            
            # play_again = self.terminal_service.play_again()
            # if play_again == "y" and game_over:
            #     tries = 4
            #     self.guesser.reset_drawing()
            #     self.jumper = random.choice(self._list_of_words)
            # else:
            #     print("\nThank you for playing!\n")

