from flask import Blueprint, request
import json
import database

Volunteer = Blueprint('volunteer', __name__)

@Volunteer.route('/volunteer/list', methods = ['POST', 'GET'])
def getVolunteerList():
    if request.method == 'POST':
        respdata = {'type': 'ERROR', 'message': '未知错误'}
        database.execute(
            "SELECT vid, vnm, dsc, vtm, stt, smx FROM volunteer")
        r = database.fetchall()
        respdata['type'] = 'SUCCESS'
        respdata['message'] = '获取成功'
        respdata['volunteer'] = []
        for i in r:
            respdata['volunteer'].append(
                {'id': i[0], 'name': i[1], 'description': i[2], 'time': i[3], 'status': i[4], 'stuMax': i[5]})
        return json.dumps(respdata)
    else:
        return ""