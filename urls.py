from application import app
from web.controllers.user.User import router_user
from web.controllers.index import route_index

# 拦截
from web.interceptors.Authlnterceptor import *

app.register_blueprint(router_user,url_prefix='/user')
app.register_blueprint(route_index,url_prefix="/")

