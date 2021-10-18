from flask import Flask,make_response,request
from flask_cors import CORS
# from flask_script import Manager
import database
from user import User
from _class import Class
from student import Student
from volunteer import Volunteer
from notice import Notice
from report import Report

# Flask init
app = Flask(__name__)
app.debug = False  # 仅在测试环境打开！
app.config["SECRET_KEY"] = "PaSsw0rD@1234!@#$"

CORS(app, supports_credentials=True) # 允许跨域

app.register_blueprint(User)
app.register_blueprint(Class)
app.register_blueprint(Student)
app.register_blueprint(Volunteer)
app.register_blueprint(Notice)
app.register_blueprint(Report)

@app.route('/',methods=['POST'])
def main():
   return ""

# manager = Manager(app)
if __name__ == '__main__':
    # manager.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000)
