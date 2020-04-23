from flask import Blueprint,render_template


router_user = Blueprint('user_page',__name__)

@router_user.route("/login")
def login():
    return render_template("user/login.html")

@router_user.route("/logout")
def logout():
    return "logput"

@router_user.route("/edit")
def edit():
    return "edit"

@router_user.route("/rest-pwd")
def restPwd():
    return "rest-pwd"