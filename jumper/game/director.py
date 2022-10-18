from game.guesser import Guesser
from game.jumper import Jumper
from game.terminal_service import TerminalService
# First we want to import all of the classes we need - Jordan

class Director:
    def __init__(self):
        # Assign classes to variables/ attributes - Jordan
        self._guesser = Guesser()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()


    # Copy code from the other director file over everything below still needs
    # to be edited for our file. (Zack D.)
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        new_location = self._terminal_service.read_word("\nGuess a letter [a-z]: ")
        self._seeker.move_location(new_location)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        self._hider.watch_seeker(self._seeker)
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        hint = self._hider.get_hint()
        self._terminal_service.write_text(hint)
        if self._hider.is_found():
            self._is_playing = False
