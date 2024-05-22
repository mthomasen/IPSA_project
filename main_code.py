from Table_class import Table
from Strategies import strategy

from datetime import datetime
import pytz
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


os.chdir("D:\AU_Cog_Sci\matematik_tilvalg\intro_prog\exam_project\IPSA_project")


def save_main_plot(data, x_axis, y_axis, filter, folder):
  sns.set(style='whitegrid')
  plt.figure(figsize=(10, 6))
  sns.lineplot(data=data, x=x_axis, y=y_axis, hue=filter)
  plt.title('{} Over {} by {}'.format(y_axis, x_axis, filter))
  plt.xlabel(f'{x_axis}')
  plt.ylabel(f'{y_axis}')
  plt.legend(title=f'{filter}')

  plot_name = '{}/main_plot_{}_{}_{}.png'.format(folder, time_stamp.hour,
                                                 time_stamp.minute,
                                                 time_stamp.second)

  plt.savefig(plot_name, dpi=300, bbox_inches='tight')

  plt.close()


time_stamp = datetime.now(pytz.timezone('Europe/Copenhagen'))
folder = f'plots_{time_stamp.day}_{time_stamp.month}'
plot_files = []

if not os.path.exists('logfiles'):
  os.makedirs('logfiles')

logfile_name = 'logfiles/logfile_{}_{}_{}.csv'.format(time_stamp.hour,\
                time_stamp.minute, time_stamp.second)

logfile_columns = [
    'strategy', 'wealth', 'game_ending', 'games_played', 'player_bet'
]

main_dataframe = pd.DataFrame(columns=logfile_columns)

for i in range(len(strategy)):
  print('----------------------------')
  print(f'strategy_{i+1}')
  new_table = Table(400000, 8, 500000, 10, strategy[i])
  new_table.play_games()
  new_table.print_table_stats()
  data_frame = new_table.make_dataframe()
  main_dataframe = pd.concat([main_dataframe, data_frame])
  plot_file = new_table.plot_table_stats(folder)
  plot_files.append(plot_file)

save_main_plot(main_dataframe, 'games_played', 'wealth', 'strategy', folder)

main_dataframe.to_csv(logfile_name)
