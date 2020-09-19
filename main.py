from flask import Flask, request
import json
import sqlite3

# Flask init
app = Flask(__name__)
app.debug = True  # 仅在测试环境打开！

#登录
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':  # 只有POST请求才是符合规范的
        json_data = json.loads(
            request.get_data().decode("utf-8"))  # 读取POST传入的JSON数据
        respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
        # 读取参数
        userid = json_data.get("userid")
        password = json_data.get("password")
        # 数据库连接操作
        conn = sqlite3.connect('zvms.db')
        c = conn.cursor()
        c.execute(
            "SELECT * FROM user WHERE userid=? AND password=?", (userid, password))
        # 获取数据库返回的所有行
        r = c.fetchall()
        if len(r) == 0:  # 如果没有对应的记录
            respdata['message'] = "用户ID或密码错误！"
        elif len(r) == 1:  # 如果只有一条记录说明符合要求
            row = r[0]
            respdata['type'] = "SUCCESS"
            respdata['message'] = "登录成功"
            respdata['username'] = row[1]
            respdata['class'] = row[2]
            respdata['permission'] = row[3]

            # 这里只是把登录信息给了客户端
            # 还需要几个SESSION的相关操作来在服务器储存用户信息

        elif len(r) > 1:  # 不然就是出现了两条一样的记录，此时为了安全考虑不能登录
            respdata['message'] = "用户重复！请向管理员寻求帮助！"
        conn.close()  # 关闭数据库连接
        return json.dumps(respdata)  # 传回json数据
    else:  # 如果不是POST请求那就返回个寂寞
        return ""

#登出
@app.route('/logout', methods=['POST', 'GET'])
def logout():
    respdata = {'type': 'SUCCESS', 'message': '登出成功！'}
    #最好在这里做点什么吧，比如删除cookie什么的
    return json.dumps(respdata)

if __name__ == '__main__':
    app.run()
