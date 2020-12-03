from flask import Flask,make_response
from flask_cors import CORS
import database
from user import User
from _class import Class
from student import Student

# Flask init
app = Flask(__name__)
app.debug = True  # 仅在测试环境打开！
app.config["SECRET_KEY"] = "PaSsw0rD@1234!@#$"
CORS(app, supports_credentials=True)
@app.after_request
def af_req(resp):
    resp = make_response(resp, 200)
    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    resp.headers['Access-Control-Allow-Methods'] = 'PUT,POST,GET,DELETE,OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , authorize'
    resp.headers['Access-Control-Allow-Credentials'] = 'true'

    resp.headers['X-Powered-By'] = 'ZVMS-beta'
    resp.headers['Content-Type'] = 'application/json;charset=utf-8'
    return resp

app.register_blueprint(User)
app.register_blueprint(Class)
app.register_blueprint(Student)

@app.route('/',methods=['POST'])
def main():
   return ""

if __name__ == '__main__':
    app.run()
