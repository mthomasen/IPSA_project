import random


class card_deck:

  
  def __init__(self, number_of_decks):
    self.number_of_decks = number_of_decks
    self.cards = None

  
  def create_deck(self):
    '''Creates a list containing all of the card values 4 times, 
    correspondign to a whole deck. 
    This list is then repeated the indicated number of decks times

    doctest:
    >>> deck = card_deck(8)
    >>> len(deck.create_deck())
    416

    >>> deck2 = card_deck(3)
    >>> len(deck2.create_deck())
    156
    '''
    self.cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
    ]
    self.cards = [j for j in self.cards for i in range(4)]
    self.cards = [j for j in self.cards for i in range(self.number_of_decks)]
    random.shuffle(self.cards)
    return self.cards

  
  def deal_cards(self):
    self.cards.pop(0)
    self.cards.pop(0)

  
  def draw_card(self):
    self.cards.pop(0)
