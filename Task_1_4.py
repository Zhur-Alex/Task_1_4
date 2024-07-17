import pandas as pd
from sqlalchemy import create_engine,text

engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres')
connection = engine.connect()
df = pd.read_sql_query('''select * from minmax_creditdebet('2018-01-09')''', con = engine)
df.to_csv('C:/Users/Александр/Desktop/1.csv', index=False)
