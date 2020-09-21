from flask import Blueprint, request
import json
import sqlite3

Class = Blueprint('class', __name__)
#登录
@Class.route('/class', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':  # 只有POST请求才是符合规范的
        json_data = json.loads(
            request.get_data().decode("utf-8"))  # 读取POST传入的JSON数据
        respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
        # 读取参数
        classid = json_data.get("classid")
        # 数据库连接操作
        conn = sqlite3.connect('zvms.db')
        c = conn.cursor()
        c.execute(
            "SELECT userid, permission FROM user WHERE userid > ? and userid < ?", (classid * 100, classid * 100 + 100))
        # 获取数据库返回的所有行
        r = c.fetchall()
        if len(r) == 0:  # 如果没有对应的记录
            respdata['message'] = "班级ID错误！"
        else:
            cnt = 0
            for row in r:
                cnt += 1
                respdata['student_id%d'%cnt] = row[0]
                respdata['student_permission%d'%cnt] = row[1]
            respdata['type'] = "SUCCESS"
            respdata['message'] = "登录成功"
            respdata['number'] = len(r)

        conn.close()  # 关闭数据库连接
        return json.dumps(respdata)  # 传回json数据
    else:  # 如果不是POST请求那就返回个寂寞
        return ""
