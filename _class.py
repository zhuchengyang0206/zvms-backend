from flask import Blueprint, request, session
import json
import oppressor as OP

Class = Blueprint('class', __name__)

@Class.route('/class/list', methods = ['POST'])
def getClassList():
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    if session['permission'] >= 1:
        st, val = OP.classList()
        if st:
            respdata['type'] = "SUCCESS"
            respdata['message'] = "获取成功"
            respdata['class'] = [] # 列表初始化
            for i in val:
                respdata['class'].append(
                    {'id': i, 'name': OP.classIdToString(i)})
        else:
            respdata.update(val)
    else:
        respdata['message'] = "权限错误！"
    return json.dumps(respdata)  # 传回json数据

@Class.route("/class/stulist/<int:classId>", methods = ['POST'])
def getStudentList(classId):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    if session["permission"] > 1 or classId == session["class"]:
        st, val = OP.studentList(classId)
        if st:
            respdata['type'] = "SUCCESS"
            respdata['message'] = "获取成功"
            respdata['student'] = []
            for i in val:
                respdata['student'].append(
                    {'id': i[0], 'name': i[1], 'inside': i[2], 'outside': i[3], 'large': i[4]})
        else:
            respdata.update(val)
    else:
        respdata['message'] = "权限错误！"
    return json.dumps(respdata)  # 传回json数据

@Class.route("/class/volunteer/<int:classId>", methods = ['POST'])
def getClassVolunteer(classId):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}
    DB.execute(
        "SELECT volId FROM class_vol WHERE class = %d"% (classId))
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