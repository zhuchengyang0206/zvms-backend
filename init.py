# 初始化数据库并插入一条测试数据

import database

database.init()

database.execute('''CREATE TABLE user(
                        userid INTERGER,
                        username VARCHAR(255),
                        class INTERGER,
                        permission SMALLINT,
                        password VARCHAR(255)
                     )''')
database.execute("INSERT INTO user VALUES(?,?,?,?,?)",(20200101,"admin",202001,1,"123456"))

database.execute('''CREATE TABLE student(
                        stuId INTERGER,
                        stuName VARCHAR(64),
                        volTimeInside INTERGER,
                        volTimeOutside INTERGER,
                        volTimeLarge INTERGER
                     )''')
database.execute("INSERT INTO student VALUES(?,?,?,?,?)",(20200101,"王彳亍",0,0,0))
database.execute('''CREATE TABLE volunteer(
                        volId INTERGER,
                        name VARCHAR(256),
                        time VARCHAR(256),
                        stuMax INTERGER,
                        description VARCHAR(1024),
                        status SMALLINT,
                        volTimeInside INTERGER,
                        volTimeOutside INTERGER,
                        volTimeLarge INTERGER
                     )''')
database.execute("INSERT INTO volunteer VALUES(?,?,?,?,?,?,?,?,?)",(1,"喂孔子+拜锦鲤","2020.9.24","blablablabla",0,202001,0,0,0))
database.execute('''CREATE TABLE stu_vol(
                        volId INTERGER,
                        stuId INTERGER,
                        status SMALLINT,
                        volTimeInside INTERGER,
                        volTimeOutside INTERGER,
                        volTimeLarge INTERGER
                     )''')
database.execute("INSERT INTO stu_vol VALUES(?,?,?,?,?,?)",(1,20200101,0,0,0,0))
database.execute('''CREATE TABLE class_vol(
                        volId INTERGER,
                        class INTERGER
                     )''')
database.execute("INSERT INTO class_vol VALUES(?,?)",(1,202001))
commit()
