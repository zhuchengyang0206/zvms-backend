from flask import Blueprint
import database as DB
import oppressor as OP
from deco import *
import tokenlib as TK
import json

Student = Blueprint("student", __name__)

@Student.route('/student/volbook/<int:stuId>', methods=['POST'])
@Deco
def getVolbook(stuId): # 可以了
    fl,r=OP.select("volId","stu_vol","stuId=%s",(stuId),["volId"],only=False)
    if not fl: return r
    ret={"type": "SUCCESS","message": "获取成功","rec":[]}
    for i in r:
        ff,rr=OP.select("volId,volName,volTimeInside,volTimeOutside,volTimeLarge,status","volunteer",
            "volId=%s",(i["volId"]),["volId","name","inside","outside","large","status"])
        if not ff: return rr
        ret["rec"].append(rr)
    return ret