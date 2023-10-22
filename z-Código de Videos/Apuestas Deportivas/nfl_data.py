# -*- coding: utf-8 -*-
"""
Video: Apuestas deportivas
Autor: Guillermo Izquierdo

"""

import pandas as pd


def clean_column_name(x):
    y = x.split(' ')
    z = y[0]
    return z


def apply_clean(df):
    df['Team'] = df['Team'].apply(lambda x: clean_column_name(x))
    df.set_index('Team', inplace=True)
    return df


def clean_col_names(x,prefix):
    x = x.lower()
    x = x.replace(' ','_')
    x = x.replace('%','_pct')
    x = x.replace('/','_per_')
    x = x.replace('+','_plus')
    x = x.replace('__','_')

    return prefix + x


def make_stats_per_game(df_,week_number):
    
    df = df_.copy()
    
    for col in df.columns:
        if 'ypc' in col:
            pass
        elif 'rate' in col:
            pass
        elif 'pct' in col:
            pass
        elif 'per_att' in col:
            pass
        elif 'lng' in col:
            df[col] = df[col].str.replace('T','')
            df[col] = df[col].astype(float)
        else:
            df[col] = df[col] / week_number
    
    return df



WEEK = 4

passing_yards = pd.read_html('https://www.nfl.com/stats/player-stats/category/passing/2023/reg/all/passingyards/desc')[0]
running_yards = pd.read_html('https://www.nfl.com/stats/player-stats/category/rushing/2023/reg/all/rushingyards/desc')[0]
receiving_yards = pd.read_html('https://www.nfl.com/stats/player-stats/category/receiving/2023/reg/all/receivingreceptions/desc')[0]


###
# Offensive
###

o_t_pass_ = pd.read_html('https://www.nfl.com/stats/team-stats/offense/passing/2023/reg/all')[0]
o_t_rush_ = pd.read_html('https://www.nfl.com/stats/team-stats/offense/rushing/2023/reg/all')[0]
o_t_rec_ = pd.read_html('https://www.nfl.com/stats/team-stats/offense/receiving/2023/reg/all')[0]
o_t_score_ = pd.read_html('https://www.nfl.com/stats/team-stats/offense/scoring/2023/reg/all')[0]
o_t_downs_ = pd.read_html('https://www.nfl.com/stats/team-stats/offense/downs/2023/reg/all')[0]

###
# Offensive
###

d_t_pass_ = pd.read_html('https://www.nfl.com/stats/team-stats/defense/passing/2023/reg/all')[0]
d_t_rush_ = pd.read_html('https://www.nfl.com/stats/team-stats/defense/rushing/2023/reg/all')[0]
d_t_score_ = pd.read_html('https://www.nfl.com/stats/team-stats/defense/scoring/2023/reg/all')[0]
d_t_fumbles_ = pd.read_html('https://www.nfl.com/stats/team-stats/defense/fumbles/2023/reg/all')[0]
d_t_inter_ = pd.read_html('https://www.nfl.com/stats/team-stats/defense/interceptions/2023/reg/all')[0]
d_t_downs_ = pd.read_html('https://www.nfl.com/stats/team-stats/defense/downs/2023/reg/all')[0]


########
### Clean data
########

team_offense_= [o_t_pass_, o_t_rush_, o_t_rec_, o_t_downs_]
team_defense_ = [d_t_pass_, d_t_rush_, d_t_score_, d_t_inter_, d_t_downs_]

team_offense_stats = [apply_clean(df) for df in team_offense_]
team_defense_stats = [apply_clean(df) for df in team_defense_]

o_t_pass,o_t_rush,o_t_rec,o_t_downs = team_offense_stats
d_t_pass,d_t_rush,d_t_score,d_t_inter,d_t_downs = team_defense_stats

cols_ot_pass = o_t_pass.columns
cols_ot_rush = o_t_rush.columns
cols_dt_pass = d_t_pass.columns
cols_dt_rush = d_t_rush.columns

clean_cols_ot_pass = [clean_col_names(col,'off_pass_') for col in cols_ot_pass]
clean_cols_ot_rush = [clean_col_names(col,'off_rush_') for col in cols_ot_rush]
clean_cols_dt_pass = [clean_col_names(col,'def_pass_') for col in cols_dt_pass]
clean_cols_dt_rush = [clean_col_names(col,'def_rush_') for col in cols_dt_rush]

o_t_pass.columns = clean_cols_ot_pass
o_t_rush.columns = clean_cols_ot_rush
d_t_pass.columns = clean_cols_dt_pass
d_t_rush.columns = clean_cols_dt_rush


df_ot_pass = make_stats_per_game(o_t_pass, WEEK)
df_ot_rush = make_stats_per_game(o_t_rush, WEEK)
df_dt_pass = make_stats_per_game(d_t_pass, WEEK)
df_dt_rush = make_stats_per_game(d_t_rush, WEEK)




#####
### Hipotesis 1
### Balance de yardas y puntos, anotados y permitidos

# offensive_side_cols = ['']
# o_t_pass.loc[teams]

##########
### Crear calendario de la semana
### para iterar en los partidos y generar los sets
#########

calendario = pd.read_html('https://www.espn.com.mx/futbol-americano/nfl/calendario/_/semana/5/ano/2023/tipodetemporada/2')
cal_merge = pd.concat([calendario[0][['PARTIDO','PARTIDO.1']],calendario[1][['PARTIDO','PARTIDO.1']],calendario[2][['PARTIDO','PARTIDO.1']]],axis=0).reset_index(drop=True)
cal_merge.columns = ['visitante','local']
cal_merge['local'] = cal_merge['local'].apply(lambda x: x.replace('en ',''))


team_map = {'Tennessee':'Titans','Atlanta':'Falcons','New Orleans':'Saints','Denver':'Broncos',
            'New England':'Patriots','Buffalo':'Bills','Houston':'Texans','Indianapolis':'Colts',
            'Carolina':'Panthers','Chicago':'Bears','Dallas':'Cowboys','Pittsburgh':'Steelers','Philadelphia':'Eagles',
            'San Francisco':'49ers','Cleveland':'Browns','Detroit':'Lions','Greenbay':'Packers','Miami':'Dolphins',
            'Minnesota':'Vikings','Washington':'Commanders','Jacksonville':'Jaguars','Baltimore':'Ravens','Seattle':'Seahawks',
            'Kansas City':'Chiefs','Arizona':'Cardinals','Las Vegas':'Raiders','Tampa Bay':'Buccaneers','Cincinnati':'Bengals'}


cal_merge['local'] = cal_merge['local'].map(team_map)
cal_merge['visitante'] = cal_merge['visitante'].map(team_map)
cal_merge.to_csv(f'./data/calendario_semana_{WEEK + 1}.csv', index=False)

##########
#### SEMANA X+1 por llenar
#### 1era etapa
#### Crear una lista de escenarios con partidos para rellenar después del partido
##########

def create_record(TEAMS, df_ot_pass,df_ot_rush,df_dt_pass, df_dt_rush):
    record_a = pd.concat([df_ot_pass.loc[TEAMS[0]],df_ot_rush.loc[TEAMS[0]],df_dt_pass.loc[TEAMS[1]],df_dt_rush.loc[TEAMS[1]]])
    record_b = pd.concat([df_ot_pass.loc[TEAMS[1]],df_ot_rush.loc[TEAMS[1]],df_dt_pass.loc[TEAMS[0]],df_dt_rush.loc[TEAMS[0]]])
    record_set = pd.concat([record_a,record_b],axis=1).T
    return record_set


df_week_calendar = pd.read_csv(f'./data/calendario_semana_{WEEK + 1}_mod.csv')

week_games = []
match_key = []
for idx, row in df_week_calendar.iterrows():
    tmp = create_record([row['visitante'],row['local']], df_ot_pass,df_ot_rush,df_dt_pass, df_dt_rush)
    week_games.append(tmp)
    match_key.append(str(row['visitante']) + '_' + str(row['local']))
    match_key.append(str(row['local']) + '_' + str(row['visitante']))

    
df_games = pd.concat(week_games)
df_games['match_key'] = match_key
df_games.set_index('match_key',inplace=True)
df_games.to_csv(f'./data/pre_game_{WEEK + 1}.csv')


