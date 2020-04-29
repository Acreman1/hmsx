# 设置服务器端口
SERVER_PORT = 5210

# 连接到数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/hmsc_db?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# cookie
AUTH_COOKIE_NAME = "hmsx"


# 拦截器忽略规则
IGNORE_URLS = [
    "^/user/login"
]
IGNORE_HCECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

STATUS = {
    "1":"正常",
    "0":"已删除"
}