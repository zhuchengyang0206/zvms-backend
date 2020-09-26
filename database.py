import sqlite3
import socket
class DBcontrol(object):
    def __init__(self):
        self.conn = sqlite3.connect('./zvms.db')
        self.cur = self.conn.cursor()
    def __del__(self):
        self.cur.close()
        self.conn.close()
    def execute(*args):
        self.cur.execute(*args)
    def commit():
        self.conn.commit()
    def fetchall():
        return self.cur.fetchall()
        
DB = DBcontrol()