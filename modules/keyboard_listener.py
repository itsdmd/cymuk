# Listen To Keyboard Events and Execute Key Combinations Using performer.py

import modules.config_handler as ch
import modules.performer as pf
import pynput.keyboard as kb

config_json = ch.read_config_file()
config_items = config_json.items()
current_screen_index = config_json["screen_default"]
current_box = config_json["screen_list"][current_screen_index]
screens = config_json["screen_list"]

current_key_combination = []
mouse_left_holding = False
mouse_middle_holding = False
mouse_right_holding = False
screens = []
sticky_keys = [kb.Key.ctrl, kb.Key.alt, kb.Key.shift]

print("new keyboard_listener.py")


def set_current_box(topLeft, bottomRight):
    global current_box
    current_box = ((topLeft[0], topLeft[1]), (bottomRight[0], bottomRight[1]))
    print("New box: ", current_box)


def set_current_screen_index(index):
    global current_screen_index
    current_screen_index = index


def set_mouse_left_holding(value):
    global mouse_left_holding
    mouse_left_holding = value


def set_mouse_middle_holding(value):
    global mouse_middle_holding
    mouse_middle_holding = value


def set_mouse_right_holding(value):
    global mouse_right_holding
    mouse_right_holding = value


def on_press(key):
    global current_key_combination

    # Alphanumeric keys
    try:
        if key.char not in current_key_combination:
            current_key_combination.append(key.char)
            pf.execute_key_combination()

    # Special keys and Other characters
    except AttributeError:
        if key in sticky_keys:
            current_key_combination.append(key)
        else:
            try:
                # Prevent duplicate alphanumeric keys being double registered
                # 	in key combination
                if key.char not in current_key_combination:
                    current_key_combination.append(key.char)
                    pf.execute_key_combination()
            except:
                if key not in current_key_combination:
                    current_key_combination.append(key)
                    pf.execute_key_combination()

    except:
        return


# Capture key release
def on_release(key):
    global current_key_combination

    try:
        current_key_combination.remove(key.char)
    except:
        try:
            current_key_combination.remove(key)
        except:
            return


# Collect single key events until released, suppress events from other
# 	processes
listener = kb.Listener(
    on_press=on_press,
    on_release=on_release,
    suppress=True)
