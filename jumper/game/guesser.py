import random

# Tried to model this file after the hider.py file from the earlier assignment

class Guesser:
  """
  The person trying to guess which word is being used
  """
  def __init__(self):
    """
    Makes a list of the possible displays depending on how many tries they have left
    """
    # List of each possible display
    self._parachute = [
      """
          X
         /|\ 
         / \ 

      ^^^^^^^^^
      """,
      """
         \ /
          O
         /|\ 
         / \ 

      ^^^^^^^^^
      """,
      """
        \   /
         \ /
          O
         /|\ 
         / \ 

      ^^^^^^^^^
      """,
      """
        /___\ 
        \   /
         \ /
          O
         /|\ 
         / \ 

      ^^^^^^^^^
      """,
      """
         ___
        /___\ 
        \   /
         \ /
          O
         /|\ 
         / \ 

      ^^^^^^^^^
      """
    ]


  def print_parachute(self, tries):
    """
    Print the correct display depending on the number of tries left
    """
    print(self._parachute[tries])

  def remove_parachute(self, tries):
    """
    Keeps track if the parachuter has died and the player has a game over
    """
    parachute_gone = False

    if self._parachute[0] == self._parachute[tries]:
      parachute_gone = True
        
    return parachute_gone

