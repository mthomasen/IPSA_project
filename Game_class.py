from Strategies import *

from Card_deck_class import *


class Game:

  def __init__(self, number_of_decks, player_bet, strategy):
    self.player_cards = []
    self.dealer_cards = []
    self.player_wealth = None
    self.number_of_decks = number_of_decks
    self.game_card_deck = None
    self.player_done = 'no'
    self.player_sum = None
    self.dealer_sum = None
    self.game_ending = None
    self.player_bet = player_bet
    self.strategy = strategy
    self.game_ending = 0

  def calculate_sum(self, cards):
    '''Calculates the sum of the given cards
    so it can be used for the startegies and figuring out who won

    Doctest:
    >>> Game1 = Game(8, 100, strategy_1)
    >>> Game1.calculate_sum(['Q','2'])
    12

    >>> Game2 = Game(8, 100, strategy_2)
    >>> Game2.calculate_sum(['A','10'])
    21

    >>> Game3 = Game(8, 100, strategy_5)
    >>> Game3.calculate_sum(['8','8','A'])
    17
    '''
    card_sum = 0
    for card in cards:
      if card.isdigit():
        card_sum += int(card)
      elif card in ['J', 'Q', 'K']:
        card_sum += 10
      elif card == 'A':
        card_sum += 11
    ace_count = cards.count('A')
    while card_sum > 21 and ace_count > 0:
      card_sum -= 10
      ace_count -= 1
    return card_sum

  def start(self):
    '''Creates a new deck, deals the cards, and calculates the sums of the 
    cards
    doctest:
    >>> Game1 = Game (8, 100, strategy_4)
    >>> Game1.start()
    >>> len(Game1.player_cards)
    2
    >>> len(Game1.dealer_cards) 
    2
    >>> len(Game1.game_card_deck.cards)
    412
    '''
    self.game_card_deck = card_deck(self.number_of_decks)
    self.game_card_deck.create_deck()

    self.player_cards = self.game_card_deck.cards[0:2]
    self.game_card_deck.deal_cards()

    self.dealer_cards = self.game_card_deck.cards[0:2]
    self.game_card_deck.deal_cards()

    self.player_sum = self.calculate_sum(self.player_cards)
    self.dealer_sum = self.calculate_sum(self.dealer_cards)

  def player_move(self):
    '''This function is the player's move, it will keep drawing cards 
    and making choices based on strategies
    Doctest:
    >>> Game1 = Game(8, 100, strategy_1)
    >>> Game1.start()
    >>> Game1.player_cards = ['8','8']
    >>> Game1.player_move()
    >>> print(Game1.player_done)
    yes

    >>> Game2 = Game(8, 100, strategy_4)
    >>> Game2.start()
    >>> Game2.player_cards = ['A','7']
    >>> Game2.player_move()
    >>> len(Game2.player_cards)
    3

    >>> Game3 = Game(8, 100, strategy_2)
    >>> Game3.start()
    >>> Game3.player_cards = ['9','K']
    >>> Game3.player_move()
    >>> len(Game3.player_cards)
    2
    '''
    while self.player_done == 'no':
      while self.player_sum < 21:
        choice = self.strategy(self.player_cards, self.player_sum,
                               self.dealer_cards)
        if choice == 0:
          self.player_done = 'yes'
          break
        if choice == 1:
          self.player_cards.extend(self.game_card_deck.cards[0])
          self.game_card_deck.draw_card()
          self.player_sum = self.calculate_sum(self.player_cards)
      self.player_done = 'yes'

  def dealer_move(self):
    '''This function is the dealer's move, it will keep drawing cards
    until it reaches 17 or higher.

    doctest:
    >>> Game1 = Game(8, 100, strategy_1)
    >>> Game1.start()
    >>> Game1.dealer_cards = ['10','8'] 
    >>> Game1.dealer_move()
    >>> len(Game1.dealer_cards)
    2

    >>> Game2 = Game(8, 100, strategy_5)
    >>> Game2.start()
    >>> Game2.dealer_cards = ['5','4','8']
    >>> Game2.player_cards = ['J','8']
    >>> Game2.dealer_move()
    >>> len(Game2.dealer_cards)
    3
    >>> len(Game2.player_cards)
    2


    >>> Game3 = Game(8, 100, strategy_5)
    >>> Game3.start()
    >>> Game3.dealer_cards = ['J','6']
    >>> Game3.dealer_move()
    >>> len(Game3.dealer_cards)
    3
    '''
    self.dealer_sum = self.calculate_sum(self.dealer_cards)

    while self.dealer_sum < 17:
      self.dealer_cards.extend(self.game_card_deck.cards[0])
      self.game_card_deck.draw_card()
      self.dealer_sum = self.calculate_sum(self.dealer_cards)

  def end_game(self):
    '''This function is the end of the game, it will calculate the
    the amount of money the player has won or lost, and if the player
    has won, it will add the bet to their wealth.


    doctest: 
    >>> Game1 = Game(8, 100, strategy_2)
    >>> Game1.start()
    >>> Game1.player_sum = 18 
    >>> Game1.dealer_sum = 17
    >>> Game1.player_done = 'yes'
    >>> Game1.end_game()
    >>> print(Game1.game_ending)
    1

    >>> Game2 = Game(8, 100, strategy_2)
    >>> Game2.start()
    >>> Game2.player_sum = 19
    >>> Game2.dealer_sum = 19
    >>> Game2.player_done = 'yes'
    >>> Game2.end_game()
    >>> print(Game2.game_ending)
    0


    >>> Game3 = Game(8, 100, strategy_2)
    >>> Game3.start()
    >>> Game3.player_sum = 24
    >>> Game3.dealer_sum = 19
    >>> Game3.player_done = 'yes'
    >>> Game3.end_game()
    >>> print(Game3.game_ending) 
    -1

    >>> Game4 = Game(8, 100, strategy_2)
    >>> Game4.player_cards = ['10','A']
    >>> Game4.dealer_cards = ['10','9']
    >>> Game4.player_sum = 21
    >>> Game4.dealer_sum = 19
    >>> Game4.player_done = 'yes'
    >>> Game4.end_game()
    >>> print(Game4.game_ending) 
    1.5

    '''
    if self.dealer_sum >= 17 and self.player_done == 'yes':
      if self.player_sum < 21:
        if (self.dealer_sum < self.player_sum) or (self.dealer_sum > 21):
          self.game_ending = 1
        elif self.dealer_sum == self.player_sum:
          self.game_ending = 0
        else:
          self.game_ending = -1
      elif self.player_sum == 21:
        if len(self.player_cards) == 2 and (len(self.dealer_cards) > 2
                                            or self.dealer_sum != 21):
          self.game_ending = 1.5
        elif self.dealer_sum == 21:
          self.game_ending = 0
        else:
          self.game_ending = 1
      else:
        self.game_ending = -1
