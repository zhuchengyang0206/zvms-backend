from flask import Blueprint, request
import json
import database

Class = Blueprint('class', __name__)

def classIdToString(a):
    # 留坑

@Class.route('/class/list', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':  # 只有POST请求才是符合规范的
        respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
        DB.execute(
            "SELECT userid FROM user WHERE userid > 202000")
        # 获取数据库返回的所有行
        r = DB.fetchall()
        if len(r) == 0:  # 如果没有对应的记录
            respdata['message'] = "数据库信息错误！"
        else:
            respdata['type'] = "SUCCESS"
            respdata['message'] = "获取成功"
            respdata['total'] = len(r)
            respdata['class'] = [] # 列表初始化
            for i in r:
                respdata['class'].append({'id':i, 'name': classIdToString(i)})

        return json.dumps(respdata)  # 传回json数据
    else:  # 如果不是POST请求那就返回个寂寞
        return ""
