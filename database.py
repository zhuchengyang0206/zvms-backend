import pymysql

conn = pymysql.connect(host="127.0.0.1",user="zvms",password="123456",db="zvms")
cur = conn.cursor()

def close():
    global conn,cur
    cur.close()
    conn.close()

def execute(a):
    global cur
    try:
        cur.execute(a)
    except:
        conn.rollback()

def commit():
    global conn
    try:
        conn.commit()
    except:
        conn.rollback()

def fetchall():
    res = cur.fetchall()
    return res
