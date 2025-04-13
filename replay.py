import json
import sys
import time
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key

import ctypes
user32 = ctypes.windll.user32
current_width, current_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

mouse = MouseController()
keyboard = KeyboardController()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

KEY_MAPPING = {
    'Key.enter': Key.enter,
    'Key.space': Key.space,
    'Key.shift': Key.shift,
    'Key.ctrl': Key.ctrl,
    'Key.alt': Key.alt,
    'Key.cmd': Key.cmd,
    'Key.esc': Key.esc,
    'Key.tab': Key.tab,
    'Key.backspace': Key.backspace,
    'Key.delete': Key.delete,
    'Key.up': Key.up,
    'Key.down': Key.down,
    'Key.left': Key.left,
    'Key.right': Key.right,
    'Key.home': Key.home,
    'Key.end': Key.end,
    'Key.page_up': Key.page_up,
    'Key.page_down': Key.page_down,
    'Key.insert': Key.insert,
    'Key.menu': Key.menu,
    'Key.f1': Key.f1,
    'Key.f2': Key.f2,
    'Key.f3': Key.f3,
    'Key.f4': Key.f4,
    'Key.f5': Key.f5,
    'Key.f6': Key.f6,
    'Key.f7': Key.f7,
    'Key.f8': Key.f8,
    'Key.f9': Key.f9,
    'Key.f10': Key.f10,
    'Key.f11': Key.f11,
    'Key.f12': Key.f12,
}

if len(sys.argv) < 2:
    print("Please provide a JSON file to replay")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    events = json.load(f)

start_time = events[0]['timestamp']

for event in events:
    delay = event['timestamp'] - start_time
    if delay > 0 :
        time.sleep(delay)
    start_time = event['timestamp']

    if event['type'] == 'mouse_move':
        details = event['details']
        x_scale = current_width / SCREEN_WIDTH
        y_scale = current_height / SCREEN_HEIGHT
        x = details['x'] * x_scale
        y = details['y'] * y_scale
        mouse.position = (x, y)

    elif event['type'] == 'mouse_click':
        details = event['details']
        x = details['x']
        y = details['y']
        mouse.position = (x, y)
        btn = Button.left if details['button'] == 'Button.left' else Button.right
        if details['pressed']:
            mouse.press(btn)
        else:
            mouse.release(btn)

    elif event['type'] == 'scroll':
        mouse.scroll(event['dx'], event['dy'])

    elif event['type'] == 'key_press':
        details = event['details']
        key = details['key']
        
        # Handle special keys
        if key in KEY_MAPPING:
            keyboard.press(KEY_MAPPING[key])
        # Handle regular keys (remove quotes if present)
        elif key.startswith("'") and key.endswith("'"):
            keyboard.press(key[1:-1])
        else:
            keyboard.press(key)

    elif event['type'] == 'key_release':
        details = event['details']
        key = details['key']
        
        # Handle special keys
        if key in KEY_MAPPING:
            keyboard.release(KEY_MAPPING[key])
        # Handle regular keys (remove quotes if present)
        elif key.startswith("'") and key.endswith("'"):
            keyboard.release(key[1:-1])
        else:
            keyboard.release(key)
