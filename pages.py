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





