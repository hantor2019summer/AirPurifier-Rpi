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
URL = 'http://bigpie1367.pythonanywhere.com/api/'

while True :
    lcd.clear()

    #Get Value
    cur_density = get_values()
    total_message = "PM-2.5 : "+str(cur_density[0])+"\nPM-10 : "+str(cur_density[1])    

    #LCD Print
    print(total_message)
    lcd.message(total_message)

    state_res = requests.get(URL+'switch/')
    state_res = json.loads(state_res.content.decode())[0]['state']
    
    #Control Relay
    if state_res == True and (cur_density[0] >= 5 or cur_density[1] >= 10) :
        GPIO.output(20, True)
        print("Current Status : ON")
    else : 
        GPIO.output(20, False)
        print("Current Status : OFF")
    
    #Post Data to Server
    density_data = {'ultra_fine_density' : cur_density[0], 'fine_density' : cur_density[1]}
    requests.post(URL+'dusts/', data = density_data)

    time.sleep(10.0) 
