import random
# Tried to model this file after the seeker.py file from the earlier assignment

class Jumper:
  """
  The responsibility of Jumper is to keep track of the random word that the jumper will be using and to keep track of how many guesses they have left
  """
  
  def __init__(self):
    """
    Constructs a new jumper
    """
    # really unsure about how to set this function up (Zack D.)
    words = ['class', 'horse', 'basketball', 'swimmer', 'ship']
    self._word = random.choice(words).lower()

    
    
  def get_word(self):
    """
    Gets word for the guesser
    """
    # Did my best to fugure out the logic of this function and the next. 
    # Feel free to make changes where needed. (Zack D.)

    return self._underscore
  
  
  def hide_word(self, word):
    """
    Hides the word from the guesser
    """
    length_word = len(self._word)
    self._underscore = ("_" * length_word)

    

  
    
    
