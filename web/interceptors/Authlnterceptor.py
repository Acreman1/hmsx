from flask import request,redirect

from common.libs.UrlManager import UrlManager
from application import app

import re

@app.before_request
def before_request():
    path = request.path

    user_info = check_login()
    if not user_info:
        return redirect(UrlManager.builduUrl("/user/login"))

    return
    
# 判断用户是否登录
def check_login():
    return 

