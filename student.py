from flask import Blueprint, session
import json

Student = Blueprint("student", __name__)
@Student.route('/student/volbook/<stuId>', methods=['POST', 'GET'])
def getVolBook(stuId):
    if request.methods == 'POST':
        respdata = {'type': 'ERROR', 'message': '未知错误!'}
        DB.execute("SELECT * FROM stu_vol WHERE stuId=?",(stuId))
        r = DB.fetchall()
        respdata['type'] = "SUCCESS"
        respdata['message'] = "获取成功"
        
    else:
        return ""