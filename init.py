# 初始化数据库并插入一条测试数据

import sqlite3
import database

DB.execute('''CREATE TABLE user(
                  userid INTERGER,
                  username VARCHAR(255),
                  class INTERGER,
                  permission SMALLINT,
                  password VARCHAR(255)
               )''')
DB.execute("INSERT INTO user VALUES(?,?,?,?,?)",(20200101,"admin",202001,1,"123456"))

DB.execute('''CREATE TABLE student(
                  stuId INTERGER,
                  stuName VARCHAR(64),
                  volTimeInside INTERGER,
                  volTimeOutside INTERGER,
                  volTimeLarge INTERGER
               )''')
DB.execute("INSERT INTO student VALUES(?,?,?,?,?)",(20200101,"王彳亍",0,0,0))

DB.execute('''CREATE TABLE volunteer(
                  volId INTERGER,
                  name VARCHAR(256),
                  time VARCHAR(256),
                  description VARCHAR(1024),
                  status SMALLINT,
                  class INTERGER,
                  volTimeInside INTERGER,
                  volTimeOutside INTERGER,
                  volTimeLarge INTERGER
               )''')
DB.execute("INSERT INTO volunteer VALUES(?,?,?,?,?,?,?,?,?)",(1,"喂孔子+拜锦鲤","2020.9.24","blablablabla",0,202001,0,0,0))

DB.execute('''CREATE TABLE stu_vol(
                  volId INTERGER,
                  stuId INTERGER,
                  status SMALLINT,
                  volTimeInside INTERGER,
                  volTimeOutside INTERGER,
                  volTimeLarge INTERGER
               )''')
DB.execute("INSERT INTO stu_vol VALUES(?,?,?,?,?,?)",(1,20200101,0,0,0,0))

DB.commit()
