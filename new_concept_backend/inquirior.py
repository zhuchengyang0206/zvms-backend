# 负责对数据库的直接数据查询，不报错
import database as DB

# TABLE user
def user_getAll():
    DB.execute("SELECT * FROM user")
    return DB.fetchall()

def user_getById(id):
    DB.execute("SELECT * FROM user where userId = %s", (id))
    return DB.fetchone()

def user_modifyById(id, userName, _class, permission, password):
    DB.execute("UPDATE user SET userName = %s, class = %s, permission = %s, password = %s) where userId = %s", (userName, _class, permission, password, id))