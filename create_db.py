import sqlite3

def create_database():
    with open('SQLs/university_data.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('university_data.db') as con:
        cur = con.cursor()
        cur.executescript(sql)
