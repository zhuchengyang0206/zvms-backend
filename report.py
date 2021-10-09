from flask import Blueprint, request
import json
from deco import *
from res import *
import oppressor as OP

Report = Blueprint('report', __name__)

@Report.route('/report', methods = ['GET', 'OPTIONS', 'POST'])
@Deco
def submitReport_NoToken():
    report = json_data().get('report')
    f = open('./report.log', 'a+')
    f.write(report + '\n')
    f.close()
    return {"type":"SUCCESS", "message":"提交成功"}