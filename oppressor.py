# 随手打的一个词竟然还真的有，那就用这个名吧
# 这个文件封装了一些针对数据库的操作
import database as DB
def userLogin(userId, password):
    if isinstance(userId, int) and isinstance(password, int):
        DB.execute("SELECT * FROM user WHERE userId = %s AND password = %s;", (userId, password))
        r = DB.fetchall()
        if len(r) == 0:
            return False, {"message": "用户ID或密码错误"}
        elif len(r) > 1:
            return False, {"message": "数据库信息错误"}
        else:
            return True, r
    else:
        return False, {"message": "请求接口错误"}