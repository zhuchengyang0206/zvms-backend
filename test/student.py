from flask import Blueprint
import database as DB
import json

Student = Blueprint("student", __name__)
@Student.route('/student/volbook/<int:stuId>', methods=['POST'])
def getVolbook(stuId):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}
    DB.execute(
        "SELECT volId FROM stu_vol WHERE stuId = %d"% (stuId))
    r = DB.fetchall()
    respdata['type'] = "SUCCESS"
    respdata['message'] = "获取成功"
    respdata['rec'] = []
    for i in r:
        DB.execute(
            "SELECT volName, volTimeInside, volTimeOutside, volTimeLarge, status FROM stu_vol WHERE vid = %d"%d (i[0]))
        res = DB.fetchall()
        respdata['rec'].append(
            {"volId": i[0], "name": res[0], "inside": res[1], "outside": res[2], "large": res[3], "status": res[4]}
        )
    return json.dumps(respdata)
