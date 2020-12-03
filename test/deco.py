from flask import request
from functools import wraps
import json

# 我不知道还有没有更好的方法，如果有的话麻烦把下面这三行改掉
post_data={}
def json_data():
    return post_data

# 以后把调试的代码写在这边，把一些公用的功能也可以移到这边
# 在所有函数名前面加上@Deco
# 这样路由的函数直接返回一个字典就好了
def Deco(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Enter->%s"%func.__name__)
        global post_data
        post_data=json.loads(request.get_data().decode("utf-8"))
        try:
            ret=func(*args,**kwargs)
        except:
            ret={'type':'ERROR','message':'未知错误'}
        return json.dumps(ret)
    return wrapper