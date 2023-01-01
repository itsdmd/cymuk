# Listen To Keyboard Events

from pynput import keyboard

continuous = False


# Capture key press
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        if continuous:
            return key.char
    except AttributeError:
        print('special key {0} pressed'.format(key))
        if continuous:
            return key


# Capture key release
def on_release(key):
    print('{0} released'.format(key))
    if not continuous:
        return key


# Collect events until released
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
