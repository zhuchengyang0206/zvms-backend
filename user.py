from flask import Blueprint, request, session

import json
import oppressor as OP

User = Blueprint('user', __name__)

@User.route('/user/login', methods=['POST'])
def login():
    json_data = json.loads(
        request.get_data().decode("utf-8"))  # 读取POST传入的JSON数据
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    # 读取参数
    userid = json_data.get("userid")
    password = json_data.get("password")
    st, val = OP.userLogin(userid, password)
    if st:
        respdata['type'] = "SUCCESS"
        respdata['message'] = "登陆成功"
        respdata['username'] = val[1]
        respdata['class'] = val[2]
        respdata['permission'] = val[3]
        respdata['classname'] = OP.classIdToString(val[2])

        session['username'] = respdata['username']
        session['class'] = respdata['class']
        session['permission'] = respdata['permission']
    else:
        respdata.update(val)
    return json.dumps(respdata)  # 传回json数据

@User.route('/user/logout', methods=['POST'])
def logout():
    session.clear()
    respdata = {'type': 'SUCCESS', 'message': '登出成功！'}
    #最好在这里做点什么吧，比如删除cookie什么的
    return json.dumps(respdata)
