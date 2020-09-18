# from flask import Flask
import socket # ?
import json
import httplib
import sqlite3

# Flask init
# app = Flask(__name__)

# socket init
s = socket().socket()
host = socket.gethostname()
port = 8000
s.bind((host, port))

# SQL init
conn = sqlite3.connect('users')
c = conn.cursor()

# start
s.listen(1) # max connection
cli, addr = s.accept()
while True:
    msg = cli.recv(1024)