
def strategy_1(cards, card_sum, dealer_cards):
  '''Hits whenever the sum of the cards are less 
  than 21

  Doctest:
  >>> strategy_1(['A','3'], 14, ['3','9'])
  1

  >>> strategy_1(['10','3','J'], 23, ['7','10'])
  0

  >>> strategy_1(['J','K'], 20, ['A','10'])
  1
  '''
  if card_sum < 21:
    return 1
  else:
    return 0


def strategy_2(cards, card_sum, dealer_cards):
  '''Always stands never hits 

  Doctest:
  >>> strategy_2(['K','J'], 20, ['K','9'])
  0

  >>> strategy_2(['10','7'], 17, ['2','10'])
  0

  >>> strategy_2(['3','K'], 13, ['5','10'])
  0
  '''
  return 0


def strategy_3(cards, card_sum, dealer_cards):
  '''Hits when sum of the cards is less than 17 

  Doctest:
  >>> strategy_3(['5','2'], 7, ['K','9'])
  1

  >>> strategy_3(['10','7'], 17, ['K','5'])
  0

  >>> strategy_3(['6','K'], 16, ['5','10'])
  1
  '''
  if card_sum < 17:
    return 1
  else:
    return 0


def strategy_4(cards, card_sum, dealer_cards):
  '''If the card sum is less than 17 the player will 
  always hit, if it is above 17 whether the player 
  hits or stands is dependent on whether or not 
  they have an A

  Doctest:
  >>> strategy_4(['A','7'], 18, ['10','9'])
  1

  >>> strategy_4(['10','8'], 18, ['7','10'])
  0

  >>> strategy_4(['5','K'], 15, ['5','8'])
  1
  '''
  if card_sum < 17:
    return 1
  elif card_sum < 20 and card_sum >= 17:
    for i in range(len(cards)):
      if cards[i] == 'A':
        return 1
      else:
        return 0
  else:
    return 0


def strategy_5(cards, card_sum, dealer_cards):
  '''Hits if sum is less than 17, and if sum is less than 19 
  while the dealers revealed card is an Ace.

  Doctest:
  >>> strategy_5(['10','8'], 18, ['K','9'])
  0

  >>> strategy_5(['8','9'], 17, ['A','10'])
  1

  >>> strategy_5(['J','4'], 14, ['5','10'])
  1
  '''
  if card_sum < 19 and dealer_cards[0] == 'A' or card_sum < 17:
    return 1
  else:
    return 0


def strategy_6(cards, card_sum, dealer_cards):
  '''Hits when sum of cards less than 18  

  Doctest:
  >>> strategy_6(['K','J'], 20, ['A','9'])
  0

  >>> strategy_6(['4','7'], 11, ['8','A'])
  1

  >>> strategy_6(['A','K'], 13, ['K','10'])
  1
  '''
  if card_sum < 18:
    return 1
  else:
    return 0


def strategy_7(cards, card_sum, dealer_cards):
  '''Stands when sum of the over 15 and 
  the dealers shown card value is less than 6,
  otherwise, stands when card sum greater than 17

  Doctest:

  >>> strategy_7(['8','J'], 18, ['5','9'])
  0

  >>> strategy_7(['10','9'], 19, ['K','10'])
  0

  >>> strategy_7(['9','7'], 16, ['6','10'])
  1
  '''
  if card_sum > 15 and dealer_cards[0] in ['2','3','4','5']:
    return 0
  elif card_sum < 17:
    return 1
  else:
    return 0


strategy = [strategy_1, strategy_2,strategy_3, 
            strategy_4, strategy_5, strategy_6, 
            strategy_7]

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
