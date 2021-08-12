from flask import Blueprint, request
import json
from deco import *
from res import *
import oppressor as OP

Student = Blueprint('student', __name__)

@Student.route('/student/volbook/<int:stuId>', methods = ['GET'])
@Deco
def getVolunteerWork(stuId):
    fl,r=OP.select("volId,volTimeInside,volTimeOutside,volTimeLarge,status","stu_vol","stuId=%s", stuId,
    ["volId","inside","outside","large","status"],only=False)
    if not fl: return r
    for i in r:
        i["inside"]/=60
        i["outside"]/=60
        i["large"]/=60
        ff,rr=OP.select("volName","volunteer","volId=%s",i["volId"], ["name"])
        if not ff: return rr
        i.update({"name": rr["name"]})
    return {"type":"SUCCESS","message":"获取成功","rec":r}