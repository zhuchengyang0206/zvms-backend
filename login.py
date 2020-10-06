from flask import Blueprint, request, session
from flask_cors import CORS

import json
import database

Login = Blueprint('login', __name__)
#登录
@Login.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':  # 只有POST请求才是符合规范的
        json_data = json.loads(
            request.get_data().decode("utf-8"))  # 读取POST传入的JSON数据
        respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
        # 读取参数
        userid = json_data.get("userid")
        password = json_data.get("password")
        database.execute(
            "SELECT * FROM user WHERE unm='%s' AND pwd='%s'"%(userid, password))
        # 获取数据库返回的所有行
        r = database.fetchall()
        if len(r) == 0:  # 如果没有对应的记录
            respdata['message'] = "用户ID或密码错误！"
        elif len(r) == 1:  # 如果只有一条记录说明符合要求
            row = r[0]

            respdata['type'] = "SUCCESS"
            respdata['message'] = "登陆成功"
            respdata['username'] = row[1]
            respdata['class'] = row[2]
            respdata['permission'] = row[3]

            session['username'] = respdata['username']
            session['class'] = respdata['class']
            session['permission'] = respdata['permission']

        elif len(r) > 1:  # 不然就是出现了两条一样的记录，此时为了安全考虑不能登录
            respdata['message'] = "用户重复！请向管理员寻求帮助！"
        return json.dumps(respdata)  # 传回json数据
    else:  # 如果不是POST请求那就返回个寂寞
        return ""
