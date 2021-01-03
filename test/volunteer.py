from flask import Blueprint, request
import json
from deco import *
import oppressor as OP

Volunteer = Blueprint('volunteer', __name__)

@Volunteer.route('/volunteer/list', methods = ['POST'])
@Deco
def getVolunteerList():
    respdata = {'type': 'ERROR', 'message': '未知错误'}
    st, val = OP.volunteerList()
    if st:
        respdata['type'] = 'SUCCESS'
        respdata['message'] = '获取成功'
        respdata['volunteer'] = []
        for i in val:
            respdata['volunteer'].append(
                {'id': i[0], 'name': i[1], 'description': i[2], 'time': i[3], 'status': i[4], 'stuMax': i[5]})
    return respdata

@Volunteer.route('/volunteer/fetch/<int:volId>', methods = ['POST'])
@Deco
def getVolunteer(volId):
    respdata = {'type': 'ERROR', 'message': '未知错误'}
    st, val = OP.getVolunteerInfo(volId)
    if st:
        # version 1
        st1, val1 = OP.listToDict_volunteer(val)
        if st1:
            respdata['type'] = 'SUCCESS'
            respdata['message'] = '获取成功'
        respdata.update(val1)
        # version 2
        # respdata['type'] = 'SUCCESS'
        # respdata['message'] = '获取成功'
        # respdata.update(OP.listToDict_volunteer_faultless(val))
    else:
        respdata.update(val)
    return respdata

@Volunteer.route('/volunteer/signup/<int:volId>', methods = ['POST'])
@Deco
def signupVolunteer(volId):
    user_class = tkdata.get("class")
    for i in json_data['stulst']:
        if i < user_class * 100 or i >= user_class * 100 + 100:
            return {"type": "ERROR", "message": "学生列表错误"}
    # 判断人数是否超过这个义工的人数上限
    st, r = OP.select("stuMax, nowStuCount","volunteer","volId=%d",volId,["stuMax","nowStuCount"],only=True)
    if not st: return r
    if len(json_data['stulst']) > r["stuMax"] - r["nowStuCount"]:
        return {"type":"ERROR", "message":"人数超限"}
    # 判断人数是否超过班级人数上限
    st, r = OP.select("stuMax, nowStuCount","class_vol","volId=%d AND classId=%d",(volId,classId),["stuMax"],only=True)
    # 在class_vol表里面应该加上nowStuCount字段
    if not st: return r
    if len(json_data['stulst']) > r["stuMax"] - r["nowStuCount"]:
        return {"type":"ERROR", "message":"人数超限"}
    for i in json_data['stulst']:
        # 代码来不及写了，写一下思路
        OP.update("nowStuCount=nowStuCount+%d","class_vol","volId=%d AND classId=%d",
            (len(json_data['stulst']),volId,classId))
        OP.update("nowStuCount=nowStuCount+%d","volunteer","volId=%d",
            (len(json_data['stulst']),volId))
        # stu_vol表里加一条未审核的记录 # 这里是不是有点问题？
    return {"type":"SUCCESS","message":"添加成功"}

@Volunteer.route('volunteer/create', methods = ['POST'])
@Deco
def createVolunteer():
    respdata = {'type': 'error', 'message': '未知错误'}
    json_data = json.loads(request.get_data().decode("utf-8"))
    # if session["permisson"]>1

@Volunteer.route('volunteer/signerList/<int:volId>', methods = ['POST'])
def getSignerList(volId):
    pass

@Volunteer.route('volunteer/choose/<int:volId>', methods = ['POST'])
def chooseVolunteer(volId):
    pass

@Volunteer.route('volunteer/joinerList/<int:volId>', methods = ['POST'])
def getJoinerList(volId):
    pass

@Volunteer.route('volunteer/thought/<int:volId>', methods = ['POST'])
def submitThought(volId):
    pass

@Volunteer.route('volunteer/randomThought', methods=['POST','GET'])
def randthought():
    respdata = {'type':'SUCCESS', 'stuName':'用户名', 'stuId': 20200101, 'content':'这是感想内容'}
    return json.dumps(respdata)
