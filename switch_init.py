from pyb import Pin
from events import *
import pyb, time


sw1 = Pin(Pin.cpu.F6, Pin.IN, Pin.PULL_UP)
sw2 = Pin(Pin.cpu.F7, Pin.IN, Pin.PULL_UP)
sw1_event = change_Handle
sw2_event = Exit_Handle




def sw1Event_Set(value):        # 设置sw1当前事件
    global sw1_event
    sw1_event = value

def sw1Event_Get():             # 获取sw1当前事件
    return sw1_event

def sw2Event_Set(value):        # 设置sw2当前事件
    global sw2_event
    sw2_event = value

def sw2Event_Get():             # 获取sw2当前事件
    return sw2_event



def sw1_Handle(t):               # 按键1中断处理
    pyb.disable_irq()           # 关闭中断
    time.sleep_ms(20)           # 延时去抖
    pyb.enable_irq()            # 打开中断
    if (not sw1.value()):
        print('debug info: button1 down')
        change_Handle()
        
        route_now = route_now_Get()
        for element in routeToPage(route_now):
            if element['checked'] == True:
                sw2Event_Set(eval(element['handle']))
                print(element['handle'])
        sw_Update()

def sw2_Handle(t):               # 按键2中断处理
    pyb.disable_irq()            # 关闭中断
    time.sleep_ms(20)            # 延时去抖
    pyb.enable_irq()             # 打开中断
    if (not sw2.value()):
        route_now = route_now_Get()
        for element in routeToPage(route_now):
            if 'id' in element.keys():
                if 'checked' in element.keys():
                    if element['checked'] == True:
                        sw2Event_Get()(element)
                        break
    


sw1.irq(trigger=Pin.IRQ_FALLING, handler=sw1_Handle)
sw2.irq(trigger=Pin.IRQ_FALLING, handler=sw2_Handle)
 

def sw_Update():
    #sw1.irq(handler=sw1_Handle)
    sw2.irq(trigger=Pin.IRQ_FALLING, handler=sw2_Handle)


