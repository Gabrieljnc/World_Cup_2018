import requests
from pandas import json_normalize


class ExtractMatches:
    def __init__(self,competition_id, season_id):
        self.competition_id = competition_id
        self.season_id = season_id

    def extracting_raw_data(self):
        read_matches = requests.get('https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches/'+str(self.competition_id)+'/'+ str(self.season_id)+'.json')
        matches = read_matches.json()
        matches_df_raw = json_normalize(matches, sep = '_')
        return matches_df_raw

    def matches_list(self): # Formating data to put on Postgree DB
        matches_df = self.extracting_raw_data()
        
        id_manager_home = []
        full_name_home = []
        nick_name_home = []
        dob_home = []

        id_manager_away = []
        full_name_away = []
        nick_name_away = []
        dob_away = []

        for i in range(64):
            id_manager_away.append((list(matches_df['home_team_managers'][i][0].values())[0]))
            full_name_away.append((list(matches_df['home_team_managers'][i][0].values())[1]))
            nick_name_away.append((list(matches_df['home_team_managers'][i][0].values())[2]))
            dob_away.append((list(matches_df['home_team_managers'][i][0].values())[3]))
            
        for i in range(64):
            id_manager_home.append((list(matches_df['away_team_managers'][i][0].values())[0]))
            full_name_home.append((list(matches_df['away_team_managers'][i][0].values())[1]))
            nick_name_home.append((list(matches_df['away_team_managers'][i][0].values())[2]))
            dob_home.append((list(matches_df['away_team_managers'][i][0].values())[3]))
            
        matches_df['id_home_team_managers'] = id_manager_home
        matches_df['full_name_home_team_managers'] = full_name_home
        matches_df['nickname_home_team_managers'] = nick_name_home
        matches_df['dob_home_team_managers'] = dob_home

        matches_df['id_away_team_managers'] = id_manager_away
        matches_df['full_name_away_team_managers'] = full_name_away
        matches_df['nickname_away_team_managers'] = nick_name_away
        matches_df['dob_away_team_managers'] = dob_away

        matches_df.drop(columns=['home_team_managers', 'away_team_managers'], inplace = True)
        
        return matches_df






