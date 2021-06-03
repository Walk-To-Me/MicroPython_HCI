from ssd1306 import SSD1306_I2C
from pyb import Pin
from machine import I2C

i2c = I2C(1)
oled = SSD1306_I2C(128, 64, i2c)
