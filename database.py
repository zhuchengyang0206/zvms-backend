import pymysql

class DBcontrol(object):
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",user="zvms",password="123456",db="zvms")
        self.cur = self.conn.cursor()
    def __del__(self):
        self.cur.close()
        self.conn.close()
    def execute(a):
        self.cur.execute(a)
    def execute(a, b):
        self.cur.execute(a, b)
    def commit():
        self.conn.commit()
    def fetchall():
        res = self.cur.fetchall()
        return res

DB = DBcontrol()
