'''
-------------------------------整体结构-------------------------------
                                 App
                                  |
                        ---------------------
                        |    |    |    |    |
应用层                 app1 app2 ...  appN appN+1
                        |
                    ----------------     ...
                    |       |      |
页面层             page1   page2   ...
                    |
                ------------------       ...
                |        |       |
元素层         elem0    elem1    ...
---------------------------------------------------------------------

'''
import framebuf

app_image = {}

with open('液位仪.pbm', 'r') as f:
    f.readline()
    width, height = [int(v) for v in f.readline().split()]
    data = bytearray(f.read())
app_image['LiquidLevel'] = framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)

with open('温湿度.pbm', 'r') as f:
    f.readline()
    width, height = [int(v) for v in f.readline().split()]
    data = bytearray(f.read())
app_image['Temperature'] = framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)

with open('时钟.pbm', 'r') as f:
    f.readline()
    width, height = [int(v) for v in f.readline().split()]
    data = bytearray(f.read())
app_image['Clock'] = framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)

with open('wifi.pbm', 'r') as f:
    f.readline()
    width, height = [int(v) for v in f.readline().split()]
    data = bytearray(f.read())
app_image['WiFi'] = framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)


App = [
    {'format': 1, 'href': '/App/LiquidLevelPage', 'data': app_image['LiquidLevel'],
     'position': (4, 0), 'id': 0, 'handle': 'JumpPage_Handle', 'checked': True},
    {'format': 1, 'href': '/App/TemperaturePage', 'data': app_image['Temperature'],
     'position': (4, 0), 'id': 1, 'handle': 'JumpPage_Handle', 'checked': False},
    {'format': 1, 'href': '/App/ClockPage', 'data': app_image['Clock'],
     'position': (4, 0), 'id': 2, 'handle':'JumpPage_Handle', 'checked': False},
    {'format': 1, 'href': '/App/WiFiPage', 'data': app_image['WiFi'],
     'position': (4, 0), 'id': 3, 'handle':'JumpPage_Handle', 'checked': False},
]

LiquidLevelPage = [
    {'format': 2, 'href': '/App/LiquidLevelPage/LiquidLevel_View', 'text': '显示液位',
     'position': (0, 0), 'id': 0, 'handle': 'JumpPage_Handle', 'checked': True},
    {'format': 2, 'href': '/App/LiquidLevelPage/LiquidLevel_Set', 'text': '设置液位',
     'position': (0, 1), 'id': 1, 'handle': 'JumpPage_Handle', 'checked': False},
    {'format': 2, 'href': '/App', 'text': '退出',
     'position': (0, 2), 'id': 2, 'handle': 'Exit_Handle', 'checked': False},
]

TemperaturePage = [
    {'format': 2, 'href': '/App/TemperaturePage/Temperature_View', 'text': '显示温度',
     'position': (0, 0), 'id': 0, 'handle': 'JumpPage_Handle', 'checked': True},
    {'format': 2, 'href': '/App/TemperaturePage/Temperature_Set', 'text': '设置温度',
     'position': (0, 1), 'id': 1, 'handle': 'JumpPage_Handle', 'checked': False},
    {'format': 2, 'href': '/App/TemperaturePage/Temperature_Save', 'text': '保存数据',
     'position': (0, 2), 'id': 2, 'handle': 'JumpPage_Handle', 'checked': False},
    {'format': 2, 'href': '/App', 'text': '退出',
     'position': (0, 3), 'id': 3, 'handle': 'Exit_Handle', 'checked': False},
]

ClockPage = [
    {'format': 2, 'href': '/App/ClockPage/ClockPage_View', 'text': '显示时间',
     'position': (0, 0), 'id': 0, 'handle': 'JumpPage_Handle', 'checked': True},
    {'format': 2, 'href': '/App/ClockPage/ClockPage_Set', 'text': '设置时间',
     'position': (0, 1), 'id': 1, 'handle': 'JumpPage_Handle', 'checked': False},
    {'format': 2, 'href': '/App', 'text': '退出',
     'position': (0, 2), 'id': 2, 'handle': 'Exit_Handle', 'checked': False},
]

WiFiPage = [
    {'format': 2, 'href': '/App/WiFiPage/WiFiPage_Connect', 'text': '连接WiFi',
     'position': (0, 0), 'id': 0, 'handle': 'JumpPage_Handle', 'checked': True},
    {'format': 2, 'href': '/App', 'text': '退出',
     'position': (0, 1), 'id': 1, 'handle': 'Exit_Handle', 'checked': False},
]

LiquidLevel_View = [
    {'format': 3, 'text': '45', 'data': 45, 'position': (0, 0), 'id': 0,
     'handle': 'SigleDataTest', 'checked': True},
    {'format': 3, 'text': '10', 'data': [10, 20, 30, 40, 50], 'position': (0, 1),
     'id': 1, 'handle': 'ListDataTest', 'checked': False},
    {'format': 2, 'href': '/App/LiquidLevelPage', 'text': '退出',
     'position': (0, 2), 'id': 2, 'handle': 'Exit_Handle', 'checked': False},
]




