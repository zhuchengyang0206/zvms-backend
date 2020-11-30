from sqlite3 import connect
import traceback # 更好的错误输出

conn = connect("zvms.db")
cur = conn.cursor()

def close():
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
        
def commit():
    global conn
    try:
        conn.commit()
    except:
        traceback.print_exc()
        conn.rollback()

def fetchall():
    global cur
    try:
        return cur.fetchall()
    except:
        traceback.print_exc()
