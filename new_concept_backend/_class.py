import oppressor as OP

def getClassList(ext):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}
    if ext[Auth] >= 1:
        st, val = OP.classList()
        if st:
            respdata['type'] = "SUCCESS"
            respdata['message'] = "获取成功"
            respdata['class'] = [] # 列表初始化
            for i in val:
                respdata['class'].append(
                    {'id': i, 'name': OP.classIdToString(i)})
        else:
            respdata.update(val)
    else:
        respdata['message'] = "权限错误！"
    return respdata

def getStudentList(classId, ext):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}  # 定义默认返回值
    if ext["Auth"] > 1 or classId == ext["Class"]:
        st, val = OP.studentList(classId)
        if st:
            respdata['type'] = "SUCCESS"
            respdata['message'] = "获取成功"
            respdata['student'] = []
            for i in val:
                respdata['student'].append(
                    {'id': i[0], 'name': i[1], 'inside': i[2], 'outside': i[3], 'large': i[4]})
        else:
            respdata.update(val)
    else:
        respdata['message'] = "权限错误！"
    return respdata

def getClassVolunteer(classId):
    respdata = {'type': 'ERROR', 'message': '未知错误!'}
    st, val = OP.getClassVolunteerList(classId)
    if st:
        respdata['volunteer'] = []
        for i in r:
            st1, val1 = OP.getVolunteerInfo(i)
            if st1:
                respdata['volunteer'].append(OP.listToDict_volunteer_faultless(val1))
            else:
                respdata.update(val1)
                break
        else:
            respdata['type'] = 'SUCCESS'
            respdata['message'] = '获取成功'
    else:
        respdata.update(val)
    return respdata