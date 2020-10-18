from flask import Blueprint, session
import database as DB
import json

Student = Blueprint("student", __name__)
@Student.route('/student/volbook/<stuId>', methods=['POST'])
def getVolBook(stuId):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}
    DB.execute_param(
        "SELECT volId FROM stu_vol WHERE stuId = ?", (stuId))
    r = DB.fetchall()
    respdata['type'] = "SUCCESS"
    respdata['message'] = "获取成功"
    respdata['rec'] = []
    for i in r:
        DB.execute_param(
            "SELECT volName, volTimeInside, volTimeOutside, volTimeLarge, status FROM stu_vol WHERE vid = ?", (i[0]))
        res = DB.fetchall()
        respdata['rec'].append(
            {"volId": i[0], "name": res[0], "inside": res[1], "outside": res[2], "large": res[3], "status": res[4]}
        )
    return json.dumps(respdata)
