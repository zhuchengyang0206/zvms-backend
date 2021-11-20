# 这个文件用来存放一些通用的数据

# 学生完成的义工的状态
STATUS_WAITING =0 # 等待审核
STATUS_ACCEPT  =1 # 接受
STATUS_REJECT  =2 # 打回不可重新提交
STATUS_RESUBMIT=3 # 打回可重新提交
# 义工活动的状态
VOLUNTEER_WAITING  =0 # 等待审核
VOLUNTEER_AVAILABLE=1 # 可以报名
VOLUNTEER_FINISHED =2 # 报名截止
# 用户权限
PMS_CLASS  =0 # 每个班的团支书
PMS_TEACHER=1 # 教师
PMS_MANAGER=2 # 义管会
PMS_SYSTEM =3 # 系统

def checkPermission(cls,pms,stu): # 判断一个用户是否有权限管理该学生
	# 教师、义管会、系统能管理所有学生
	# 班级编号为6位：202001，学号为8位：20200100~20200199
	return pms in [PMS_CLASS,PMS_TEACHER,PMS_SYSTEM] or(pms==PMS_CLASS and stu>=cls*100 and stu<cls*100+100)

CURRENT_VERSION = "7659efa34712b560a174dd090e605c1c"
CURRENT_VERSION_ERROR_MESSAGE = "服务器维护中"
