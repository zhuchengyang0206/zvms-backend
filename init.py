# 初始化数据库并插入一条测试数据

import database as DB

DB.execute("DROP TABLE IF EXISTS user;")

DB.execute('''CREATE TABLE user(
                  userId INTEGER,
                  userName CHAR(255),
                  class INTEGER,
                  permission SMALLINT,
                  password CHAR(255)
               );''')
DB.execute_param('''INSERT INTO user(userId, userName, class, permission, password)
                    VALUES(?, '?', ?, ?, '?');''',
                    (20200101, "admin", 202001, 2, "e10adc3949ba59abbe56e057f20f883e"))

DB.execute("DROP TABLE IF EXISTS student;")

DB.execute('''CREATE TABLE student(
                  stuId INTEGER,
                  stuName CHAR(64),
                  volTimeInside INTEGER,
                  volTimeOutside INTEGER,
                  volTimeLarge INTEGER
               );''')
DB.execute_param('''INSERT INTO student(stuId, stuName, volTimeInside, volTimeOutside, volTimeLarge)
                    VALUES(?, '?', ?, ?, ?);''',
                    (20200101, "王彳亍", 0, 0, 0))

DB.execute("DROP TABLE IF EXISTS volunteer;")

DB.execute('''CREATE TABLE volunteer(
                  volId INTEGER,
                  volName CHAR(256),
                  volDate CHAR(256),
                  volTime CHAR(256),
                  stuMax INTEGER,
                  nowStuCount INTEGER,
                  description CHAR(1024),
                  status SMALLINT,
                  volTimeInside INTEGER,
                  volTimeOutside INTEGER,
                  volTimeLarge INTEGER,
                  holderId INTEGER
               );''')
DB.execute_param('''INSERT INTO volunteer(volId, volName, volDate, volTime, stuMax, nowStuCount, description, status, volTimeInside, volTimeOutside, volTimeLarge, holderId)
                    VALUES(?, '?', '?', '?', ?, '?', ?, ?, ?, ?, ?);''',
                    (1, "喂孔子+拜锦鲤", "2020.9.24", "13:00", 10, 0, "blablablabla", 0, 0, 0, 0, 202001))

DB.execute("DROP TABLE IF EXISTS stu_vol;")

DB.execute('''CREATE TABLE stu_vol(
                  volId INTEGER,
                  stuId INTEGER,
                  status SMALLINT,
                  volTimeInside INTEGER,
                  volTimeOutside INTEGER,
                  volTimeLarge INTEGER
               );''')
DB.execute_param('''INSERT INTO stu_vol(volId, stuId, status, volTimeInside, volTimeOutside, volTimeLarge)
                    VALUES(?, ?, ?, ?, ?, ?);''',
                    (1, 20200101, 0, 0, 0, 0))

DB.execute("DROP TABLE IF EXISTS class_vol;")

DB.execute('''CREATE TABLE class_vol(
                  volId INTEGER,
                  class INTEGER,
                  stuMax INTEGER
               );''')

DB.execute_param('''INSERT INTO class_vol(volId, class, stuMax)
                    VALUES(?, ?, ?);''',
                    (1, 202001, 10))

DB.commit()