import sqlite3
import socket
import _thread
import json
class DBcontrol(object):
    def __init__(self):
        self.conn = sqlite3.connect('./zvms.db')
        self.cur = self.conn.cursor()
        self.locked = False # 线程锁
    def __del__(self):
        self.cur.close()
        self.conn.close()
    def execute(a):
        while self.locked:
            pass
        self.lock()
        self.cur.execute(a)
        self.unlock()
    def commit():
        while self.locked:
            pass
        self.lock()
        self.conn.commit()
        self.unlock()
    def fetchall():
        while self.locked:
            pass
        self.lock()
        res = self.cur.fetchall()
        self.unlock()
        return res
    def lock():
        self.locked = True
    def unlock():
        self.locked = False

DB = DBcontrol()

def analyzer(cli):
    global DB
    while True:
        msg = cli.recv()
        if msg=="COMMIT":
            DB.commit()
        elif msg=="FETCHALL":
            cli.send(json.dumps(DB.fetchall()))
        else:
            DB.execute(msg)

def run():
    s = socket.socket()
    s.bind((socket.gethostname(), 1020))
    s.listen(5)
    while True:
        c, addr = s.accept()
        _thread.start_new_thread(analyzer, (c))