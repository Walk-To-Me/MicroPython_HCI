# 2021年6月3日 00点00分
# 人机交互V1.0
# 创建工程
# Walk-To-Me

from oled_init import *
#from switch_init import *



def route_now_Set(route):       # 设置当前路由
    route_now = route

def route_now_Get():            # 获取当前路由
    return route_now


def display_Update(page):
    oled.fill(0)                # 清屏

    
    for element in page:        # 遍历页面元素
        fmt = element['format']
        if fmt == 0:
            pass
        elif fmt == 1:          # 图片元素处理
            if 'checked' in element.keys():
                if element['checked'] == True:
                    oled.blit(element['data'], element['position'][0]*8, element['position'][1]*8)
        elif fmt == 2:          # 文本元素处理
            is_invert = False                          # 反向显示标志
            if 'checked' in element.keys():
                if element['checked'] == True:         # 选中项反向显示
                    is_invert = True
            oled.draw_chinese_fast(element['text'], element['position'][0], element['position'][1], invert=is_invert, font_size=16)
                    

    #sw_Update()
    oled.show()                 # 更新显示


    
