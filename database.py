from pymysql import connect, cursors

# initialize

conn = connect(
    host = "127.0.0.1",
    user = "zvms",
    password = "123456",
    db = "zvms"
)
cur = conn.cursor()

def execute(*args): # 这个*args有问题
    print(args)
    global cur, conn
    try:
        cur.execute(args)
    except:
        conn.rollback()

def commit():
    global conn
    try:
        conn.commit()
    except:
        conn.rollback()

def fetchall():
    global cur
    return cur.fetchall()

def getdata(only = True, *args):
    try:
        execute(args)
        r = fetchall()
        if only:
            if len(r) == 1:
                return True, r
            else:
                return False, r
        else:
            return True, r
    except:
        return True, ()

def close():
    global conn,cur
    cur.close()
    conn.close()
