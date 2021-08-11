import json
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature

ERROR = 0
SUCCESS = 1
EXPIRED = 2
BAD = 3

SECRET_KEY = "譋窹乆乣詈"
SALT = "詈乆窹乣譋 "
EXPIRES_IN = 3600

def generateToken(data):
    global SECRET_KEY, SALT, EXPIRES_IN
    s = TimedJSONWebSignatureSerializer(secret_key=SECRET_KEY, expires_in=EXPIRES_IN, salt=SALT)
    return s.dumps(data).decode('ascii')

def readToken(token):
    global SECRET_KEY, SALT, EXPIRES_IN
    global ERROR, SUCCESS, EXPIRED, BAD
    s = TimedJSONWebSignatureSerializer(secret_key=SECRET_KEY, salt=SALT)
    st = ERROR
    data = {}
    try:
        data = s.loads(token)
        st = SUCCESS
    except SignatureExpired:
        st = EXPIRED
    except BadSignature:
        st = BAD
    return st, data
