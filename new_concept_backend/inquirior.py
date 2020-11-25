# 负责对数据库的直接数据查询，不报错
import database as DB

# TABLE user
def user_getAll():
    DB.execute("SELECT * FROM user")
    return DB.fetchall()

def user_getById(uid):
    DB.execute("SELECT * FROM user where userId = %s;", (uid))
    return DB.fetchone()

def user_modifyById(uid, userName, _class, permission, password):
    DB.execute("UPDATE user SET userName = %s, class = %s, permission = %s, password = %s wHERE userId = %s;", (userName, _class, permission, password, uid))

def user_insert(uid, userName, _class, permission, password):
    DB.execute("INSERT INTO user (userId, userName, class, permission, password) VALUES (%s, %s, %s, %s, %s);", (uid, userName, _class, permission, password))

# TABLE student
def student_getAll():
    DB.execute("SELECT * FROM student;")
    return DB.fetchall()

def student_getById(sid):
    DB.execute("SELECT * FROM student WHERE stuid = %s;", (sid))
    return DB.fetchone()

def student_modifyById(sid, stuName, volIn, volOut, VolLarge):
    DB.execute("UPDATE student SET stuName = %s, volTimeInside = %s, volTimeOutside = %s, volTimeLarge = %s WHERE stuId = %s;", (stuName, volIn, volOut, VolLarge, sid))

def student_insert(sid, stuName, volIn, volOut, VolLarge):
    DB.execute("INSERT INTO student (stuId, stuName, volTimeInside, volTimeOutside, volTimeLarge) VALUES (%s, %s, %s, %s, %s)", (sid, stuName, volIn, volOut, VolLarge))

# TABLE volunteer
def volunteer_getAll()
    DB.execute("SELECT * FROM volunteer;")
    return DB.fetchall()

def volunteer_getById(vid):
    DB.execute("SELECT * FROM volunteer WHERE volId = %s;", (vid))
    return DB.fetchone()

def volunteer_modifyById(volId, volName, volDate, volTime, stuMax, nowStuCount, description, status, volIn, volOut, volLarge, holderId):
    DB.execute("UPDATE volunteer SET volName = %s, volDate = %s, volTime = %s, stuMax = %s, nowStuCount = %s, description = %s, status = %s, volTimeInside = %s, volTimeOutside = %s, volTimeLarge = %s, holderId = %s WHERE volId = %s;", (volName, volDate, volTime, stuMax, nowStuCount, description, status, volIn, volOut, volLarge, holderId, volId))

def volunteer_insert(volId, volName, volDate, volTime, stuMax, nowStuCount, description, status, volIn, volOut, volLarge, holderId):
    DB.execute("INSERT INTO student (volName, volDate, volTime, stuMax, nowStuCount, description, status, volTimeInside, volTimeOutside, volTimeLarge, holderId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (volId, volName, volDate, volTime, stuMax, nowStuCount, description, status, volIn, volOut, volLarge, holderId))

# TABLE stu_vol
def stu_vol_getAll():
    DB.execute("SELECT * FROM stu_vol;")
    return DB.fetchall()
