from flask import Blueprint, request
from deco import *
import tokenlib as TK
import json
import res
import traceback
import oppressor as OP

User = Blueprint('user', __name__)

@User.route('/user/login', methods = ['POST','OPTIONS','GET'])
@Deco
def login_NoToken():
	userid = json_data().get("userid")
	password = json_data().get("password")
	version = json_data().get("version")
	if version != res.CURRENT_VERSION:
                return {"type": "ERROR", "message": res.CURRENT_VERSION_ERROR_MESSAGE}
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
		ret.update({"type": "ERROR", "message": "用户名或密码错误"})
		traceback.print_exc()
		ret.update(val)
	return ret

@User.route('/user/logout', methods = ['GET','OPTIONS','POST'])
@Deco
def logout_NoToken():
	return {'type': 'SUCCESS', 'message': '登出成功！'}
	#最好在这里做点什么吧，比如删除cookie什么的

@User.route('/user/info', methods = ['GET','POST','OPTIONS'])
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
	fl, r = OP.select("userid","user", "userId = %s and password = %s", (tkData().get("userid"), old), ["user"])
	if not fl: return {"type": "ERROR", "message": "密码错误"}
	print(type(tkData().get("userid")))
	OP.update("password=%s","user","userId=%s",(new, tkData().get("userid"),))
	return {"type":"SUCCESS", "message":"修改成功"}
