from flask import Blueprint, request
import tokenlib as tk
import json
import traceback
import oppressor as OP

User = Blueprint('user', __name__)

@User.route('/user/login', methods=['POST'])
def login():
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    try:
        json_data = json.loads(request.get_data().decode("utf-8"))  # 读取POST传入的JSON数据
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
            traceback.print_exc()
            respdata.update(val)
    except:
        respdata['message'] = "接口错误"
    return json.dumps(respdata)  # 传回json数据

@User.route('/user/logout', methods=['POST'])
def logout():
    respdata = {'type': 'SUCCESS', 'message': '登出成功！'}
    #最好在这里做点什么吧，比如删除cookie什么的
    return json.dumps(respdata)

@User.route('/user/info', methods=['POST','GET'])
def info():
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    try:
        tkst, tkdata = tk.readToken(json.loads(request.get_data().decode('utf-8')).get('token'))
        if tkst == tk.SUCCESS:
            respdata['type']="SUCCESS"
            respdata['message']="获取成功"
            respdata['info']=tkdata
        elif tkst == tk.EXPIRED:
            respdata['message']="token过期"
        elif tkst == tk.BAD:
            respdata['message']="token出错"
    except:
        respdata['message']="接口错误"
    return json.dumps(respdata)

@User.route('/user/getInfo/<int:userId>', methods=['POST'])
def getInfo():
    pass
