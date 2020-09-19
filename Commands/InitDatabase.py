# 初始化数据库并插入一条测试数据

import sqlite3

conn = sqlite3.connect("./../zvms.db")
c = conn.cursor()
c.execute('''CREATE TABLE user(
                 userid INTERGER,
                 username VARCHAR(255),
                 class INTERGER,
                 permission SMALLINT,
                 password VARCHAR(255)
              )''')
c.execute("INSERT INTO user VALUES(?,?,?,?,?)",(20200101,"admin",202001,1,"123456"))
conn.commit()
c.close()
conn.close()
