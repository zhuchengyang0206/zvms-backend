import pymysql

conn = pymysql.connect(host="localhost",user="zvms",password="123456",db="zvms")
cur = conn.cursor()

def close():
    global conn,cur
    cur.close()
    conn.close()
def execute(a):
    global cur
    cur.execute(a)
def commit():
    global conn
    conn.commit()
def fetchall():
    res = cur.fetchall()
    return res