from flask import render_template,g
import datetime

# 自定义渲染方法
def ops_render(template,context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template,**context) 


# 获取当前时间
def getCurrentDate():
    return datetime.datetime.now()


# 自定义分页操作
def iPagenation(params):
    import math
    ret = {
        "is_prev":True,
        "is_next":True,
        "from":0,
        "end":0,
        "current":0,
        "tatal_pages":0,
        "page_size":0,
        "total":0,
        "url":params['url']
    }

    total = int(params['total'])
    page_size = int(params['page_size'])
    page = int(params['page'])
    total_pages = int(math.ceil(total/page_size))

    if page <= 1:
        ret['is_prev'] = False
    if page >= total_pages:
        ret['is_next'] = False

    ret['from'] = 1
    ret['end'] = total_pages
    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['total'] = total
    ret['page_size'] = page_size
    # 分页的核心是：生成器,生成页码
    ret['range'] = range(ret['from'],ret['end']+1)

    return ret 

