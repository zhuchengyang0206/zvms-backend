from flask import Flask
import sqlite3

# SQL init
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Flask init
app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    user = request.form['userid']
    psw = request.form['password']
    if c.execute("SELECT * FROM user WHERE username=? AND password=?", (user, psq)):
        # if it's a successfully login
        return "welcome! %s" % user # temporary

app.run()
