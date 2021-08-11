# 在Oppressor完成以后请不要直接使用这里面的函数
# 详细请看oppressor.py中的select/insert/update

from pymysql import connect, cursors
import traceback # 更好的错误输出

# （临时的）设置，记得改密码！
conn = connect(
    host = "127.0.0.1",
    user = "zvms",
    password = "123456",
    db = "zvms"
)
cur = conn.cursor()

def close(): # 这玩意有被用到吗？
    global conn,cur
    try:
        cur.close()
        conn.close()
    except:
        traceback.print_exc()

def execute(sql, param = None):
    global cur, conn
    try:
        cur.execute(sql, param)
    except:
        traceback.print_exc()
        conn.rollback()

def fetchall():
    global cur
    try:
        return cur.fetchall()
    except:
        traceback.print_exc()

def fetchone():
    global cur
    try:
        return cur.fetchone()
    except:
        traceback.print_exc()
