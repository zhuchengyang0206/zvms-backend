# https://blog.csdn.net/GuoQiZhang/article/details/91344509
import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute('''CREATE TABLE user(
                 id INTERGER,
                 username VARCHAR(255),
                 password VARCHAR(255),
                 class INTERGER,
                 permission SMALLINT
              )''')
c.execute("INSERT INTO user VALUES(?,?,?,?,?)",(0,"asdasdasd","asdasdasd",202001,1))
conn.commit()
c.close()
conn.close()
