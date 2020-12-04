from flask import Blueprint
import database as DB
from deco import *
import tokenlib as TK
import json

Student = Blueprint("student", __name__)
@Student.route('/student/volbook/<int:stuId>', methods=['POST'])
@Deco
def getVolbook(stuId):
    if tkData().get("permission")==1 and tkData().get("class")!=stuId//100:
        return {'type':'ERROR', 'message':"权限不足"}
    DB.execute("SELECT volId FROM stu_vol WHERE stuId = %s", (stuId))
    r = DB.fetchall()
    ret={'type':'SUCCESS', 'message':"获取成功", "rec":[]}
    for i in r:
        DB.execute(
            "SELECT volTimeInside, volTimeOutside, volTimeLarge, status FROM stu_vol WHERE volId = %s",
            (i[0]))
        res=DB.fetchall()[0]
        ret['rec']+=[{"volId": i[0], "inside": res[0], "outside": res[1], "large": res[2], "status": res[3]}]
    return ret