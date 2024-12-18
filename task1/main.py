import pandas as pd
import sqlite3
import os
db = sqlite3.connect('task1.db')
for file in os.listdir('./data')[1:]:
    dfs = pd.read_excel(f'./data/{file}', sheet_name=None)
    for table, df in dfs.items():
        df.to_sql(file.removesuffix('.xlsx'), db)
db.close()