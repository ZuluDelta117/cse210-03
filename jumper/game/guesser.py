import random

# Tried to model this file after the hider.py file from the earlier assignment

class Guesser:
  """
  The person trying to guess which word is being used
  """
  def __init__(self):
    """
    Makes a list of the possible displays depending on if they get something wrong
    """
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
      # This method prints the parachute part of the drawing when called.
      print(self._parachute[tries])

  def remove_parachute(self, tries):
      # This method removes parts of the parachute drawing when an incorrect letter is guessed.
      parachute_gone = False
      # self._parachute = self._parachute[tries]
      if self._parachute[0] == self._parachute[tries]:
        parachute_gone = True
        
      return parachute_gone

