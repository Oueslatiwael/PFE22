import sqlite3
from tkinter.tix import INTEGER


from faker import Faker
fake = Faker()
i = INTEGER
conn = sqlite3.connect('myDatabase.db')
cur = conn.cursor()
cur.execute('insert into persons (firstname, lastname, job, address) values (?, ?, ?, ?)',
            (fake.first_name(), fake.last_name(), fake.job(), fake.address()))
conn.commit()
