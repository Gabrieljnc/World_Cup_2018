import extract_competitions  
import extract_matches  
import extract_events 

import psycopg2
from sqlalchemy import create_engine

competitions_to_db = extract_competitions.ExtractCompetitions().competitions_list()
matches_to_db = extract_matches.ExtractMatches(43,3).matches_list()

conn_string = 'postgresql://1922120013_TCC_Gabriel:1922120013_TCC_Gabriel@3.133.102.60/IESB_Soccer_Performance'

db = create_engine(conn_string)
conn = db.connect()

for event in range(len(extract_events.frames)):
    events_to_db = extract_events.frames[event]
    events_to_db.to_sql('Match_0'+str(event), con=conn, if_exists='replace',index=False)


competitions_to_db.to_sql('All_competitions', con=conn, if_exists='replace',index=False)
matches_to_db.to_sql('All_matches', con=conn, if_exists='replace',index=False)


conn = psycopg2.connect(conn_string)

conn.autocommit = True
cursor = conn.cursor()
  
# conn.commit()
conn.close()


