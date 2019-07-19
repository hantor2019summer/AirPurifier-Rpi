import time
import Adafruit_CharLCD as LCD
from aqi import get_values
# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

print(get_values())

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.message('ABCDEFGHIJKLMNP\nabcdefghijklmnop!')
time.sleep(5.0)

lcd.clear()

'''
text = raw_input("Type Something to be displayed: ")

lcd.message(text)
time.sleep(5.0)

lcd.clear()

lcd.message('Goodbye\nWorld!')
time.sleep(5.0)

lcd.clear()
'''
