from flask import Blueprint,render_template,request,jsonify,make_response,redirect,g

from common.models.User import User
from common.libs.user.UserService import UserService
from common.libs.UrlManager import UrlManager
from common.libs.Helper import ops_render
from application import app,db
import json

router_user = Blueprint('user_page',__name__)

@router_user.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        if g.current_user:
            return redirect(UrlManager.builduUrl("/"))
        return ops_render('user/login.html')
    resp = {
        'code':200,
        'msg':'登录成功',
        'data':{}
    }
    req=request.values
    login_name = req['login_name']
    login_pwd = req['login_pwd']
    # 校检
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的用户名"
        return jsonify(resp)
    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的密码"
        return jsonify(resp)
        
    # 数据库比对
    user_info = User.query.filter_by(login_name=login_name).first()
    
    if not user_info:
        resp["code"] = -1
        resp["msg"] = "用户不存在"
        return jsonify(resp)
    if user_info.status != 1:
        resp["code"] = -1
        resp["msg"] = "账号已经禁用"
        return jsonify(resp)
    if user_info.login_pwd != UserService.generatePwd(login_pwd,user_info.login_salt):
        resp["code"] = -1
        resp["msg"] = "密码错误"
        return jsonify(resp)

    # 将用户信息存入到浏览器的Cookie中
    # json.dumps()处理dict,list 类型，经过处理后可以直接在浏览器中使用
    response = make_response(json.dumps({'code':200,'msg':'登录成功'}))
    # name  value  过期时间
    # value包括login_name  login_pwd  login_salt  uid
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],'%s@%s'%(UserService.generateAuthCode(user_info=user_info),user_info.uid),60*60*24*5)

    return response

@router_user.route("/edit",methods=["GET","POST"])
def edit():
    if request.method == "GET":
        return ops_render("/user/edit.html")
    resp = {
        "code":200,
        "msg":"编辑成功",
        "data":{}
    }
    rep = request.values
    nickname = rep['nickname'] if 'nickname' in rep else ''
    email = rep['email'] if 'nickname' in rep else ''

    # 校检
    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = "请正确输入名字"
        return jsonify(resp)

    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = "email不符合规范"
        return jsonify(resp)

    # 跟新数据库
    user_info = g.current_user
    user_info.nickname = nickname
    user_info.email = email

    db.session.add(user_info)
    db.session.commit()

    return jsonify(resp)

@router_user.route("/reset-pwd",methods=["GET","POST"])
def resetPwd():
    if request.method == "GET":
        return ops_render("/user/reset_pwd.html")
    resp = {
        "code":200,
        "msg":"ok",
        "data":{}
    }
    rep = request.values
    old_password = rep['old_password'] if "old_password" in rep else ''
    new_password = rep['new_password'] if "new_password" in rep else ''
    # 校检
    if old_password is None or len(old_password) < 6:
        resp['code'] = -1
        resp['msg'] = "原密码错误"
        return jsonify(resp)

    if new_password is None or len(new_password) < 6:
        resp['code'] = -1
        resp['msg'] = "新密码错误"
        return jsonify(resp)

    if new_password == old_password:
        resp['code'] = -1
        resp['msg'] = "新密码与旧密码相同"
        return jsonify(resp)

    # 获取用户信息,修改密码
    user_info = g.current_user
    user_info.login_pwd = UserService.generatePwd(new_password,user_info.login_salt)
    db.session.add(user_info)
    db.session.commit()

    # 跟新cookie的密码
    response = make_response(json.dumps(resp))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],"%s@%s" % (UserService.generateAuthCode(user_info),user_info.uid),60*60*24*5)

    return response


@router_user.route("/logout")
def logout():
    response = make_response(redirect(UrlManager.builduUrl("/user/login")))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response 