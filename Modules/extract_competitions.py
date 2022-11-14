import pandas as pd
import requests

from pandas import json_normalize


class ExtractCompetitions:
    def competitions_list(self):
        competitions = requests.get('https://raw.githubusercontent.com/statsbomb/open-data/master/data/competitions.json')
        competitions = competitions.json()
        competition_name = []
        season_name = []
        competition_id = []
        season_id = []

        for competition in competitions:
            competition_name.append(competition['competition_name'])
            season_name.append(competition['season_name'])
            competition_id.append(competition['competition_id'])
            season_id.append(competition['season_id'])

        competition_df = pd.DataFrame(list(zip(competition_name,season_name,competition_id,season_id)), columns=['Nome da Competição', 'Temporada', 'ID da Competição', 'ID da Temporada'])

        return competition_df
