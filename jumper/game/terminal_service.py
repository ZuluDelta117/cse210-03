

class TerminalService:
    # Obviously we want to set this class up to display to the terminal - Jordan
    def __init__(self):
        """
        Create the initial guess as an empty string.
        """
        self.letter_guess = ""

    def guess(self):
        """
        Get the user input for their guess of what a letter is in the secret word.
        """
        self.letter_guess = input("Guess a letter [a-z]: ").lower()
        return (self.letter_guess)

    # I commented this out because I cannot get the play again function to work
    # def play_again(self):
    #     """
    #     Get user input for whether the player wants to play again.
    #     """
    #     self.play_again_choice = input("Play again [y/n]? ").lower()
    #     return (self.play_again_choice)

