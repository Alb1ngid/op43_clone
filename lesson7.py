# БАЗА ДАННЫХ
# crud - create read update delete
# SQL noSQL
# СУБД -система управления базами данных
# relation

import sqlite3

db = sqlite3.connect('group43.db')

cursor = db.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    name VARCHAR(100) NOT NULL,
    age DATE DEFAULT 0,
    password TEXT
)''')

# create
# cursor.execute('''INSERT INTO users(name,age,password)
#                             VALUES ('beka2',20,'qwerty')  ''')
#
# cursor.execute('''INSERT INTO users(name,age,password)
#                             VALUES ('bek32',30,'3214rfqwerty')  ''')
#
# cursor.execute('''INSERT INTO users(name,age,password)
#                             VALUES ('beka2',200,'qwerty3rfd')  ''')
#
# cursor.execute('''INSERT INTO users(name,age,password)
#                             VALUES ('bewqrfrvdc',20,'qwerty')  ''')


# UPDATE
cursor.execute('''UPDATE users SET name="крутой прогер",age=11  WHERE rowid %2 ''')

# DELETE
cursor.execute(''' DELETE FROM users WHERE password ''')


#read
# SELECT\fetch
cursor.execute('''SELECT rowid,* FROM users ''')
for row in cursor.fetchall():
    print(row)

db.commit()
db.close()