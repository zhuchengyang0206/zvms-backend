# 随手打的一个词竟然还真的有，那就用这个名吧
# 这个文件封装了一些针对数据库的操作
import database as DB

thisYear = 2020 # 以后要改成自动获取
# 并且这个应该是指学年而不是当前年份
# 这个函数被用到的地方：_class.py
def classIdToString(a):
	global thisYear
	id = int(a)
	_year = id // 100
	_class = id % 100
	ret = ""
	# 特殊身份的判断 # 这些东西要放到文档里
	# 教师 100001 100002
	# 管理员 110001 110002
	# 系统 120003 120004
	if _year//100 == 10:
		ret = "教师"
		return ret
	elif _year//100 == 11:
		ret = "管理员"
		return ret
	elif _year//100 == 12:
		ret = "系统"
		return ret
	
	if _class <= 10:
		ret = ret + "高"
	elif _class <= 17:
		ret = ret + "蛟"
	if _year == thisYear:
		ret = ret + "一"
	elif _year == thisYear - 1:
		ret = ret + "二"
	elif _year == thisYear - 2:
		ret = ret + "三"
	ret = ret + (["NULL","1","2","3","4","5","6","7","8","9","10","NULL","2","3","4","5","6","7"])[_class] #如果我没记错的话校徽是这样的
	ret = ret + "班"

	return ret

# 下面三个是对MySQL操作的封装
# 对SQL的操作尽量使用这三个而不是直接DB.execute()
# 标出来的是调试输出
# 注意：SQL中传入的所有参数要使用%s（我也不知道为什么，但是是对的）
def select(col,src,exp,val,ret,only=True): # 估计能用了
	# col:选择的列，字符串 src:从哪张表，字符串 exp:条件，字符串
	# val:传入的数据，元组 ret:返回的格式，列表，内容为字符串，为[]则为col
	# only:是否只取一个
	# 返回值:一个布尔值、一个字典，格式由ret决定（若only=False则为一个数组）
	s="SELECT %s FROM %s WHERE %s;"%(col,src,exp)
	print("Selecting:",s,val) # 生成的SQL语句和参数 #
	DB.execute(s,val)
	r=DB.fetchall()
	print("Select Result:",r) # SQL返回值 #
	if ret==[]: # 这个尽量避免使用吧，可能会有奇奇怪怪的锅（本来还想偷点懒的）
		ret=list(col.split(","))
		for i in len(ret): ret[i]=ret[i].strip()
	if len(r)==0:
		return False, {"type":"ERROR","message":"数据库信息错误：未查询到相关信息"}
	if len(r)==1:
		result={} # 格式化返回值
		for j in range(0,len(ret)):
			result.update({ret[j]: r[0][j]})
		if only: return True, result
		else: return True, [result] # 就算只有一个，没有Only还是要返回数组
	else:
		if only: # 理论上不应该有这种情况，真出现了估计是Insert的锅
			return False, {"type":"ERROR","message":"数据库信息错误：要求一个但查询到多个"}
		result=[]
		for i in range(0,len(r)):
			result.append({}) # 格式化返回值
			for j in range(0,len(ret)):
				result[i].update({ret[j]: r[i][j]})
		return True, result

# ！！！注意！！！下面两个函数是没有返回值的！！！
# fl,r=OP.update(...) 错！
# OP.update(...) 对！
def update(col,src,exp,val): # 估计能用了
	# 参数同上
	s="UPDATE %s SET %s WHERE %s;"%(src,col,exp)
	print("Updating:",s,val) # 生成的SQL语句和参数 #
	DB.execute(s,val)
	r=DB.fetchall()

def insert(col,src,val): # 估计能用了
	# 参数同上
	print(col)
	print(src)
	print(val)
	tmp=("%s,"*len(val))[:-1]
	print(tmp)
	s="INSERT INTO %s (%s) VALUES (%s);"%(src,col,tmp)
	print("Inserting:",s,val) # 生成的SQL语句和参数 #
	DB.execute(s,val)
	r=DB.fetchall()

def getRandThought():
	s="SELECT * FROM stu_vol ORDER BY status DESC, RAND() DESC LIMIT 1;"
	DB.execute(s)
	return DB.fetchone()

# 获取一个表中有多少行记录
# （到目前）只被用于获取volId
# 是不是可以用来随机获取一条数据？
# 这东西现在看来好像没什么用，只要设置AUTO_INCREMENT就好了
def getLength(src): # 还未调试！
	s="SELECT MAX(ROWNUM) FROM %s"%src
	print("Get Length:",s,src) # 生成的SQL语句和参数 #
	DB.execute(s)
	r=DB.fetchall()
	print("Length:",r) # SQL返回值 #
	return r[0]
	
# 下面两个函数本来是想改掉的，但是他们（到目前为止）没有任何锅，
# 并且和别的函数也没有关系，暂时先放一下。
# 被使用到的地方：user.py
def user2dict(v):
	return { "username":v[1], "class":v[2],
		"permission":v[3], "classname":classIdToString(v[2])
	}

def userLogin(userId, password):
	if isinstance(userId, str) and isinstance(password, str): # 其实传入的都是str类型
		DB.execute("SELECT * FROM user WHERE userId = %s AND password = %s;", (userId, password))
		r = DB.fetchall()
		if len(r) == 0:
			return False, {"message":"用户ID或密码错误"}
		elif len(r) > 1:
			return False, {"message":"数据库信息错误：要求一个但查询到多个"}
		else:
			return True, r[0]
	else:
		return False, {"message": "请求接口错误"}

# 其他一些就都暂时没用了，在这个分支上先删了
