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
        print("Entering Function->%s:"%func.__name__)
        global postdata, tkst, tkdata # 重要！！
        try: # 为了防止空POST出锅
            postdata=json.loads(request.get_data().decode("utf-8"))
            print("Postdata:",postdata)
        except:
            postdata=""
            print("No Postdata loaded.")

        if not "NoToken" in func.__name__:
        # 为了判断是否需要Token验证
        # 我知道这很不好，但是带参数的修饰器和Flask冲突了（估计是）
        # 所以请在不用Token的函数名后面加上"_NoToken"
            try: # 获取Token
                tkst, tkdata=TK.readToken(request.headers.get("Authorization")) # 改了一下
                print("Loading Token:",tkst, tkdata)
                if tkst==TK.EXPIRED:
                    return json.dumps({'type':'ERROR', 'message':"token过期"})
                elif tkst==TK.BAD:
                    return json.dumps({'type':'ERROR', 'message':"token失效"})
            except:
                tksk=TK.ERROR
                tkdata={}
                return json.dumps({'type':'ERROR', 'message':"未获取到Token"})
        
        try:
            return json.dumps(func(*args,**kwargs))
        except:
            return json.dumps({'type':'ERROR','message':'未知错误'})
    return wrapper