# 随手打的一个词竟然还真的有，那就用这个名吧
# 这个文件封装了一些针对数据库的操作
import database as DB

thisYear = 2020 # 以后要改成自动获取

def classIdToString(a):
    global thisYear
    id = int(a)
    _year = id // 100
    _class = id % 100
    ret = ""
    # 特殊身份的判断
    # 教师 100001 100002
    # 管理员 110001 110002
    # 系统 120003 120004
    if _year//100 == 10:
        ret = "教师"
        return ret
    elif _year//100 == 11:
        ret = "管理员"
        return ret
    elif _year//100 == 12:
        ret = "系统"
        return ret
    
    if _class <= 10:
        ret = ret + "高"
    elif _class <= 17:
        ret = ret + "蛟"
    if _year == thisYear:
        ret = ret + "一"
    elif _year == thisYear - 1:
        ret = ret + "二"
    elif _year == thisYear - 2:
        ret = ret + "三"
    ret = ret + (["NULL","1","2","3","4","5","6","7","8","9","10","NULL","2","3","4","5","6","7"])[_class] #如果我没记错的话校徽是这样的
    ret = ret + "班"

    return ret

def userLogin(userId, password):
    if isinstance(userId, str) and isinstance(password, str): # 其实传入的都是str类型
        DB.execute("SELECT * FROM user WHERE userId = %s AND password = %s;", (userId, password))
        r = DB.fetchall()
        if len(r) == 0:
            return False, {"message": "用户ID或密码错误"}
        elif len(r) > 1:
            return False, {"message": "数据库信息错误"}
        else:
            return True, r[0]
    else:
        return False, {"message": "请求接口错误"}

def classList():
    DB.execute("SELECT class FROM user WHERE userId > %s;", (thisYear * 100 - 200))
    r = DB.fetchall()
    if len(r) == 0:
        return False, {"message": "数据库信息错误"}
    else:
        lst = []
        for i in r:
            lst.append(i[0])
        return True, lst

def studentList(classId):
    if isinstance(classId, int):
        DB.execute(
            "SELECT * FROM student WHERE stuId < %d AND stuId > %d;"% # 这里是不是要 %s ?
            (classId * 100 + 100, classId * 100))
        r = DB.fetchall()
        if len(r) == 0:
            return False, {"message": "数据库信息错误"}
        else:
            return True, r
    else:
        return False, {"message": "请求接口错误"}

def volunteerList(): # 总列表
    DB.execute(
        "SELECT * FROM volunteer WHERE volId = '%s'", (volId))
    r = DB.fetchall()
    return True, r