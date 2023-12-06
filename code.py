# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import digitalio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import rotaryio



# Buttons setup
button_a = digitalio.DigitalInOut(board.GP8)
button_a.switch_to_input(pull=digitalio.Pull.UP)

button_b = digitalio.DigitalInOut(board.GP9)
button_b.switch_to_input(pull=digitalio.Pull.UP)

button_c = digitalio.DigitalInOut(board.GP26)
button_c.switch_to_input(pull=digitalio.Pull.UP)

button_d = digitalio.DigitalInOut(board.GP27)
button_d.switch_to_input(pull=digitalio.Pull.UP)

button_e = digitalio.DigitalInOut(board.GP12)
button_e.switch_to_input(pull=digitalio.Pull.UP)

# Rotary encoder setup
encoder = rotaryio.IncrementalEncoder(board.GP15, board.GP14)

# LED's

#led = Pin(28,Pin.OUT)
#led2 = Pin(27,Pin.OUT)
#led3 = Pin(26,Pin.OUT)
led = digitalio.DigitalInOut(board.GP21)
led.direction = digitalio.Direction.OUTPUT

led_a = digitalio.DigitalInOut(board.GP20)
led_a.direction = digitalio.Direction.OUTPUT

led_b = digitalio.DigitalInOut(board.GP19)
led_b.direction = digitalio.Direction.OUTPUT

led_c = digitalio.DigitalInOut(board.GP18)
led_c.direction = digitalio.Direction.OUTPUT

led_d = digitalio.DigitalInOut(board.LED)
led_d.direction = digitalio.Direction.OUTPUT

led.value = True
led_a.value = True
led_b.value = True
led_c.value = True
led_d.value = True

cc = ConsumerControl(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)

button_state = None
last_position = encoder.position

while True:
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            keyboard.press(Keycode.UP_ARROW)
            keyboard.release_all()
            led.value = False
            led_a.value = False
            led_b.value = False
            led_c.value = False
            led_d.value = False
            time.sleep(0.1)
            led.value = True
            time.sleep(0.1)
            led_a.value = True
            time.sleep(0.1)
            led_b.value =True
            time.sleep(0.1)
            led_c.value =True
            time.sleep(0.1)
            led_d.value = True
              
        print("Volume Increased:", current_position)
    elif position_change < 0:
        for _ in range(-position_change):
            keyboard.press(Keycode.DOWN_ARROW)
            keyboard.release_all()
            led.value = False
            led_a.value = False
            led_b.value = False
            led_c.value = False
            #led_d.value = False
            time.sleep(0.1)
            led_c.value = True
            time.sleep(0.1)
            led_b.value = True
            time.sleep(0.1)
            led_a.value =True
            time.sleep(0.1)
            led.value =True
            time.sleep(0.1)
            #led_d.value = True
            
            
        print("Volume Decreased:", current_position)
    last_position = current_position
 
    if not button_a.value:
        
        keyboard.press(Keycode.LEFT_ARROW)
        keyboard.release_all()
        led_a.value = False
        time.sleep(0.4)
        led_a.value = True
        #time.sleep(0.6)  # Adjusted delay to debounce the button
        

    if not button_b.value:
        keyboard.press(Keycode.RIGHT_ARROW)
        keyboard.release_all()
        led_b.value = False
        time.sleep(0.4)  # Adjusted delay to debounce the button
        led_b.value = True

    if not button_c.value:
        keyboard.press(Keycode.ENTER)
        keyboard.release_all()
        led.value = False
        time.sleep(0.4)  # Adjusted delay to debounce the button
        led.value = True
        
    if not button_d.value:
        keyboard.press(Keycode.BACKSPACE)
        keyboard.release_all()
        #time.sleep(0.4)  # Adjusted delay to debounce the button
        led_c.value = False
        time.sleep(0.4)
        led_c.value = True

    if not button_e.value:
        keyboard.press(Keycode.SPACEBAR)
        keyboard.release_all()
        led.value = False
        led_a.value = False
        led_b.value = False
        led_c.value = False
        #led_d.value = False
        time.sleep(0.3)
        led.value = True
        led_a.value = True
        led_b.value =True
        led_c.value =True
        #led_d.value = True
        time.sleep(0.1)
              
           #time.sleep (2)
  
#if not b  utto n_f
       
 # cc.send(Consumeg button_f is your
