from flask import Blueprint, request, session

import json
import database as DB

User = Blueprint('user', __name__)

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
    # 系统 110003 110004
    if _year//100 == 10:
        ret = "教师"
        return ret
    elif _year//100 == 1:
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

@User.route('/user/login', methods=['POST'])
def login():
    json_data = json.loads(
        request.get_data().decode("utf-8"))  # 读取POST传入的JSON数据
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    # 读取参数
    userid = json_data.get("userid")
    password = json_data.get("password")
    DB.execute("SELECT * FROM user WHERE userId=%s AND password=%s;",(userid, password))
    # 获取数据库返回的所有行
    r = DB.fetchall()
    if len(r) == 0:  # 如果没有对应的记录
        respdata['message'] = "用户ID或密码错误！"
    elif len(r) == 1:  # 如果只有一条记录说明符合要求
        row = r[0]

        respdata['type'] = "SUCCESS"
        respdata['message'] = "登陆成功"
        respdata['username'] = row[1]
        respdata['class'] = row[2]
        respdata['permission'] = row[3]
        respdata['classname'] = classIdToString(row[2])

        session['username'] = respdata['username']
        session['class'] = respdata['class']
        session['permission'] = respdata['permission']

    elif len(r) > 1:  # 不然就是出现了两条一样的记录，此时为了安全考虑不能登录
        respdata['message'] = "用户重复！请向管理员寻求帮助！"
    return json.dumps(respdata)  # 传回json数据

@User.route('/user/logout', methods=['POST'])
def logout():
    session.clear()
    respdata = {'type': 'SUCCESS', 'message': '登出成功！'}
    #最好在这里做点什么吧，比如删除cookie什么的
    return json.dumps(respdata)
