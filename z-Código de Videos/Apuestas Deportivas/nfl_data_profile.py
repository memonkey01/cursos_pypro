# -*- coding: utf-8 -*-
"""
Video: Apuestas deportivas
Autor: Guillermo Izquierdo
"""

import pandas as pd
from pandas_profiling import ProfileReport
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
sns.set_theme(style="ticks", palette="pastel")
WEEK = 2

df = pd.read_csv(f'./data/pre_game_{WEEK + 1}_mod.csv').set_index('match_key')

###
#prof = ProfileReport(df)
#prof.to_file(output_file='output.html')
###

pivot_win = pd.pivot_table(df, index='win_or_lose', values=['off_pass_att', 'off_pass_cmp', 'off_pass_cmp_pct',
       'off_pass_yds_per_att', 'off_pass_pass_yds', 'off_pass_td',
       'off_pass_int', 'off_pass_rate', 'off_pass_1st', 'off_pass_1st_pct',
       'off_pass_20_plus', 'off_pass_40_plus', 'off_pass_lng', 'off_pass_sck',
       'off_pass_scky', 'off_rush_att', 'off_rush_rush_yds', 'off_rush_ypc',
       'off_rush_td', 'off_rush_20_plus', 'off_rush_40_plus', 'off_rush_lng',
       'off_rush_rush_1st', 'off_rush_rush_1st_pct', 'off_rush_rush_fum',
       'def_pass_att', 'def_pass_cmp', 'def_pass_cmp_pct',
       'def_pass_yds_per_att', 'def_pass_yds', 'def_pass_td', 'def_pass_int',
       'def_pass_1st', 'def_pass_1st_pct', 'def_pass_sck', 'def_rush_att',
       'def_rush_rush_yds', 'def_rush_ypc', 'def_rush_td', 'def_rush_rush_1st',
       'def_rush_rush_1st_pct'], aggfunc='mean')


mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

for column in df.columns[1:-1]:
    fig, ax = plt.subplots()
    sns.boxplot(data=df, y=column, x='win_or_lose', hue="win_or_lose", ax=ax)
    ax.legend(bbox_to_anchor=(1.1, 1.05))
    plt.show()

