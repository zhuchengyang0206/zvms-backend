import pymysql

conn = 1
cur = 1

def init():
    global conn, cur
    conn = pymysql.connect(host = "localhost",
                           user = "zvms",
                           password = "123456",
                           db = "zvms")
    cur = conn.cursor()

def close():
    global conn, cur
    cur.close()
    conn.close()
def execute(a):
    global conn, cur
    cur.execute(a)
def commit():
    global conn, cur
    conn.commit()
def fetchall():
    global conn, cur
    res = cur.fetchall()
    return res
