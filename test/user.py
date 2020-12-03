from flask import Blueprint, request
from deco import Deco, json_data
import tokenlib as tk
import json
import traceback
import oppressor as OP

User = Blueprint('user', __name__)

@User.route('/user/login', methods=['POST'])
@Deco
def login():
    userid = json_data().get("userid")
    password = json_data().get("password")
    st, val = OP.userLogin(userid, password)
    ret={}
    if st:
        ret.update({"type":"SUCCESS", "message":"登入成功！"})
        ret.update(OP.user2dict(val))
        ret.update({"token":tk.generateToken({
            "username": ret['username'],
            "class": ret['class'],
            "permission": ret['permission']
        })})
    else:
        traceback.print_exc()
        ret.update(val)
    return ret

@User.route('/user/logout', methods=['POST'])
@Deco
def logout():
    return {'type': 'SUCCESS', 'message': '登出成功！'}
    #最好在这里做点什么吧，比如删除cookie什么的

@User.route('/user/info', methods=['POST','GET'])
@Deco
def info():
    tkst, tkdata = tk.readToken(json_data()).get('token')
    if tkst == tk.SUCCESS:
        return {'type':'SUCCESS', 'message':"获取成功", 'info':tkdata}
    elif tkst == tk.EXPIRED:
        return {'type':'ERROR', 'message':"token过期"}
    elif tkst == tk.BAD:
        return {'type':'ERROR', 'message':"token失效"}
    return respdata

@User.route('/user/getInfo/<int:userId>', methods=['POST'])
@Deco
def getInfo(userId):
    pass
