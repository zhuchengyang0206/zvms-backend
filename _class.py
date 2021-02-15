from flask import Blueprint, request
import tokenlib as tk
import json
import oppressor as OP
from deco import Deco

Class = Blueprint('class', __name__)

@Class.route('/class/list', methods = ['GET'])
@Deco
def getClassList(): # 好了
    fl,r=OP.select("class","user","true",(),["id"],only=False)
    print(fl,r)
    if not fl: return r
    for i in r: i.update({"name":OP.classIdToString(i["id"])})
    return {
        "type": "SUCCESS",
        "message": "获取成功",
        "class": r
    }
    
@Class.route("/class/stulist/<int:classId>", methods = ['GET'])
@Deco
def getStudentList(classId): # 好了
    fl,r=OP.select("stuId,stuName,volTimeInside,volTimeOutside,volTimeLarge","student",
        "stuId > %s and stuId < %s",(str(classId*100),str(classId*100+100)),
        ["id","name","inside","outside","large"],only=False)
    if not fl: return r
    return {
        "type": "SUCCESS",
        "message": "获取成功",
        "student": r
    }

@Class.route("/class/volunteer/<int:classId>", methods = ['GET'])
def getClassVolunteer(classId):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}
    st, val = OP.getClassVolunteerList(classId)
    if st:
        respdata['volunteer'] = []
        for i in r:
            st1, val1 = OP.getVolunteerInfo(i)
            if st1:
                respdata['volunteer'].append(
                    OP.listToDict_volunteer(val1))
            else:
                respdata.update(val1)
                break
        else:
            respdata['type'] = 'SUCCESS'
            respdata['message'] = '获取成功'
    else:
        respdata.update(val)
    return json.dumps(respdata)
