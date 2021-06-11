from flask import Blueprint, request
import tokenlib as tk
import json
import oppressor as OP
from deco import Deco

Class = Blueprint('class', __name__)

@Class.route('/class/list', methods = ['GET'])
@Deco
def getClassList(): # 好了
	# 是不是还要加上特殊情况的判断？
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
@Deco
def getClassVolunteer(classId): # 还没调
    fl,r=OP.select("volId","class_vol","class=%s",(classId),["id"],only=False)
    if not fl: return r
    ret={"type":"SUCCESS","message":"获取成功","volunteer":[]}
    for i in r:
        ff,rr=OP.select("volId,volName,volDate,volTime,description,status,stuMax",
        "volunteer","volId=%s",(i),["id","name","date","time","description","status","stuMax"])
        if not ff: return rr
        ret["volunteer"].append(rr)
    return ret
