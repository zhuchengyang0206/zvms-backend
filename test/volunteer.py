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
    user_class = tkData.get("class")
    # 判断是否都是本班的人
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
    if not st: return r
    if len(json_data['stulst']) > r["stuMax"] - r["nowStuCount"]:
        return {"type":"ERROR", "message":"人数超限"}
    # 修改数据库
    OP.update("nowStuCount=nowStuCount+%d","class_vol","volId=%d AND classId=%d",
        (len(json_data['stulst']),volId,classId))
    OP.update("nowStuCount=nowStuCount+%d","volunteer","volId=%d",
        (len(json_data['stulst']),volId))
    for i in json_data['stulst']:
        # 遍历每一个学生，加入一条未审核的记录
        OP.insert("volId,stuId,status,volTimeInside,volTimeOutside,volTimeLarge,thought",
            "stu_vol",(volId,i,0,0,0,""))
        # 审核过了以后再发义工时间
    return {"type":"SUCCESS","message":"添加成功"}

@Volunteer.route('volunteer/create', methods = ['POST'])
@Deco
def createVolunteer():
    if not tkData.get("permission") in [2,4]: # 这权限是不是有点奇怪？
        return {'type':'ERROR', 'message':"权限不足"}
    
    OP.insert("volId,volName,volDate,volTime",
        "volunteer",
        ())
    # 这里出了一些问题
    # TIME和DATE类型的insert还没写
    # 还有这两个类型可以直接用%吗？
    return {"type":"SUCCESS", "message":"创建成功"}
'''
    {
    "name": "义工活动1",
    "date": "2020.10.1",
    "time": "13:00",
    "stuMax": 20,
    "description": "新华书店打扫",
    "inside": 0,
    "outside": 3,
    "large": 0,
    "class": [
        {"id": 202001, "stuMax": 10},
        {"id": 202002, "stuMax": 5},
        {"id": 202003, "stuMax": 10}
    ]
    // hid 是自动从session获取的
    }
'''

@Volunteer.route('volunteer/signerList/<int:volId>', methods = ['POST'])
def getSignerList(volId):
    if not tkData.get("permission")<3:
        return {'type':'ERROR', 'message':"权限不足"}
    ret={"type":"SUCCESS", "message":"获取成功","result":[]}
    fl,r=OP.select("stuId","stu_vol","volId=%d",(volId),["stuId"],only=False)
    if not fl: return r
    for i in r: # 为什么要返回学生姓名啊
        fl,rr=OP.select("stuId,stuName","student","stuId=%d",(i.get("stuId"),["stuId","stuName"])
        if not fl: return rr
        ret["result"]+=rr
    return ret

@Volunteer.route('volunteer/choose/<int:volId>', methods = ['POST'])
def chooseVolunteer(volId):
    pass

@Volunteer.route('volunteer/joinerList/<int:volId>', methods = ['POST'])
def getJoinerList(volId):
    # 所以这个的意思是返回所有审核过了的报名的人吗？
    if not tkData.get("permission")<3:
        return {'type':'ERROR', 'message':"权限不足"}
    ret={"type":"SUCCESS", "message":"获取成功","result":[]}
    fl,r=OP.select("stuId","stu_vol","volId=%d and status=1",(volId),["stuId"],only=False)
    if not fl: return r
    for i in r: # 为什么要返回学生姓名啊
        fl,rr=OP.select("stuId,stuName","student","stuId=%d",(i.get("stuId"),["stuId","stuName"])
        if not fl: return rr
        ret["result"]+=rr
    return ret

@Volunteer.route('volunteer/thought/<int:volId>', methods = ['POST'])
def submitThought(volId):
    pass

@Volunteer.route('volunteer/randomThought', methods=['POST','GET'])
def randthought():
    respdata = {'type':'SUCCESS', 'stuName':'用户名', 'stuId': 20200101, 'content':'这是感想内容'}
    return json.dumps(respdata)
