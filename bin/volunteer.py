from flask import Blueprint, request
import json
import database as DB

Volunteer = Blueprint('volunteer', __name__)

@Volunteer.route('/volunteer/list', methods = ['POST'])
def getVolunteerList():
    respdata = {'type': 'ERROR', 'message': '未知错误'}
    DB.execute(
        "SELECT volId, volName, description, volTime, status, stuMax FROM volunteer") # 这里是否需要获取分配给我班有多少人
    r = DB.fetchall()
    respdata['type'] = 'SUCCESS'
    respdata['message'] = '获取成功'
    respdata['volunteer'] = []
    for i in r:
        respdata['volunteer'].append(
            {'id': i[0], 'name': i[1], 'description': i[2], 'time': i[3], 'status': i[4], 'stuMax': i[5]})
    return json.dumps(respdata)

@Volunteer.route('/volunteer/fetch/<int:volId>', methods = ['POST'])
def getVolunteer(volId):
    respdata = {'type': 'ERROR', 'message': '未知错误'}
    DB.execute_param(
        "SELECT volName, volDate, volTime, stuMax, description, nowStuCount, status, volTimeInside, volTimeOutside, volTimeLarge, holderId FROM volunteer WHERE volId = '?'", (volId))
    r = DB.fetchall()
    if len(r) <> 1:
        respdata['message'] = '数据库信息错误'
    else:
        respdata['type'] = 'SUCCESS'
        respdata['message'] = '获取成功'
        respdata['name'] = r[0][0]
        respdata['date'] = r[0][1]
        respdata['time'] = r[0][2]
        respdata['stuMax'] = r[0][3]
        respdata['description'] = r[0][4]
        respdata['nowStu'] = r[0][5]
        respdata['status'] = r[0][6]
        respdata['inside'] = r[0][7]
        respdata['outside'] = r[0][8]
        respdata['large'] = r[0][9]
        respdata['hid'] = r[0][10]
    return json.dumps(respdata)

@Volunteer.route('/volunteer/signup/<int:volId>', methods = ['POST'])
def signupVolunteer(volId):
    respdata = {'type': 'ERROR', 'message': '未知错误'}
    json_data = json.loads(request.get_data().decode("utf-8"))
    user_class = session["class"]
    tag = True
    for i in json_data['stulst']:
        if i < user_class * 100 or i >= user_class * 100 + 100:
            Tag = False
            break
    if not Tag:
        respdata['message'] = "学生列表错误"
    else:
        DB.execute_param(
            "SELECT stuMax, nowStuCount FROM volunteer WHERE volId = ?", (volId))
        r = DB.fetchall()
        if len(r) <> 1:
            respdata['message'] = "数据库信息错误"
        else:
            if len(json_data['stulst']) > r[0][0] - r[0][1]:
                respdata['message'] = "人数超限"
            else:
                DB.execute_param(
                    "SELECT stuMax FROM class_vol WHERE volId = ? AND classId = ?", (volId, user_class))
                # 这里不对，应该在class_vol表里存这个班已经报名了多少人，不然多次报名可以突破班级人数限制
                r = DB.fetchall()
                if len(r) <> 1:
                    respdata['message'] = "数据库信息错误"
                else:
                    if len(json_data['stulst']) > r[0][0]:
                        respdata['message'] = "人数超限"
                    else:
                        for i in json_data['stulst']:
                            # 代码来不及写了，写一下思路
                            # class_vol表里修改一下这个班的报名人数
                            # stu_vol表里加一条未审核的记录
                            # volunteer表里修改nowStuCount
                        respdata['type'] = "SUCCESS"
                        respdata['message'] = "添加成功"
                        
@Volunteer.route('volunteer/create', methods = ['POST'])
def createVolunteer():
    respdata = {'type': 'error', 'message': '未知错误'}
    json_data = json.loads(request.get_data().decode("utf-8"))
    if session["permisson"]>1