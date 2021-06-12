from display import *
from pages import *

route_now = '/App'

def routeToPage(route):         # 获取当前页面
    page_now = ''
    page = NotFoundPage
    try:
        page_now = route.rsplit('/', 1)[1] # 获取路由中最后页面
    except IndexError:
        print('路由格式错误')
    try:
        page = eval(page_now)
    except NameError:
        print('该页面未定义，%s' % page_now)
    return page


def route_now_Set(route):       # 设置当前路由
    global route_now
    route_now = route

def route_now_Get():            # 获取当前路由
    return route_now

def page_checked_Clear(page):       # 清除页面按钮状态
    for element in page:
        if 'id' in element.keys():
            if 'checked' in element.keys():
                if element['id'] == 0:
                    element['checked'] = True
                else:
                    element['checked'] = False


def change_Handle():
    max_id = 0                                  # 页面中元素最大id
    checked_id = 0                              # 被选中项元素id
    page_now = routeToPage(route_now)
    print('debug info: change_Handle()')
    for element in page_now:
        if 'id' in element.keys():
            if element['id'] > max_id:          # 获取当前页面中所有可选项个数
                max_id = element['id']
            if element['checked'] == True:      # 获取当前页面中被选中项元素id
                checked_id = element['id']
                element['checked'] = False
    
    if checked_id == max_id:                    # 更新下一次被选中项元素
        checked_id = 0
    else:
        checked_id += 1

    for element in page_now:
        if 'id' in element.keys():
            if element['id'] == checked_id:
                element['checked'] = True
    
    display_Update(page_now)


def JumpPage_Handle(element):                                 # 页面跳转
    route_now_Set(element['href'])
    page = routeToPage(route_now)
    page_checked_Clear(page)
    display_Update(page)


def Exit_Handle(element):                                     # 退出页面
    route_now_Set(element['href'])
    page = routeToPage(route_now)
    page_checked_Clear(page)
    display_Update(page)

def SigleDataTest(element):                                   # 单个数据测试
    element['data'] += 1
    element['text'] = str(element['data'])
    display_Update(routeToPage(route_now))

def ListDataTest(element):                                    # 列表数据测试
    if eval(element['text']) in element['data']:
        index = element['data'].index(eval(element['text']))  # 获取当前数据索引
        if index < len(element['data'])-1:                    # 获取列表中下一个数据
            element['text'] = str(element['data'][index + 1])
        else:
            element['text'] = str(element['data'][0])  
    display_Update(routeToPage(route_now))



