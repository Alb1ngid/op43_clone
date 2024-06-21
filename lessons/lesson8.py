# логические операторы\ методы jоin\foregin key, связи таблиц


import sqlite3

with sqlite3.connect('user.db') as con:
    cur=con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INT DEFAULT 0
    )
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users (id)
    )
    
    ''')


    # cur.execute('''
    # INSERT INTO users (name,age) VALUES ('beka',20),
    # ('alisa',19),('alan',60),('jhin',44)
    # ''')
    # cur.execute('''DELETE FROM users WHERE id=1''')
    cur.execute('''SELECT * FROM users''')
    # for i in cur.fetchall():
    #     print(i)
    # #
    # cur.execute('''
    # insert into orders(user_id, product) VALUES
    # (1,'комп'),(1,'мышка'),(2,'чайник'),(3,'воду'),(4,'машину')
    # ''')
    print('')
    cur.execute('''SELECT * FROM orders''')

    # for i in cur.fetchall():
    #     print(i)

    cur.execute('''SELECT users.name,orders.product
    FROM users
     JOIN orders ON users.id = orders.user_id 
    
    ''')

    # print('')
    # for i in cur.fetchall():
    #     print(i)

    cur.execute('''SELECT * FROM users WHERE name LIKE "a%" ''')
    print('')
    # for i in cur.fetchall():
    #     print(i)

