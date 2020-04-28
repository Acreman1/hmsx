import hashlib,base64,random,string

class UserService():
    # 生成密码
    @staticmethod
    def generatePwd(pwd,salt):
        m = hashlib.md5()
        str = "%s-%s"%(base64.encodebytes(pwd.encode("utf-8")),salt)
        m.update(str.encode("utf-8"))

        return m.hexdigest()

    @staticmethod
    def generateAuthCode(user_info=None):
        m = hashlib.md5()
        str = "%s-%s-%s-%s"%(user_info.uid,user_info.login_name,user_info.login_pwd,user_info.login_salt)
        m.update(str.encode('utf-8'))

        return m.hexdigest()

    # 生成一个16位的加密字符串
    @staticmethod
    def generateSalt(length = 16):
        list = [random.choice((string.ascii_letters + string.digits)) for i in range(16)]
        return (''.join(list))

