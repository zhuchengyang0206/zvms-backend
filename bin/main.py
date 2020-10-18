from flask import Flask,session
import database
from user import User
from _class import Class
from student import Student

# Flask init
app = Flask(__name__)
app.debug = True  # 仅在测试环境打开！
app.config["SECRET_KEY"] = "PaSsw0rD@1234!@#$"

app.register_blueprint(User)
app.register_blueprint(Class)
app.register_blueprint(Student)

@app.route('/',methods=['POST'])
def main():
   return ""

if __name__ == '__main__':
    app.run()
