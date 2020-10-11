from flask import Blueprint, session
import database
import json

Student = Blueprint("student", __name__)
@Student.route('/student/volbook/<stuId>', methods=['POST'])
def getVolBook(stuId):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}
    database.execute("SELECT vid FROM stu_vol WHERE sid=%s"%(stuId))
    r = database.fetchall()
    respdata['type'] = "SUCCESS"
    respdata['message'] = "获取成功"
    respdata['rec'] = []
    for i in r:
        database.execute("SELECT vnm, vti, vto, vtl, stt FROM stu_vol WHERE vid=%s"%(i[0]))
        res = database.fetchall()
        respdata['rec'].append(
            {"volId": i[0], "name": res[0], "inside": res[1], "outside": res[2], "large": res[3], "status": res[4]}
        )
    return json.dumps(respdata)
