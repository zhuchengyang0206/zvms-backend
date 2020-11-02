from flask import Blueprint, request, session
import json
import database as DB

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
    if _year == thisYear:
        ret = ret + "一"
    elif _year == thisYear - 1:
        ret = ret + "二"
    else:
        ret = ret + "三"
    ret = ret + (["NULL","1","2","3","4","5","6","7","8","9","10","2","3","4","5","6","7"])[_class]
    ret = ret + "班"

@Class.route('/class/list', methods = ['POST'])
def getClassList():
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    if session['permission'] > 1:
        DB.execute(
            "SELECT userId FROM user WHERE userId > %d;"%
            (thisYear * 100 - 200))
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
    else:
        respdata['message'] = "权限错误！"
    return json.dumps(respdata)  # 传回json数据

@Class.route("/class/stulist/<int:classId>", methods = ['POST'])
def getStudentList(classid):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    if session["permission"] > 1 or classid == session["class"]:
        DB.execute(
            "SELECT * FROM student WHERE stuId < %d AND stuId > %d;"%
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
    else:
        respdata['message'] = "权限错误！"
    return json.dumps(respdata)  # 传回json数据

@Class.route("/class/volunteer/<int:classId>", methods = ['POST'])
def getClassVolunteer(classid):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}
    DB.execute(
        "SELECT volId FROM class_vol WHERE class = %d"% (classid))
    r = DB.fetchall()
    if len(r) == 0:
        respdata['message'] = "数据库信息错误！"
    else:
        respdata['type'] = 'SUCCESS'
        respdata['message'] = '获取成功'
        respdata['volunteer'] = []
        for i in r:
            DB.execute(
                "SELECT volName, volDate, volTime, description, status, stuMax FROM stu_vol WHERE volId=%d"% (i[0]))
            res = DB.fetchall()
            respdata['volunteer'].append(
                {"id": i[0], "name": res[0], "date": res[1], "time": res[2], "description": res[3], "status": res[4], "stuMax": res[5]}
            )
    return json.dumps(respdata)