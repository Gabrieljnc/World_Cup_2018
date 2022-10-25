import requests
from pandas import json_normalize

class ExtractEvents:
    def __init__(self,match_id):
        self.match_id = match_id

    def list_events(self):
        read_events = requests.get("https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/"+str(self.match_id)+'.json')       
        events = read_events.json() 
        events_df = json_normalize(events, sep = '_')

        return events_df
