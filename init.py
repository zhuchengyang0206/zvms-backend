# 初始化数据库并插入一条测试数据

import database as DB

DB.execute("DROP TABLE IF EXISTS user;")

DB.execute('''CREATE TABLE user(
                  uid INTEGER,
                  unm CHAR(255),
                  cls INTEGER,
                  pms SMALLINT,
                  pwd CHAR(255)
               );''')
DB.execute("INSERT INTO user(uid,unm,cls,pms,pwd) VALUES(%d,'%s',%d,%d,'%s');"%(20200101,"admin",202001,2,"e10adc3949ba59abbe56e057f20f883e"))

DB.execute("DROP TABLE IF EXISTS student;")

DB.execute('''CREATE TABLE student(
                  sid INTEGER,
                  snm CHAR(64),
                  vti INTEGER,
                  vto INTEGER,
                  vtl INTEGER
               );''')
DB.execute("INSERT INTO student(sid,snm,vti,vto,vtl) VALUES(%d,'%s',%d,%d,%d);"%(20200101,"王彳亍",0,0,0))

DB.execute("DROP TABLE IF EXISTS volunteer;")

DB.execute('''CREATE TABLE volunteer(
                  vid INTEGER,
                  vnm CHAR(256),
                  vdt CHAR(256),
                  vtm CHAR(256),
                  smx INTEGER,
                  nst INTEGER,
                  dsc CHAR(1024),
                  stt SMALLINT,
                  vti INTEGER,
                  vto INTEGER,
                  vtl INTEGER,
                  hid INTEGER
               );''')
DB.execute("INSERT INTO volunteer(vid,vnm,vdt,vtm,smx,nst,dsc,stt,vti,vto,vtl,hid) VALUES(%d,'%s','%s','%s',%d,'%s',%d,%d,%d,%d,%d);"%(1,"喂孔子+拜锦鲤","2020.9.24","13:00",10,0,"blablablabla",0,0,0,0,202001))

DB.execute("DROP TABLE IF EXISTS stu_vol;")

DB.execute('''CREATE TABLE stu_vol(
                  vid INTEGER,
                  sid INTEGER,
                  stt SMALLINT,
                  vti INTEGER,
                  vto INTEGER,
                  vtl INTEGER
               );''')
DB.execute("INSERT INTO stu_vol(vid,sid,stt,vti,vto,vtl) VALUES(%d,%d,%d,%d,%d,%d);"%(1,20200101,0,0,0,0))

DB.execute("DROP TABLE IF EXISTS class_vol;")

DB.execute('''CREATE TABLE class_vol(
                  vid INTEGER,
                  cls INTEGER,
                  smx INTEGER
               );''')

DB.execute("INSERT INTO class_vol(vid,cls) VALUES(%d,%d,%d);"%(1,202001,10))

DB.commit()