import sqlite3
import re

connection = sqlite3.connect('db.sqlite3')
cur = connection.cursor()
a = cur.execute("SELECT number FROM phone;")
e = a.fetchall()

new_ls = list()
for i in e:
    j = i[0]
    new = re.findall("[0-9]+", str(j))
    item = ''.join(new)
    print(item)
    new_ls.append(item)
print(new_ls)

cur.execute("DELETE FROM phone;")
connection.commit()
for new_num in new_ls:
    f = cur.execute("SELECT number FROM phone WHERE number=?", (new_num,))
    g = f.fetchone()
    if g is None:
        cur.execute("INSERT INTO phone (number) VALUES (?)", (new_num,))
        connection.commit()
    else:
        continue
        
    
    
    
