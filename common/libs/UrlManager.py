import time

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def builduUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = "%s"%(int(time.time()))
        path = "/static" + path + "?bersion=" + ver
        return UrlManager.builduUrl(path)

    @staticmethod
    def buildImageUrl(path):
        pass