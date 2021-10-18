from flask import Blueprint, request
import json
import time
from deco import *
from res import *
import oppressor as OP

Volunteer = Blueprint('volunteer', __name__)

@Volunteer.route('/volunteer/list', methods = ['GET', 'OPTIONS']) # 这里不需要参数传入，使用GET方式。下同
@Deco
def getVolunteerList(): # 可以了
	fl,r=OP.select("volId,volName,description,volDate,volTime,status,stuMax","volunteer","true",(),
	              ["id", "name", "description","date","time","status","stuMax"],only=False)
	if not fl: return r # 数据库错误
	r=sorted(r,key=lambda x: x["date"])
	return {"type":"SUCCESS","message":"获取成功","volunteer":r[::-1]}

@Volunteer.route('/volunteer/fetch/<int:volId>', methods = ['GET', 'OPTIONS'])
@Deco
def getVolunteer(volId): # 可以了
	fl,r=OP.select("volName,volDate,volTime,stuMax,nowStuCount,description,status,volTimeInside,volTimeOutside,volTimeLarge",
				  "volunteer","volId=%s",(volId),
		          ["name", "date", "time", "stuMax","stuNow","description","status","inside",  "outside",     "large"])
	if not fl: return r # 数据库错误
	r.update({"type":"SUCCESS","message":"获取成功"})
	return r

# 判断班级人数是否超限
# 义工vol，在cls班里再报名dlt个人
def checkStuLimit(vol,cls,dlt): # 过了
	# print("Checking:",vol,cls,dlt)
	fl,r=OP.select("stuMax,nowStuCount","class_vol","volId=%s AND class=%s",(vol,cls),["stuMax","nowStuCount"])
	if not fl:
		if r["message"]=="数据库信息错误：未查询到相关信息":
			r["message"]="班级%d无法报名该义工"%cls
			return False,r
		else: return False,r
	if r["nowStuCount"]+dlt>r["stuMax"]:
		return False,{"type":"ERROR","message":"班级%d人数超限"%cls}
	return True,{}

# 判断义工人数是否合法
# 传入字典（直接用postdata就好）至少有以下内容：
# {"stuMax":233,"class":[{"id":202001,"stuMax":10},...]}
def checkStudentCount(js): # 过了
	# 传入json
	# 如果最大人数大于每个班最大人数之和那么永远报不满
	print("Entered checkStudentCount.")
	mx=js["stuMax"]
	for i in js["class"]: mx-=i["stuMax"]
	return mx<=0

@Volunteer.route('/volunteer/signup/<int:volId>', methods = ['POST'])
@Deco
def signupVolunteer(volId): # 过了
	# 判断权限
	for i in json_data()['stulst']:
		if not checkPermission(tkData()["class"],tkData()["permission"],i):
			return {"type":"ERROR", "message":"权限不足：学生列表中有别班学生"}
	# 判断人数是否超过这个义工的人数上限
	fl,r=OP.select("stuMax,nowStuCount,volDate,volTime","volunteer","volId=%s",(volId),["stuMax","nowStuCount","volDate","volTime"])
	if not fl: return r # 数据库错误
	if len(json_data()['stulst'])>r["stuMax"]-r["nowStuCount"]:
		return {"type":"ERROR", "message":"人数超限"}
	nowTime=time.time()
	endTime=time.mktime(time.strptime(r["volDate"] + ' ' + r["volTime"], "%Y-%m-%d %H:%M"))
	if nowTime > endTime:
		return {"type":"ERROR", "message":"义工时间已过"}
	# 判断是否有人已经报名了
	for i in json_data()["stulst"]:
		fl,r=OP.select("status","stu_vol","volId=%s AND stuId=%s",(volId,i),["status"])
		# 理论上所有人都没有在数据库里面
		if not (fl==False and r["message"]=="数据库信息错误：未查询到相关信息"):
			return {"type":"ERROR", "message":"学生%d已经报名，不可重复报名！"%i}
	# 判断人数是否超过班级人数上限
	# 先统计每个班级报名人数
	num={} # {202001:233,202002:234,...}
	for i in json_data()['stulst']:
		cur=i//100 # 获取学生的班级
		if cur in num: num[cur]+=1
		else: num[cur]=1
	for i in num: # 分别检查每个班的报名
		fl,r=checkStuLimit(volId,i,num[i])
		if not fl: return r
	# 修改数据库
	OP.update("nowStuCount=nowStuCount+%s","volunteer","volId=%s",
		(len(json_data()['stulst']),volId)) # 修改总的记录
	for i in num:
		OP.update("nowStuCount=nowStuCount+%s","class_vol","volId=%s AND class=%s",
			(num[i],volId,i)) # 修改每个班的记录
	for i in json_data()['stulst']:
		# 遍历每一个学生，加入一条未审核的记录
		OP.insert("volId,stuId,status,volTimeInside,volTimeOutside,volTimeLarge,thought",
			"stu_vol",(volId,i,STATUS_WAITING,0,0,0,""))
		# 审核过了以后再发义工时间
	return {"type":"SUCCESS","message":"添加成功"}

@Volunteer.route('/volunteer/create', methods = ['POST','OPTIONS'])
@Deco
def createVolunteer(): # 大概可以了
	# 判断权限，教师、义管会、系统可以创建义工
	# print(2333)
	# print(tkData())
	if not tkData().get("permission") in [PMS_TEACHER,PMS_MANAGER,PMS_SYSTEM]:
		print("Pemission Denied.")
		return {'type':'ERROR', 'message':"权限不足"}
	print("Permission verified.")
	print(json_data())
	if not checkStudentCount(json_data()): # HERE! PARAMTERS ERROR!
		print("count check failed.")
		return {"type":"ERROR", "message":"最大人数不符合要求：义工人数永远无法报满"}
	print(666)
	if json_data()["inside"]<=0 or json_data()["outside"]<=0 or json_data()["large"]<=0:
		return {"type":"ERROR", "message":"义工时间不能为负数"}
	# 创建一条总的记录
	OP.insert("volName,volDate,volTime,stuMax,nowStuCount,description,status,"
		+"volTimeInside,volTimeOutside,volTimeLarge,holderId",
		"volunteer",
		(json_data()["name"],json_data()["date"],json_data()["time"],json_data()["stuMax"],0,
		json_data()["description"],VOLUNTEER_WAITING,json_data()["inside"],json_data()["outside"],json_data()["large"],tkData()["userid"]))
	# 因为volunteer表里面是AUTO_INCREMENT，所以insert的时候volId自动加一
	# 所以下面要获取当前的volId以供后面操作（为了防止一些奇奇怪怪的锅用了三项）
	fl,r=OP.select("volId","volunteer","volName=%s AND volDate=%s AND volTime=%s",
		(json_data()["name"],json_data()["date"],json_data()["time"]),["id"])
	if not fl: return r # 理论上这个错误不可能发生
	volId=r["id"]
	# 在每个班的表里添加一条记录
	for i in json_data()["class"]:
		OP.insert("volId,class,stuMax,nowStuCount","class_vol",(volId,i["id"],i["stuMax"],0))
	return {"type":"SUCCESS", "message":"创建成功"}

@Volunteer.route('/volunteer/signerList/<int:volId>', methods = ['GET'])
@Deco
def getSignerList(volId): # 过了
	# 判断权限
	# if not tkData().get("permission") in [PMS_TEACHER,PMS_MANAGER,PMS_SYSTEM]:
	# 	return {'type':'ERROR', 'message':"权限不足"}
	ret={"type":"SUCCESS", "message":"获取成功","result":[]}
	fl,r=OP.select("stuId","stu_vol","volId=%s",(volId),["stuId"],only=False)
	if not fl: return r # 数据库错误：没有这个义工
	for i in r: # 返回学生姓名
		ff,rr=OP.select("stuId,stuName","student","stuId=%s",(i["stuId"]),["stuId","stuName"])
		if not ff: return rr # 数据库错误：没有这个人
		ret["result"].append(rr)
	return ret

'''
@Volunteer.route('/volunteer/choose/<int:volId>', methods = ['POST'])
def chooseVolunteer(volId):
	pass

@Volunteer.route('/volunteer/joinerList/<int:volId>', methods = ['GET'])
@Deco
def getJoinerList(volId): # 这个到底要不要？
	# 所以这个的意思是返回所有审核过了的报名的人吗？
	if not tkData().get("permission")<3:
		return {'type':'ERROR', 'message':"权限不足"}
	ret={"type":"SUCCESS", "message":"获取成功", "result":[]}
	fl,r=OP.select("stuId","stu_vol","volId=%s AND status=1",(volId),["stuId"],only=False)
	# 这里的审核通过是1，如果改了记得改
	if not fl: return r # 数据库错误：没有这个义工
	for i in r: # 返回学生姓名
		ff,rr=OP.select("stuId,stuName","student","stuId=%s",i.get("stuId"),[])
		if not ff: return rr # 数据库错误：没有这个人
		ret["result"].append(rr)
	return ret
'''

@Volunteer.route('/volunteer/unaudited', methods=['GET'])
@Deco
def getUnaudited():
	fl,r=OP.select("volId,stuId,thought","stu_vol","((status=%s)and length(thought)>0)",(STATUS_WAITING),["volId","stuId","thought"],only=False)
	if not fl:
		if r["message"]=="数据库信息错误：未查询到相关信息":
			r={"type":"SUCCESS","message":"全部审核完毕"}
		return r
	return {"type":"SUCCESS","message":"获取成功","result":r}

@Volunteer.route('/volunteer/audit/<int:volId>', methods = ['POST'])
@Deco
def auditThought(volId): # 大概是过了
	# 判断权限，只有义管会和系统可以审核
	if not tkData()["permission"] in [PMS_MANAGER,PMS_SYSTEM]:
		return {'type':'ERROR', 'message':"权限不足"}
	# 判断状态是否可以审核
	for i in json_data()["thought"]:
		fl,r=OP.select("status","stu_vol","volId=%s AND stuId=%s",(volId,i["stuId"]),["status"])
		if not fl: return r
		if r["status"]==STATUS_ACCEPT:
			return {"type":"ERROR", "message":"学生%d已过审，不可重复审核"%i["stuId"]}
		if r["status"]==STATUS_REJECT:
			return {"type":"ERROR", "message":"学生%d不可重新提交"%i["stuId"]}
	# 修改数据库
	for i in json_data()["thought"]:
		stuId=i["stuId"]
		if i["status"]!=STATUS_ACCEPT:
                        OP.update("thought=%s","stu_vol","volId=%s AND stuId=%s",("",volId,stuId))
		# 修改状态。状态由JSON传入
		OP.update("status=%s","stu_vol","volId=%s AND stuId=%s",(i["status"],volId,stuId))
		# 把stu_vol的表里的数据填上
		OP.update("volTimeInside=%s","stu_vol","volId=%s AND stuId=%s",(i["inside"],volId,stuId))
		OP.update("volTimeOutside=%s","stu_vol","volId=%s AND stuId=%s",(i["outside"],volId,stuId))
		OP.update("volTimeLarge=%s","stu_vol","volId=%s AND stuId=%s",(i["large"],volId,stuId))
		# 修改学生数据
		OP.update("volTimeInside=volTimeInside+%s","student","stuId=%s",(i["inside"],stuId))
		OP.update("volTimeOutside=volTimeOutside+%s","student","stuId=%s",(i["outside"],stuId))
		OP.update("volTimeLarge=volTimeLarge+%s","student","stuId=%s",(i["large"],stuId))
		# 如果SQL的update可以一次修改多列的话麻烦把上面改了
	return {"type":"SUCCESS", "message":"审核成功"}

@Volunteer.route('/volunteer/holiday', methods=['POST'])
@Deco
def holidayVolunteer():
	# 判断是否是本班的人
	# 这里义管会和系统是不可以的（因为后面关联到班级的时候必须要有一个classId）
	# 真要改也不是不可以。在后面统计学生列表中出现过的班级。
	print(json_data())
	print(json_data()["stuId"],tkData()["class"])
	for i in json_data()["stuId"]:
		if not tkData()["class"]==i//100:
			return {"type":"ERROR", "message":"权限不足：学生列表中有别班学生"}
	stulen=len(json_data()["stuId"])
	print(2333)
	print(stulen)
	print(json_data()["name"],json_data()["date"],json_data()["time"],stulen,stulen)
	print(json_data()["description"],VOLUNTEER_WAITING,json_data()["inside"],json_data()["outside"],json_data()["large"],tkData()["userid"])
	#  先创建一个义工（照搬Create）
	OP.insert("volName,volDate,volTime,stuMax,nowStuCount,description,status,"
		+"volTimeInside,volTimeOutside,volTimeLarge,holderId",
		"volunteer", # 初始把所有学生报进去
		(json_data()["name"],json_data()["date"],json_data()["time"],str(stulen),str(stulen),
		json_data()["description"],str(VOLUNTEER_WAITING),json_data()["inside"],json_data()["outside"],json_data()["large"],tkData()["userid"]))
	# 获取volId
	fl,r=OP.select("volId","volunteer","volName=%s AND volDate=%s AND volTime=%s",
		(json_data()["name"],json_data()["date"],json_data()["time"]),["id"])
	if not fl: return r # 理论上这个错误不可能发生
	volId=r["id"]
	# 在每个班的表里添加一条记录
	OP.insert("volId,class,stuMax,nowStuCount","class_vol",(volId,tkData()["class"],str(stulen),str(stulen)))
	# 给每个学生一条记录
	for i in json_data()["stuId"]:
		OP.insert("volId,stuId,status,volTimeInside,volTimeOutside,volTimeLarge,thought",
			"stu_vol",(str(volId),str(i),str(STATUS_WAITING),'0','0','0',""))
	return {"type":"SUCCESS", "message":"提交成功"}

'''暂时去掉
@Volunteer.route('/volunteer/modify/<int:volId>', methods = ['POST'])
@Deco
def modifyVolunteer(volId):
	# 判断权限，教师、义管会和系统（也即可以创建义工的）可以修改
	if not tkData()["permission"] in [PMS_TEACHER,PMS_MANAGER,PMS_SYSTEM]:
		return {"type":"ERROR", "message":"权限不足"}
	if not checkStudentCount(json_data()):
		return {"type":"ERROR", "message":"最大人数不符合要求：义工人数永远无法报满"}
	# 最大人数大于当前报名人数
	fl,r=OP.select("nowStuCount","volunteer","volId=%s",(volId),["now"])
	if not fl: return r
	if json_data()["stuMax"]<r["now"]:
		return {"type":"ERROR", "message":"最大人数不得小于当前报名人数"}
	for i in json_data()["class"]:
		fl,r=OP.select("nowStuCount","class_vol","volId=%s AND ",)
	# 创建一条总的记录
	volId=OP.getLength("volunteer")
	OP.insert("volId,volName,volDate,volTime,stuMax,nowStuCount,description,status,"
		+"volTimeInside,volTimeOutside,volTimeLarge,holderId",
		"volunteer",
		(volId,json_data()["name"],json_data()["date"],json_data()["time"],json_data()["stuMax"],0
		json_data()["description"],VOLUNTEER_WAITING,json_data()["inside"],json_data()["outside"],json_data()["large"],tkData()["userid"]))
	# 在每个班的表里添加一条记录
	for i in json_data()["class"]:
		OP.insert("volId,class,stuMax,nowStuCount","class_vol",(volId,i["id"],i["stuMax"],0))
	return {"type":"SUCCESS", "message":"创建成功"}
	return {"type":"SUCCESS", "message":"修改成功"}
{
    "name": "义工活动1",
    "date": "2020.10.1",
    "time": "13:00",
    "stuMax": 20,
    "description": "...",
    "inside": 0,
    "outside": 3,
    "large": 0,
    "class": [
        {"id": 202001, "stuMax": 10, "visible": true},
        {"id": 202002, "stuMax": 5, "visible": true},
        {"id": 202003, "stuMax": 10, "visible": true}
        {"id": 202004, "stuMax": 0, "visible": false},
    ]
}
'''

@Volunteer.route('/volunteer/thought/<int:volId>', methods = ['POST'])
@Deco
def submitThought(volId): # 大概是过了
	# 判断权限
	for i in json_data()["thought"]:
		if not checkPermission(tkData()["class"],tkData()["permission"],i):
			return {"type":"ERROR","message":"权限不足：学生列表中有别班学生"}
	# 判断状态是否可以提交
	for i in json_data()["thought"]:
		fl,r=OP.select("status","stu_vol","volId=%s AND stuId=%s",(volId,i["stuId"]),["status"])
		if not fl: return r # 数据库错误
		if r["status"]==STATUS_ACCEPT:
			return {"type":"ERROR", "message":"学生%d已过审，不可重复提交"%i["stuId"]}
		if r["status"]==STATUS_REJECT:
			return {"type":"ERROR", "message":"学生%d不可重新提交"%i["stuId"]}
	# 修改数据库
	for i in json_data()["thought"]:
		OP.update("thought=%s","stu_vol","volId=%s and stuId=%s",(i["content"],volId,i["stuId"]))
		OP.update("status=%s","stu_vol","volId=%s and stuId=%s",(STATUS_WAITING,volId,i["stuId"]))
	return {"type":"SUCCESS","message":"提交成功"}

@Volunteer.route('/volunteer/randomThought', methods=['GET'])
def randthought(): # 随机一条感想
	# respdata = {'type':'ERRR',"message": "感想获取不到"}
	respdata = {'type':'SUCCESS',"message": "感想获取不到"}
	cnt = 0
	while True:
		cnt += 1
		if cnt > 10: break   # 说明系统刚上线
		r = OP.getRandThought()
		if r == None: break
		if r[2] == 1:
			name = OP.select("stuName", "student", "stuId=%s", (r[1]), ["name"])["name"]
			respdata = {"type": "SUCCESS", "stuId": r[1], "stuName": name, "content": r[7]}
			break
	return json.dumps(respdata)
