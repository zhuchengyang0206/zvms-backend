from flask import request
from functools import wraps
import tokenlib as TK
import json

# 我不知道还有没有更好的方法，如果有的话麻烦把下面这几行改掉
postdata={}
def json_data():
    return postdata

tkst=TK.BAD
tkdata={}
def tkStatus():
    return tkst

def tkData():
    return tkdata

# 以后把调试的代码写在这边，把一些公用的功能也可以移到这边
# 在所有函数名前面加上@Deco
# 这样路由的函数直接返回一个字典就好了
def Deco(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Enter->%s"%func.__name__)
        global postdata, tkst, tkdata # 重要！！
        try: # 为了防止空POST出锅
            postdata=json.loads(request.get_data().decode("utf-8"))
            print(postdata)
        except:
            postdata=""
        
        try: # 获取Token
            tkst, tkdata=TK.readToken(json_data().get('token'))
            print(tkst, tkdata)
        except:
            tksk=TK.ERROR
            tkdata={}
        
        try:
            ret=func(*args,**kwargs)
        except:
            ret={'type':'ERROR','message':'未知错误'}
        return json.dumps(ret)
    return wrapper