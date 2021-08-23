from flask import Blueprint, request
from deco import *
import tokenlib as TK
import json
import traceback
import oppressor as OP

User = Blueprint('user', __name__)

@User.route('/user/login', methods = ['POST','OPTIONS'])
@Deco
def login_NoToken():
	userid = json_data().get("userid")
	password = json_data().get("password")
	st, val = OP.userLogin(userid, password)
	ret={}
	if st:
		ret.update({"type":"SUCCESS", "message":"登入成功！"})
		ret.update(OP.user2dict(val))
		ret.update({"token":TK.generateToken({
			"userid": userid,
			"username": ret['username'],
			"class": ret['class'],
			"permission": ret['permission']
		})})
	else:
		traceback.print_exc()
		ret.update(val)
	return ret

@User.route('/user/logout', methods = ['GET','OPTIONS'])
@Deco
def logout_NoToken():
	return {'type': 'SUCCESS', 'message': '登出成功！'}
	#最好在这里做点什么吧，比如删除cookie什么的

@User.route('/user/info', methods = ['GET'])
@Deco
def info():
	return {'type':'SUCCESS', 'message':"获取成功", 'info':tkData()}

@User.route('/user/getInfo/<int:userId>', methods=['POST'])
@Deco
def getInfo(userId):
	fl,r=OP.select("userName,class,permission","user","userId=%s",userId,["userName","class","permission"])
	if not fl: return r
	r.update({"type":"SUCCESS", "message":"获取成功"})
	return r

@User.route('/user/modPwd', methods = ['POST'])
@Deco
def modifyPassword():
	old=json_data().get("oldPwd")
	new=json_data().get("newPwd")
	print(type(tkData().get("userid")))
	OP.update("password=%s","user","userId=%s",(new, tkData().get("userid"),))
	return {"type":"SUCCESS", "message":"修改成功"}