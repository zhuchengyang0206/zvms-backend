import user
import _class

# 传入传出的都是字典，而非 json
# 这里的话 session 就不关我什么事咯

def exec(url, param, Auth, Class): #  Auth 是权限 Class 是班级
                                   # 首字母大写的就是要从 session 里面读的
    if "user/login" in url:
        return user.login(param)
    if "user/logout" in url:
        return user.logout()
    if "class/list" in url:
        return _class.getClassList(Auth, Class)
    if "class/stulist/" in url:
        return _class.getStudentList(int(url[url.find("class/stulist/")+len("class/stulist/"):]), Auth, Class)
    if "class/volunteer/" in url:
        return _class.getClassVolunteer(int(url[url.find("class/volunteer/")+len("class/volunteer/"):]))