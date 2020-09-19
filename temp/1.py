# https://blog.csdn.net/GuoQiZhang/article/details/91344509
import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute('''CREATE TABLE user(
                 id INTERGER PRIMARY KEY,
                 name VARCHAR(255),
                 grade INTERGER,
                 class INTERGER,
                 volTime DECIMAL
              )''')
conn.commit()
c.close()
conn.close()
