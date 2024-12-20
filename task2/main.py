import sqlite3

import requests

API_KEY = 'live_70wX1DDUfbxnXFklS5Xm9N7Yo3Z7aQ0u3Fh08XhNB87BorGWE1Lko1YHHMVDOD3h'
ENDP = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(ENDP, {'limit': 10})
connect = sqlite3.connect('task2.db')
cursor = connect.cursor()
try:
    for entry in response.json():
        cursor.execute('''INSERT INTO cats (url) VALUES (?)''', (entry['url'],))
    connect.commit()
except sqlite3.Error:
    connect.rollback()

connect.close()
