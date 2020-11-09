# 初始化数据库并插入一条测试数据

import database as DB

DB.execute("DROP TABLE IF EXISTS user;")
DB.execute('''CREATE TABLE user(
                  userId INTEGER PRIMARY KEY,
                  userName CHAR(255),
                  class INTEGER,
                  permission SMALLINT,
                  password CHAR(255)
               );''')

DB.execute("DROP TABLE IF EXISTS student;")
DB.execute('''CREATE TABLE student(
                  stuId INTEGER PRIMARY KEY,
                  stuName CHAR(64),
                  volTimeInside INTEGER,
                  volTimeOutside INTEGER,
                  volTimeLarge INTEGER
               );''')

DB.execute("DROP TABLE IF EXISTS volunteer;")
DB.execute('''CREATE TABLE volunteer(
                  volId INTEGER PRIMARY KEY,
                  volName CHAR(255),
                  volDate DATE,
                  volTime TIME,
                  stuMax INTEGER,
                  nowStuCount INTEGER,
                  description TEXT,
                  status SMALLINT,
                  volTimeInside INTEGER,
                  volTimeOutside INTEGER,
                  volTimeLarge INTEGER,
                  holderId INTEGER
               );''')

DB.execute("DROP TABLE IF EXISTS stu_vol;")
DB.execute('''CREATE TABLE stu_vol(
                  volId INTEGER,
                  stuId INTEGER,
                  status SMALLINT,
                  volTimeInside INTEGER,
                  volTimeOutside INTEGER,
                  volTimeLarge INTEGER
               );''')

DB.execute("DROP TABLE IF EXISTS class_vol;")
DB.execute('''CREATE TABLE class_vol(
                  volId INTEGER,
                  class INTEGER,
                  stuMax INTEGER
               );''')


               
# DB.execute('''INSERT INTO user(userId, userName, class, permission, password)
#               VALUES(%d, %s, %d, %d, %s);''',
#               (20200101, "admin", 202001, 2, "e10adc3949ba59abbe56e057f20f883e"))

# DB.execute('''INSERT INTO student(stuId, stuName, volTimeInside, volTimeOutside, volTimeLarge)
#               VALUES(%d, %s, %d, %d, %d);''',
#               (20200101, "王彳亍", 0, 0, 0))

# DB.execute('''INSERT INTO volunteer(volId, volName, volDate, volTime, stuMax, nowStuCount, description, status, volTimeInside, volTimeOutside, volTimeLarge, holderId)
#               VALUES(%d, %s, %s, %s, %d, %d, %s, %d, %d, %d, %d);''',
#               (1, "喂孔子+拜锦鲤", "2020.9.24", "13:00", 10, 0, "blablablabla", 0, 1, 0, 202001))

# DB.execute('''INSERT INTO stu_vol(volId, stuId, status, volTimeInside, volTimeOutside, volTimeLarge)
#               VALUES(%d, %d, %d, %d, %d, %d);''',
#               (1, 20200101, 0, 0, 0, 0))

# DB.execute('''INSERT INTO class_vol(volId, class, stuMax)
#               VALUES(%d, %d, %d);''',
#               (1, 202001, 10))

DB.commit()