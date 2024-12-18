import sqlite3

conn = sqlite3.connect('task1.db')
cur = conn.cursor()

get_sub_categories_count =\
'''SELECT DISTINCT  "Главная категория",COUNT("Дочерняя категория") FROM "Дерево категорий"
GROUP BY "Главная категория";'''


def execute(statement):
    res = cur.execute(statement)
    return list(res)


conn.close()