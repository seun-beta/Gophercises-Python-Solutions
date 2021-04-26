import sqlite3
import re
from db import SeedData

seed = SeedData()


def database_connection():
    connection = sqlite3.connect(seed.database_name)
    cur = connection.cursor()
    return cur, connection


cur, connection = database_connection()
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
    print('Database is being normalized')
    if mobile_no is None:
        cur.execute("INSERT INTO phone (number) VALUES (?)", (new_num,))
        connection.commit()
    else:
        continue
