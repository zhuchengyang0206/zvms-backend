import socket

def analyze(msg):
    pos1 = msg.find("\n\r")
    pos2 = msg.find("\n\r\n\r")
    firstLine = msg[:pos1]
    header = msg[(pos1 + 2):pos2]
    content = msg[(pos2 + 4):]
    method, url, protocol = firstLine.split(" ")
    info = header.split("\n\r")
    # save informations
    resp = {}
    resp["method"] = method
    resp["url"] = url
    resp["protocol"] = protocol
    resp["header"] = []
    for i in info:
        field, value = i.split(": ")
        resp["header"].append({"field": field, "value": value})
    resp["content"] = content

    # 这里要把数据给后端让后端返回数据

    ret = "HTTP/1.1 200 OK\n\rServer: ZVMS\n\r\n\r" + 后端.返回的东西()
    # 这里要去弄tokenid之类的东西
    return ret

def run():
    s = socket.socket()
    s.bind(socket.gethostname(), 5000)
    s.listen(5)
    while True:
        c, addr = s.accept()
        msg = c.recv()
        c.send(analyze(msg))
        c.close()

if __name__ == "__main__":
    run()