import sqlite3

import pandas as pd

fname = './data/Данные поставщика.xlsx'
xlsx = pd.read_excel(fname)
cleaned = xlsx[['Название', "Раздел", "Код артикула"]]
cleaned['Название'] = xlsx['Название'] + ' ' + xlsx["Код артикула"]
cleaned.drop('Код артикула')
db = sqlite3.connect('task1.db')
cleaned.to_sql("Данные поставщика", db)
db.close()
# xlsx.to_csv('temp.csv') # это был единственный способ открыть его в нормальном виде
# xlsx.dropna(how='all', axis=1, inplace=True)
# print(xlsx.tail(150))
