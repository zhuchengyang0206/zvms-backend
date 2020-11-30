import socket

def analyze(msg):
    #在字符串传入的时候莫名其妙会被转义，要不要之前先encode一下？
    print(msg)
    pos1 = msg.find("\\r\\n")
    pos2 = msg.find("\\r\\n\\r\\n")
    print(pos1,pos2)
    firstLine = msg[:pos1]
    print('firstline-->',firstLine)
    header = msg[(pos1 + 4):pos2]
    content = msg[(pos2 + 8):]
    method, url, protocol = firstLine.split(" ")
    info = header.split("\\r\\n")
    method=method[2:]
    print('header-->',header)
    print('content->',content)
    print('method-->',method)
    print('url----->',url)
    print('protocol>',protocol)
    # save informations
    resp = {}
    resp["method"] = method
    resp["url"] = url
    resp["protocol"] = protocol
    resp["header"] = []
    print("info:-->")
    for i in info:
        print(i)
        field, value = i.split(": ")
        resp["header"].append({"field": field, "value": value})
    resp["content"] = content
    
    # 这里要把数据给后端让后端返回数据
    
    ret = "HTTP/1.1 200 OK\r\nServer: ZVMS\r\n\r\n"+"Hello,world!"
    #+ 后端.返回的东西()
    ## 这里要去弄tokenid之类的东西
    return ret

def run():
    s = socket.socket()
    s.bind((socket.gethostname(), 5000))
    print(socket.gethostname()) #hostname:5000
    s.listen(5)
    while True:
        c, addr = s.accept()
        print("Yes")
        msg = c.recv(1024)
        c.send(bytes(analyze(str(msg)).encode('UTF-8','strict')))
        c.close()

if __name__ == "__main__":
    run()