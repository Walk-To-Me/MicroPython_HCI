from display import *
from pages import *

route_now = '/App/LiquidLevelPage'

def routeToPage(route):         # 获取当前页面
    page_now = None
    try:
        page_now = route.rsplit('/', 1)[1] # 获取路由中最后页面
    except IndexError:
        print('路由格式错误')
    return eval(page_now)




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


def JumpPage_Handle():
    pass

def Exit_Handle():
    pass




