import json
import sys
import time
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key

mouse = MouseController()
keyboard = KeyboardController()

if len(sys.argv) < 2:
    print("Please provide a JSON file to replay")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    events = json.load(f)

start_time = events[0]['timestamp']

for event in events:
    delay = event['timestamp'] - start_time
    time.sleep(delay)
    start_time = event['timestamp']

    if event['type'] == 'mouse_move':
        details = event['details']
        x = details['x']
        y = details['y']
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
        try:
            details = event['details']
            keyboard.press(details['key'])
        except:
            pass
    elif event['type'] == 'key_release':
        try:
            details = event['details']
            keyboard.release(details['key'])
        except:
            pass
