from pyb import Pin
from events import *
import pyb, time


sw1 = Pin(Pin.cpu.F6, Pin.IN, Pin.PULL_UP)
sw2 = Pin(Pin.cpu.F7, Pin.IN, Pin.PULL_UP)
sw1_event = change_Handle
sw2_event = None




def sw1Event_Set(value):        # 设置sw1当前事件
    sw1_event = value

def sw1Event_Get():             # 获取sw1当前事件
    return sw1_event

def sw2Event_Set(value):        # 设置sw2当前事件
    sw2_event = value

def sw2Event_Get():             # 获取sw2当前事件
    return sw2_event



def sw1_Handle(t):               # 按键1中断处理
    pyb.disable_irq()           # 关闭中断
    print('debug info: button1 down')
    change_Handle()
    time.sleep_ms(50)           # 延时去抖
    pyb.enable_irq()            # 打开中断

def sw2_Handle(t):               # 按键2中断处理
    pyb.disable_irq()           # 关闭中断
    sw2Event_Get()()
    time.sleep_ms(50)           # 延时去抖
    pyb.enable_irq()            # 打开中断


sw1.irq(trigger=Pin.IRQ_FALLING, handler=sw1_Handle)
sw2.irq(trigger=Pin.IRQ_FALLING, handler=sw2_Handle)
 

def sw_Update():
    sw1.irq(sw1_Handle)
    sw2.irq(sw2_Handle)

