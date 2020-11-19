import oppressor as OP

def login(data):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    # 读取参数
    userid = data["userid"]
    password = data["password"]
    st, val = OP.userLogin(userid, password)
    if st:
        respdata['type'] = "SUCCESS"
        respdata['message'] = "登陆成功"
        respdata.update({"username": val[1], "class": val[2], "permission": val[3], "className": OP.classIdToString(val[2])})
    else:
        respdata.update(val)
    return json.dumps(respdata)  # 传回json数据

def logout():
    respdata = {'type': 'SUCCESS', 'message': '登出成功！'}
    return respdata
