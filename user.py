from flask import Blueprint, request
import tokenlib as tk
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
        respdata['message'] = "登录成功"
        respdata.update({"username": val[1], "class": val[2], "permission": val[3], "classname": OP.classIdToString(val[2])})
        respdata.update({"token":tk.generateToken({
            "username": respdata['username'],
            "class": respdata['class'],
            "permission": respdata['permission']
        })})
    else:
        respdata.update(val)
    return json.dumps(respdata)  # 传回json数据

@User.route('/user/logout', methods=['POST'])
def logout():
    respdata = {'type': 'SUCCESS', 'message': '登出成功！'}
    #最好在这里做点什么吧，比如删除cookie什么的
    return json.dumps(respdata)

@User.route('/user/info/', methods=['POST','GET'])
def info():
    json_data = json.loads(request.get_data().decode("utf-8"))
    st, data = tk.readToken(json_data.get["token"])
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    if st == tk.SUCCESS:
        respdata['type']="SUCCESS"
        respdata['message']="获取成功"
        respdata['info']=data
        return json.dumps(respdata)
    elif st == tk.EXPIRED:
        respdata['message']="token过期"
    elif st == tk.BAD:
        respdata['message']="token出错"
    return 