import random

class Jumper:
  """
  The responsability of Jumper is to keep track of the random word that the jumper will be using and to keep track of how many guesses they have left
  """
  
  def __init__(self):
    """
    Constructs a new jumper
    """
    # really unsure about how to set this function up (Zack D.)
    words = ['class', 'horse', 'basketball', 'swimmer', 'ship']
    self._word = random.choice(words)
    
    
    
  def get_word(self):
    """
    Gets word for the guesser
    """
    length_word = len(self._word)
    underscore = ("_" * length_word)
    
    return underscore
  
  
  def letter_found(self):
    """
    Tells you which letter was correctly found
    """
    pass
  
    
    
