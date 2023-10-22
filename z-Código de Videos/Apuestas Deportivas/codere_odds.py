# -*- coding: utf-8 -*-
"""
Video: Apuestas deportivas
Autor: Guillermo Izquierdo
"""
import pandas as pd

odds_raw = pd.read_html('https://apuestas.codere.mx/es_MX/futbol-americano')[0]

odds_raw['team'] = odds_raw['Unnamed: 5'].apply(lambda x: x.split(' ')[1])
odds_raw['ganador_derecha'] = odds_raw['Ganador del Partido'].apply(lambda x: float(x.split(' ')[1]))
odds_raw['proba_implicita'] = odds_raw['ganador_derecha'].apply(lambda x: 1/x)
