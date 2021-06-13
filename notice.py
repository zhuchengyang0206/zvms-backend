from flask import Blueprint, request
import json
from deco import *
import oppressor as OP

Notice = Blueprint('notice', __name__)

@Notice.route('/notice/new', methods = ['POST'])
@Deco
def newNotice():
	pass

@Notice.route('/notice/query', methods = ['GET'])
@Deco
def queryNotice():
	pass

@Notice.route('/notice/modify/<ntcId>', methods = ['POST'])
@Deco
def modifyNotice(ntcId):
	pass
