import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "create table users (id int, username text, password text)"
insert_row = "insert into users values (?, ?, ?)"
select_all = "select * from users"

user = (1, 'jose', 'asdf')
users = [(2, 'rolf', 'asdf'), (3, 'anne', 'xyz')]

cursor.execute(create_table)
cursor.execute(insert_row, user)
cursor.executemany(insert_row, users)
for row in cursor.execute(select_all):
    print(row)

connection.commit()
connection.close()
