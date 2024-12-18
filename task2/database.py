import sqlite3

db = sqlite3.connect('task2.db')
cur = db.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS cats (
    id INTEGER PRIMARY KEY,
    url TEXT
)
''')


db.close()
