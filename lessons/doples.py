import sqlite3

conn = sqlite3.connect('user.db')
cur = conn.cursor()

cur.execute('''
   SELECT users.id,users.name,users.age,orders.product 
   FROM users
   INNER JOIN orders ON users.id = orders.user_id
   ''')
rows = cur.fetchall()
for row in rows:
    print('inner', row)

cur.execute('''
SELECT users.id,users.name,users.age,orders.product
FROM users
LEFT JOIN orders ON users.id = orders.user_id
''')

rowss = cur.fetchall()
for row in rowss:
    print('left', row)
