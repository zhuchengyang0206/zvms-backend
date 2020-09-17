from flask import Flask
import sqlite3

# Flask init
app = Flask(__name__)
# SQL init
conn = sqlite3.connect('users')
c = conn.cursor()
