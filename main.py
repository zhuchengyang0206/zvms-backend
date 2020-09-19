from flask import Flask
import sqlite3

# SQL init
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Flask init
app = Flask(__name__)

@app.route('/')
def analyzer():
    return 'test'

app.run()