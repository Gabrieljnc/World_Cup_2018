from Modules import extract_competitions
from Modules import extract_matches

import psycopg2
from sqlalchemy import create_engine

competitions_to_db = extract_competitions.ExtractCompetitions().competitions_list()
matches_to_db = extract_matches.ExtractMatches(43,3).matches_list()

conn_string = '####'

db = create_engine(conn_string)
conn = db.connect()

competitions_to_db.to_sql('competitions', con=conn, if_exists='replace',index=False)
matches_to_db.to_sql('matches', con=conn, if_exists='replace',index=False)

conn = psycopg2.connect(conn_string)

conn.autocommit = True
cursor = conn.cursor()
  
# conn.commit()
conn.close()

