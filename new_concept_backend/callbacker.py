import socket

def run():
    s = socket.socket()
    s.bind(socket.gethostname(), 5000)
    while True:
        # 早睡早起不爆肝

if __name__ == "__main__":
    run()