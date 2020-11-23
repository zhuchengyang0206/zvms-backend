import user
import _class

# 传入传出的都是字典，而非 json

def exec(url, param, ext): #  ext[Auth] 是权限  ext[Class] 是班级
                           # ext 从 session 里面读
    if "user/login" in url:
        return user.login(param)
    if "user/logout" in url:
        return user.logout()
    if "class/list" in url:
        return _class.getClassList(ext)
    if "class/stulist/" in url:
        return _class.getStudentList(int(url[url.find("class/stulist/")+len("class/stulist/"):]), ext)
    if "class/volunteer/" in url:
        return _class.getClassVolunteer(int(url[url.find("class/volunteer/")+len("class/volunteer/"):]))