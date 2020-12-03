from flask import Blueprint, request
import tokenlib as tk
import json
import oppressor as OP

Class = Blueprint('class', __name__)

@Class.route('/class/list', methods = ['POST'])
def getClassList():
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    try:
        #print("Before")
        #tkst, tkdata = tk.readToken(json.loads(request.get_data().decode('utf-8')).get('token'))
        #print("After")
        #if tkdata['permission'] >= 1 and tkst == tk.SUCCESS:
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
        #elif tkst == tk.EXPIRED or tkst == tk.BAD or tkst == tk.ERROR:
        #    respdata['message'] = "Token错误"
        #else:
        #    respdata['message'] = "权限错误！"
    except:
        respdata['message'] = "接口错误"
    return json.dumps(respdata)  # 传回json数据
    
@Class.route("/class/stulist/<int:classId>", methods = ['POST'])
def getStudentList(classId):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    try:
        #tkst, tkdata = tk.readToken(json.loads(request.get_data().decode('utf-8')).get('token'))
        #if (tkdata["permission"] > 1 or classId == tkdata["class"]) and tkst == tk.SUCCESS:
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
        #elif tkst == tk.EXPIRED or tkst == tk.BAD or tkst == tk.ERROR:
        #    respdata['message'] = "Token错误"
        #else:
        #    respdata['message'] = "权限错误！"
    except:
        respdata['message'] = "接口错误"

    return json.dumps(respdata)  # 传回json数据

@Class.route("/class/volunteer/<int:classId>", methods = ['POST'])
def getClassVolunteer(classId):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}
    st, val = OP.getClassVolunteerList(classId)
    if st:
        respdata['volunteer'] = []
        flg = True
        err = {}
        for i in r:
            st1, val1 = OP.getVolunteerInfo(i)
            if st1:
                respdata['volunteer'].append(
                    OP.listToDict_volunteer_faultless(val1))
            else:
                flg = False
                err = val1
                break
        if flg:
            respdata['type'] = 'SUCCESS'
            respdata['message'] = '获取成功'
        else:
            respdata.update(err)
    else:
        respdata.update(val)
    return json.dumps(respdata)
