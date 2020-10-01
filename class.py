from flask import Blueprint, request
import json
import database

Class = Blueprint('class', __name__)

thisYear = 2020 # 以后要改成自动获取

def classIdToString(a):
    global thisYear
    id = int(a)
    _year = id // 100
    _class = id % 100
    ret = ""
    if _class <= 10:
        ret = ret + "高"
    elif _class <= 16:
        ret = ret + "蛟"
    else:
        ret = ret + "剑"
    if _year == thisYear:
        ret = ret + "一"
    elif _year == thisYear - 1:
        ret = ret + "二"
    else:
        ret = ret + "三"
    ret = ret + (["NULL","1","2","3","4","5","6","7","8","9","10","2","3","4","5","6","7","1","2"])[_class]
    ret = ret + "班"

@Class.route('/class/list', methods=['POST', 'GET'])
def getClassList():
    if request.method == 'POST':  # 只有POST请求才是符合规范的
        respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
        DB.execute(
            "SELECT userid FROM user WHERE userid > 201800")
        # 获取数据库返回的所有行
        r = DB.fetchall()
        if len(r) == 0:  # 如果没有对应的记录
            respdata['message'] = "数据库信息错误！"
        else:
            respdata['type'] = "SUCCESS"
            respdata['message'] = "获取成功"
            respdata['class'] = [] # 列表初始化
            for i in r:
                respdata['class'].append(
                    {'id': i[0], 'name': classIdToString(i[0])})

        return json.dumps(respdata)  # 传回json数据
    else:  # 如果不是POST请求那就返回个寂寞
        return ""

@Class.route("/class/stulist/<classid>", methods=['POST','GET'])
def getStudentList(classid):
    if request.method == 'POST':
        respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
        DB.execute(
            "SELECT * FROM student WHERE stuId < ? AND stuId > ?",
            (classid * 100 + 100, classid * 100))
        r = DB.fetchall()
        if len(r) == 0:
            respdata['message'] = "数据库信息错误！"
        else:
            respdata['type'] = "SUCCESS"
            respdata['message'] = "获取成功"
            respdata['student'] = []
            for i in r:
                respdata['student'].append(
                    {'id': i[0], 'name': i[1], 'inside': i[2], 'outside': i[3], 'large': i[4]})

        return json.dumps(respdata)  # 传回json数据
    else:
        return ""
