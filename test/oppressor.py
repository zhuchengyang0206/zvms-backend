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
    
def select(col,src,exp,val,ret,only=True):
    # col:选择的列，字符串 src:从哪张表，字符串 exp:条件，字符串
    # val:传入的数据，元组 ret:返回的格式，列表，内容为字符串，为[]则为col
    # only:是否只取一个
    # 返回值:一个布尔值、一个字典，格式由ret决定（若only=False则为一个数组）
    s="SELECT %s FROM %s WHERE %s;"%(col,src,exp)
    DB.execute(s,val)
    r=DB.fetchall()
    if ret==[]:
        ret=list(split(col,","))
        for i in len(ret): ret[i]=ret[i].strip()
    if len(r)==0: return False, {"message": "数据库信息错误：未查询到相关信息"}
    if len(r)==1:
        ret={}
        for j in range(0,len(val)):
            ret.update({val[j]: r[0][j]})
        if only: return True, ret
        else: return True, [ret]
    else:
        if only: return False, {"message": "数据库信息错误：要求一个但查询到多个"}
        ret=[]
        for i in range(0,len(r)):
            for j in range(0,len(val)):
                ret[i].update({val[j]: r[i][j]})
        return True, ret

def update(col,src,exp,val):
    s="UPDATE %s SET %s WHERE %s;"%(src,col,exp)
    DB.execute(s,val)
    r=DB.fetchall()
    # 这个东西封装起来似乎没什么用。。以后可以考虑加上错误处理？

def insert(col,src,val):
    tmp=""
    for i in val:
        if isinstance(i,int): tmp+="%d,"
        if isinstance(i,str): tmp+="%s,"
        # 暂且如此
    tmp=tmp[0:-1]
    s="INSERT INTO %s (%s) VALUES (%s);"%(src,col,tmp)
    DB.execute(s,val)
    r=DB.fetchall()

def user2dict(v):
    return { "username":v[1], "class":v[2],
        "permission":v[3], "classname":classIdToString(v[2])
    }

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
            "SELECT * FROM student WHERE stuId < %d AND stuId > %d;", # 这里是不是要 %s ?
            (classId * 100 + 100, classId * 100))
        r = DB.fetchall()
        if len(r) == 0:
            return False, {"message": "数据库信息错误"}
        else:
            return True, r
    else:
        return False, {"message": "请求接口错误"}

def getClassVolunteerList(classId):
    if isinstance(classId, int):
        DB.execute("SELECT volId FROM class_vol WHERE class = %d", (classId))
        r = DB.fetchall() # len(r) == 0 是否判定为数据库信息错误？
        lst = []
        for i in r:
            lst.append(i[0])
        return True, lst
    else:
        return False, {"message": "请求接口错误"}

def volunteerList(): # 总列表
    DB.execute("SELECT * FROM volunteer")
    r = DB.fetchall()
    return True, r

def getVolunteerInfo(volId):
    if isinstance(volId, int):
        DB.execute("SELECT * FROM volunteer WHERE volId = %d", (volId))
        r = DB.fetchall()
        if len(r) == 0:
            return False, {"message": "数据库信息错误"}
        else:
            return True, r[0]
    else:
        return False, {"message": "请求接口错误"}

def listToDict_volunteer(a):
    if isinstance(a, list) and len(a) == 12 and isinstance(a[0], int) and isinstance(a[1], str) and isinstance(a[2], str): # Date形式存储的mysql内容读取出来后怎么判断
        return True, {"volId": a[0], "volName": a[1], "volDate": a[2], "volTime": a[3], "stuMax": a[4], "nowStuCount": a[5], "description": a[6], "status": a[7], "volTimeInside": a[8], "volTimeOutside": a[9], "volTimeLarge": a[10], "holderId": a[11]}
    else:
        return False, {"message": "调用接口错误"}