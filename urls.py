from application import app
from web.controllers.user.User import router_user
from web.controllers.index import route_index
from web.controllers.Account.Account import router_account
from web.controllers.member.Member import router_member

# 拦截
from web.interceptors.Authlnterceptor import *

app.register_blueprint(router_user,url_prefix='/user')
app.register_blueprint(route_index,url_prefix="/")
app.register_blueprint(router_account,url_prefix="/account")
app.register_blueprint(router_member,url_prefix="/member") 
