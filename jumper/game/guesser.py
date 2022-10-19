import random

# Tried to model this file after the hider.py file from the earlier assignment

class Guesser:
  """
  The person trying to guess which word is being used
  """
  def __init__(self):
    words = ['class', 'horse', 'basketball', 'swimmer', 'ship']
    self._word = random.choice(words)
    # how many wrong answers they can input before game over
    tries = 4
    
  
  def underscore(self):
    length_word = len(self._word)
    underscore = ("_" * length_word)

    return underscore

  def stages(tries):
    """
    Makes a list of the possible displays depending on if they get something wrong
    """
    stages = [
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

    return stages[tries]
  
  def found_letters(self):

    pass

  def watch_guesser(self, guess):
    """
    replace the underscores with the correct letters
    """
    while not guessed and tries > 0:
    # This portion of code will eventually check to see what letter they guessed and replace the underscore
    # with the proper letter. 
    # I do not know if the code should go here or somewhere else. Feel free to make adjustments (Zack D.)
      if guess.isalpha():
        if guess not in word:
          tries -= 1
        else:
          break
  
      else:
        print("Not a valid guess")

