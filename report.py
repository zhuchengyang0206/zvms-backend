from flask import Blueprint, request
import json
from deco import *
from res import *
import oppressor as OP
import datetime

Report = Blueprint('report', __name__)

@Report.route('/report', methods = ['GET', 'OPTIONS', 'POST'])
@Deco
def submitReport_NoToken():
    report = json_data().get('report')
    f = open('./report.log', 'a+')
    # 2021.11.22 10.40 Modified by nekomoyi
    f.write('[' + datetime.datetime.now() + '] ' + report + '\n')
    f.close()
    return {"type":"SUCCESS", "message":"提交成功"}
