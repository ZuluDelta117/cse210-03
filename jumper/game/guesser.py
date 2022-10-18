import random

# Tried to model this file after the hider.py file from the earlier assignment

class Guesser:
  """
  The person trying to guess which word is being used
  """
  def __init__(self):
    words = ['class', 'horse', 'basketball', 'swimmer', 'ship']
    self._word = random.choice(words)
    tries = 4
    
  
  def underscore(self):
    length_word = len(self._word)
    underscore = ("_" * length_word)

    return underscore

  def stages(tries):
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
