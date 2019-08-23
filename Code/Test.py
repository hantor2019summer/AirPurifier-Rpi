import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import requests, json
import time

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

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# Raspberry Relay Control
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)

# Request Server
URL = 'http://bigpie1367.pythonanywhere.com/api/dusts/'

while True : 
    lcd.clear()

    #Get Value
    cur_density = get_values()
    total_message = "UDust : "+str(cur_density[0])+"\nFDust : "+str(cur_density[1])

    # Control Relay
    if cur_density[0] >= 12 or cur_density[1] >= 15 :
        GPIO.output(20, True)
        print("Current Status : ON")
    else : 
        GPIO.output(20, False)
        print("Current Status : OFF")

    #Post Data to Server
    data = {'density' : cur_density[0]}
    res = requests.post(URL, data = json.dumps(data))

    #Print LCD 
    print(total_message)
    lcd.message(total_message)

    time.sleep(5.0) 
