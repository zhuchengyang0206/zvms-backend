# 初始化数据库并插入一条测试数据

import database as DB

# 数据库中所有条目都使用3个小写英文字母缩写（原来的实在太长了），意义见DATABASE.md

DB.execute('''CREATE TABLE user(
                  uid INTEGER,
                  unm CHAR(255),
                  cls INTEGER,
                  pms SMALLINT,
                  pwd CHAR(255)
               );''')
DB.execute("INSERT INTO user(uid,unm,cls,pms,pwd) VALUES(%s,'%s',%s,%s,'%s');"%(20200101,"admin",202001,1,"e10adc3949ba59abbe56e057f20f883e"))

DB.execute('''CREATE TABLE student(
                  sid INTEGER,
                  snm CHAR(64),
                  vti INTEGER,
                  vto INTEGER,
                  vtl INTEGER
               );''')
DB.execute("INSERT INTO student(sid,snm,vti,vto,vtl) VALUES(%s,'%s',%s,%s,%s);"%(20200101,"王彳亍",0,0,0))

DB.execute('''CREATE TABLE volunteer(
                  vid INTEGER,
                  vnm CHAR(256),
                  vtm CHAR(256),
                  smx INTEGER,
                  dsc CHAR(1024),
                  stt SMALLINT,
                  vti INTEGER,
                  vto INTEGER,
                  vtl INTEGER
               );''')
DB.execute("INSERT INTO volunteer(vid,vnm,vtm,smx,des,stt,vti,vto,vtl) VALUES(%s,'%s','%s','%s',%s,%s,%s,%s,%s);"%(1,"喂孔子+拜锦鲤","2020.9.24","blablablabla",0,202001,0,0,0))

DB.execute('''CREATE TABLE stu_vol(
                  vid INTEGER,
                  sid INTEGER,
                  stt SMALLINT,
                  vti INTEGER,
                  vto INTEGER,
                  vtl INTEGER
               );''')
DB.execute("INSERT INTO stu_vol(vid,sid,stt,vti,vto,vtl) VALUES(%s,%s,%s,%s,%s,%s);"%(1,20200101,0,0,0,0))

DB.execute('''CREATE TABLE class_vol(
                  vid INTEGER,
                  cls INTEGER
               );''')

DB.execute("INSERT INTO class_vol(vid,cls) VALUES(%s,%s);"%(1,202001))

DB.commit()