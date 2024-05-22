from Game_class import *

import matplotlib.pyplot as plt

import os

import pytz

from datetime import datetime

import pandas as pd


class Table:

  def __init__(self, number_of_games, number_of_decks, player_wealth,
               player_bet, strategy):
    self.number_of_games = number_of_games
    self.number_of_decks = number_of_decks
    self.games_played = 0
    self.player_wealth = player_wealth
    self.player_bet = player_bet
    self.game = Game(self.number_of_decks, self.player_bet, strategy)
    self.player_won = 0
    self.dealer_won = 0
    self.tied = 0
    self.player_blackjack = 0
    self.strategy = strategy
    self.wealth_stats = [self.player_wealth]
    self.stats_game_ending = [0]
    self.stats_games_played = [0]
    self.stats_bet = [self.player_bet]
    self.strategy_name = strategy.__name__
    self.dataframe = None

  def update_wealth(self):
    '''This function is the end of the game, it will calculate the
    sum of all the wealth after each game.

    doctest:
    >>> Table1 = Table(1, 8, 1000, 416, strategy_1)
    >>> Table1.game.game_ending = -1
    >>> Table1.update_wealth()
    >>> print(Table1.player_wealth)
    584

    >>> Table2 = Table(1, 8, 584, 113, strategy_1)
    >>> Table2.game.game_ending = 1
    >>> Table2.update_wealth()
    >>> print(Table2.player_wealth)
    697

    >>> Table3 = Table(1, 8, 349, 113, strategy_1)
    >>> Table3.game.game_ending = 0
    >>> Table3.update_wealth()
    >>> print(Table3.player_wealth)
    349
    '''
    self.player_wealth += (self.game.player_bet * self.game.game_ending)

  def who_won(self):
    '''This function is the end of the game and will calculate
    how many times the player has won, lost, or tied.

    doctest:
    >>> Table1 = Table(1, 8, 349, 113, strategy_1)
    >>> Table1.game.game_ending = 1
    >>> Table1.who_won()
    >>> print(Table1.player_won)
    1
    >>> print(Table1.dealer_won)
    0
    >>> print(Table1.player_blackjack)
    0

    >>> Table2 = Table(1, 8, 349, 113, strategy_1)
    >>> Table2.game.game_ending = 1.5
    >>> Table2.who_won()
    >>> print(Table2.player_won)
    0
    >>> print(Table2.dealer_won)
    0
    >>> print(Table2.player_blackjack)
    1

    >>> Table3 = Table(1, 8, 349, 113, strategy_1)
    >>> Table3.game.game_ending = 0
    >>> Table3.who_won()
    >>> print(Table3.dealer_won)
    0
    >>> print(Table3.player_blackjack)
    0
    >>> print(Table3.tied)
    1
    '''
    if self.game.game_ending == 1:
      self.player_won += 1
    elif self.game.game_ending == 1.5:
      self.player_blackjack += 1
    elif self.game.game_ending == -1:
      self.dealer_won += 1
    else:
      self.tied += 1

  def table_statistics(self):
    '''This function is the end of game and will calculate the 
    statistiscs of the wealth, bet, and number of games played.

    doctest:
    >>> Table1 = Table(1, 8, 300, 100, strategy_1)
    >>> Table1.game.game_ending = 1
    >>> Table1.table_statistics()
    >>> print(Table1.wealth_stats)
    [300, 300]
    '''
    self.wealth_stats.append(self.player_wealth)
    self.stats_game_ending.append(self.game.game_ending)
    self.stats_games_played.append(self.games_played)
    self.stats_bet.append(self.player_bet)

  def play_games(self):
    '''This function is the main part of the code, it will play the games
    and update the wealth after each game.

    doctest:
    >>> Table1 = Table(4, 8, 1000,  100, strategy_1)
    >>> Table1.play_games()
    >>> print(Table1.games_played)
    4


    >>> Table2 = Table(12, 8, 1000, 100, strategy_1)
    >>> Table2.play_games()
    >>> print(Table2.games_played)
    12

    '''
    while self.games_played < self.number_of_games:
      self.game.start()
      self.game.player_move()
      self.game.dealer_move()
      self.game.end_game()
      self.who_won()
      self.update_wealth()
      self.games_played += 1
      self.table_statistics()

  def print_table_stats(self):
    '''
    Doctest:
    >>> Table1 = Table(12, 8, 3564, 100, strategy_1)
    >>> Table1.player_won = 6
    >>> Table1.dealer_won = 4
    >>> Table1.tied = 1
    >>> Table1.player_blackjack = 1
    >>> Table1.print_table_stats()
    You got black Jack 1 times
    The player won 6 times
    You tied 1 times
    The dealer won 4 times
    The Players wealth is now 3564
    '''
    print(f'You got black Jack {self.player_blackjack} times')
    print(f'The player won {self.player_won} times')
    print(f'You tied {self.tied} times')
    print(f'The dealer won {self.dealer_won} times')
    print(f'The Players wealth is now {self.player_wealth}')

  def plot_table_stats(self, folder):

    plt.plot(self.stats_games_played, self.wealth_stats)
    plt.title(f'Earnings over games played for {self.strategy_name}')
    plt.xlabel('Number of games played')
    plt.ylabel('Player wealth')

    if not os.path.exists(folder):
      os.makedirs(folder)

    time_stamp = datetime.now(pytz.timezone('Europe/Copenhagen'))
    filename = f'{folder}/plot_{self.strategy_name}_{time_stamp.hour}_\
    {time_stamp.minute}_{time_stamp.second}.png'

    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    return filename

  def make_dataframe(self):

    self.dataframe = pd.DataFrame({
        'strategy': self.strategy_name,
        'wealth': self.wealth_stats,
        'game_ending': self.stats_game_ending,
        'games_played': self.stats_games_played,
        'player_bet': self.stats_bet
    })

    return self.dataframe


if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
