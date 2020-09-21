from flask import Flask,session

from login import Login
from logout import Logout

# Flask init
app = Flask(__name__)
app.debug = True  # 仅在测试环境打开！
app.config["SECRET_KEY"] = "PaSsw0rD@1234!@#$"

app.register_blueprint(Login) #登录
app.register_blueprint(Logout) #登出

@app.route('/')
def index():
   pass

if __name__ == '__main__':
    app.run()
