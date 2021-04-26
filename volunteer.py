from flask import Blueprint, request
import json
from deco import *
import oppressor as OP

Volunteer = Blueprint('volunteer', __name__)

@Volunteer.route('/volunteer/list', methods = ['GET']) # 这里不需要参数传入，使用GET方式。下同
@Deco
def getVolunteerList(): # 可以了
    fl,r=OP.select("volId,volName,description,volDate,volTime,status,stuMax","volunteer","true",(),
        ["id","name","description","date","time","status","stuMax"],only=False)
    if not fl: return r
    return {
        "type": "SUCCESS",
        "message": "获取成功",
        "volunteer": r
    }

@Volunteer.route('/volunteer/fetch/<int:volId>', methods = ['GET'])
@Deco
def getVolunteer(volId): # 可以了
    fl,r=OP.select("volName,volDate,volTime,stuMax,nowStuCount,description,status,"+
		"volTimeInside,volTimeOutside,volTimeLarge",
        "volunteer","volId=%s",(volId),
		["name","date","time","stuMax","stuNow","description","status","inside","outside","large"])
    if not fl: return r
    r.update({"type":"SUCCESS","message":"获取成功"})
    return r

@Volunteer.route('/volunteer/signup/<int:volId>', methods = ['POST'])
@Deco
def signupVolunteer(volId):
    user_class = tkData.get("class")
    # 判断是否都是本班的人
    for i in json_data['stulst']:
        if i < user_class * 100 or i >= user_class * 100 + 100:
            return {"type": "ERROR", "message": "学生列表错误"}
	
    # 判断人数是否超过这个义工的人数上限
    st, r = OP.select("stuMax, nowStuCount","volunteer","volId=%d",volId,["stuMax","nowStuCount"])
    if not st: return r # 数据库错误
    if len(json_data['stulst']) > r["stuMax"] - r["nowStuCount"]:
        return {"type":"ERROR", "message":"人数超限"}
	
    # 判断人数是否超过班级人数上限
    st, r = OP.select("stuMax, nowStuCount","class_vol","volId=%d AND classId=%d",(volId,classId),["stuMax"])
    if not st: return r # 数据库错误
    if len(json_data['stulst']) > r["stuMax"] - r["nowStuCount"]:
        return {"type":"ERROR", "message":"人数超限"}
	
    # 修改数据库
    OP.update("nowStuCount=nowStuCount+%d","class_vol","volId=%d AND classId=%d",
        (len(json_data['stulst']),volId,classId)) # 修改每个班的记录
    OP.update("nowStuCount=nowStuCount+%d","volunteer","volId=%d",
        (len(json_data['stulst']),volId)) # 修改总的记录
    for i in json_data['stulst']:
        # 遍历每一个学生，加入一条未审核的记录
        OP.insert("volId,stuId,status,volTimeInside,volTimeOutside,volTimeLarge,thought",
            "stu_vol",(volId,i,0,0,0,""))
        # 审核过了以后再发义工时间
    return {"type":"SUCCESS","message":"添加成功"}

@Volunteer.route('/volunteer/create', methods = ['POST'])
@Deco
def createVolunteer():
	# 判断权限
    if not tkData.get("permission") in [2,4]:
        return {'type':'ERROR', 'message':"权限不足"}
	# 创建一条总的记录
    volId=OP.getLength("volunteer")
    OP.insert("volId,volName,volDate,volTime,stuMax,nowStuCount,description,status,"
		+"volTimeInside,volTimeOutside,volTimeLarge,holderId",
        "volunteer",
        (volId,json_data["name"],json_data["date"],json_data["time"],json_data["stuMax"],0
		json_data["description"],0,json_data["inside"],json_data["outside"],json_data["large"],tkData["userid"]))
		# 这里的status默认是0，如果规范修改了记得改一下
	# 在每个班的表里添加一条记录
	for i in json_data["class"]:
		OP.insert("volId,class,stuMax,nowStuCount","class_vol",volId,i["id"],i["stuMax"],0)
    return {"type":"SUCCESS", "message":"创建成功"}

@Volunteer.route('/volunteer/signerList/<int:volId>', methods = ['GET'])
@Deco
def getSignerList(volId):
	# 判断权限
    if not tkData.get("permission")<3:
        return {'type':'ERROR', 'message':"权限不足"}
    ret={"type":"SUCCESS", "message":"获取成功","result":[]}
    fl,r=OP.select("stuId","stu_vol","volId=%d",(volId),["stuId"],only=False)
    if not fl: return r # 数据库错误：没有这个义工
    for i in r: # 返回学生姓名
        ff,rr=OP.select("stuId,stuName","student","stuId=%d",i.get("stuId"),[])
        if not ff: return rr # 数据库错误：没有这个人
        ret["result"].append(rr)
    return ret

@Volunteer.route('/volunteer/choose/<int:volId>', methods = ['POST'])
def chooseVolunteer(volId):
    pass

@Volunteer.route('/volunteer/joinerList/<int:volId>', methods = ['GET'])
@Deco
def getJoinerList(volId):
    # 所以这个的意思是返回所有审核过了的报名的人吗？
    if not tkData.get("permission")<3:
        return {'type':'ERROR', 'message':"权限不足"}
    ret={"type":"SUCCESS", "message":"获取成功","result":[]}
    fl,r=OP.select("stuId","stu_vol","volId=%d and status=1",(volId),["stuId"],only=False)
    if not fl: return r # 数据库错误：没有这个义工
    for i in r: # 返回学生姓名
        ff,rr=OP.select("stuId,stuName","student","stuId=%d",i.get("stuId"),[])
        if not ff: return rr # 数据库错误：没有这个人
        ret["result"].append(rr)
    return ret

@Volunteer.route('/volunteer/thought/<int:volId>', methods = ['POST'])
def submitThought(volId):
    pass

@Volunteer.route('/volunteer/randomThought', methods=['GET'])
def randthought(): # 随机【钦定】一条感想（话说SQL怎么随机取一条数据啊）
    respdata = {'type':'SUCCESS', 'stuName':'用户名', 'stuId': 20200101, 'content':'这是感想内容'}
    return json.dumps(respdata)
