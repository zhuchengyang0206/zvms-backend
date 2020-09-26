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

c.execute('''CREATE TABLE student(
                 stuId INTERGER,
                 stuName VARCHAR(64),
                 volTimeInside INTERGER,
                 volTimeOutside INTERGER,
                 volTimeLarge INTERGER
              )''')
c.execute("INSERT INTO student VALUES(?,?,?,?,?)",(20200101,"王彳亍",0,0,0))

c.execute('''CREATE TABLE volunteer(
                 volId INTERGER,
                 name VARCHAR(256),
                 time VARCHAR(256),
                 volTimeInside INTERGER,
                 volTimeOutside INTERGER,
                 volTimeLarge INTERGER
              )''')
c.execute("INSERT INTO volunteer VALUES(?,?,?,?,?,?)",(1,"喂孔子+拜锦鲤","2020.9.24",0,0,0))

conn.commit()
c.close()
conn.close()
