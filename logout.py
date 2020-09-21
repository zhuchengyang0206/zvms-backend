from flask import Blueprint, session
import json

Logout = Blueprint('logout', __name__)
#登录
@Logout.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    respdata = {'type': 'SUCCESS', 'message': '登出成功！'}
    #最好在这里做点什么吧，比如删除cookie什么的
    return json.dumps(respdata)
