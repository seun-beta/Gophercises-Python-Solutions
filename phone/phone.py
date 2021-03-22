import sqlite3
import re

connection = sqlite3.connect('db.sqlite3')
cur = connection.cursor()

a = cur.execute("SELECT number from phone;")
for i in a.fetchall():
    print(i)
    new = re.findall("[0-9]", str(i))
