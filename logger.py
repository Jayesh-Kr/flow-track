import ctypes
PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)

from pynput import mouse, keyboard
import json
import time
from datetime import datetime

# events = []

def log_event(event_type, details):
    event = {
        'timestamp': time.time(),
        'type': event_type,
        'details': details
    }
    print(json.dumps(event))  # Output as JSON string
    # events.append(event)

# Mouse events
def on_move(x, y):
    log_event('mouse_move', {'x': x, 'y': y})

def on_click(x, y, button, pressed):
    log_event('mouse_click', {
        'x': x,
        'y': y,
        'button': str(button),
        'pressed': pressed
    })

def on_scroll(x, y, dx, dy):
    log_event('mouse_scroll', {
        'x': x,
        'y': y,
        'dx': dx,
        'dy': dy
    })

# Keyboard events
def on_press(key):
    try:
        key_val = key.char
    except AttributeError:
        key_val = str(key)
    log_event('key_press', {'key': key_val})

def on_release(key):
    key_val = str(key)
    log_event('key_release', {'key': key_val})
    if key == keyboard.Key.esc:
        return False

# Start listeners non-blocking
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

mouse_listener.start()
keyboard_listener.start()

keyboard_listener.join()
mouse_listener.stop()

# Save to file on exit
# filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
# with open(filename, 'w') as f:
#     json.dump(events, f, indent=2)
