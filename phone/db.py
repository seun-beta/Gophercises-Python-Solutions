import sqlite3


class SeedData():
    
    database_name = "db.sqlite3"
    connection = sqlite3.connect(database_name)
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS phone;")
    cur.execute("""CREATE TABLE phone (Id INTEGER PRIMARY KEY,
                number varchar(100) NOT NULL);""")

    seed_list = ['1234567890', '123 456 7891', '(123) 456 7892',
                 '(123) 456-7893', '123-456-7894', '123-456-7890',
                 '1234567892', '(123)456-7892']

    for raw_number in seed_list:
        print(raw_number)
        cur.execute("""INSERT INTO phone (number) VALUES (?)""", (raw_number,))
        connection.commit()

    cur.close()
