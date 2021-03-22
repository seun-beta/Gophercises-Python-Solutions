import sqlite3
import re

connection = sqlite3.connect('db.sqlite3')
cur = connection.cursor()
number = cur.execute("SELECT number FROM phone;")
number_list = number.fetchall()

new_list = list()
for i in number_list:
    number = i[0]
    cleaned_number = re.findall("[0-9]+", str(number))
    item = ''.join(cleaned_number)
    new_list.append(item)

cur.execute("DELETE FROM phone;")
connection.commit()
for new_num in new_list:
    mobile = cur.execute("SELECT number FROM phone WHERE number=?", (new_num,))
    mobile_no = mobile.fetchone()
    if mobile_no is None:
        cur.execute("INSERT INTO phone (number) VALUES (?)", (new_num,))
        connection.commit()
    else:
        continue
        