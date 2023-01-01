# Read Config File

import pyautogui as pag
from pynput import keyboard as kb
import configparser
import json

alphanumerics = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

config_dir = 'config.json'

# ---------------------------------------------------------------------------- #
#                               List of all keys                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Screen ---------------------------------- #
screen_size = pag.size()
# Format: (x, y)
# Description: The total dimension of all screens, depends on how you set up
# 	your screens in the settings.

screen_list = [((0, 0), screen_size)]
# Format: [((top_left_x, top_left_y), (bottom_right_x, bottom_right_y)), ...]
# Description: An ordered list of all screens' top left and bottom right
# 	coordination relative to the bounding box of all the screens.

# -------------------------------- Key mapping ------------------------------- #
# List of all key codes:
#   a-z, 0-9, -, =, [, ], ', ,, ., ;, /, \, f1-f12, left, right, up, down,
#   page_up, page_down, home, end, alt_l, alt_r, alt_gr, ctrl_l, ctrl_r,
#   shift_l, shift_r, tab, caps_lock, cmd, esc, backspace, delete, enter, space,
#   print_screen, scroll_lock, pause, insert

key_activate = 'ctrl+;'
# Format: 'key_code1(+key_code2+...)'
# Description: The key that will activate the program.

key_quit = 'esc'
# Description: The key that will quit the program.

key_left = 'left'
# Description: The key that will move the cursor left in continuous mode.

key_right = 'right'

key_up = 'up'

key_down = 'down'

key_jump_left = 'shift+left'
# Description: The key that will move the cursor left in jump mode. See
# 	modules/mouse_jump.py for more info.

key_jump_right = 'shift+right'

key_jump_up = 'shift+up'

key_jump_down = 'shift+down'

key_click_left = 'space'
# Description: The key that will emulate left mouse button click.

key_click_right = 'alt+space'

key_click_middle = 'ctrl+space'

key_scroll_up = 'page_up'
# Description: The key that will emulate scrolling up.

key_scroll_down = 'page_down'

key_scroll_up_fast = 'shift+page_up'
# Description: The key that will emulate scrolling up with multiplier.

key_scroll_down_fast = 'shift+page_down'

key_scroll_multiplier = 5
# Description: The multiplier that will be used when scrolling up or down.

key_scroll_multiplier_fast = 15
# Description: The multiplier that will be used when scrolling up or down in
# 	fast mode.

# ---------------------------------------------------------------------------- #


def read_config_file():
    try:
        f = open(config_dir, 'r')
        config_json = json.load(f)
        print("Config file loaded.")
        f.close()

        try:
            screen_size = config_json['screen_size']
            screen_list = config_json['screen_list']
            key_activate = config_json['key_activate']
            key_quit = config_json['key_quit']
            key_left = config_json['key_left']
            key_right = config_json['key_right']
            key_up = config_json['key_up']
            key_down = config_json['key_down']
            key_jump_left = config_json['key_jump_left']
            key_jump_right = config_json['key_jump_right']
            key_jump_up = config_json['key_jump_up']
            key_jump_down = config_json['key_jump_down']
            key_click_left = config_json['key_click_left']
            key_click_right = config_json['key_click_right']
            key_click_middle = config_json['key_click_middle']
            key_scroll_up = config_json['key_scroll_up']
            key_scroll_down = config_json['key_scroll_down']
            key_scroll_up_fast = config_json['key_scroll_up_fast']
            key_scroll_down_fast = config_json['key_scroll_down_fast']
            key_scroll_multiplier = config_json['key_scroll_multiplier']
            key_scroll_multiplier_fast = config_json['key_scroll_multiplier_fast']

        except KeyError:
            print("Config file is corrupted. Do you want to create a new one?")
            choice = input('y/n: ')
            if choice == 'y':
                write_config_file()
            else:
                print("Exiting...")
                exit()

    except FileNotFoundError:
        print("Config file not found. Do you want to create a new one?")
        choice = input('y/n: ')
        if choice == 'y':
            write_config_file()
        else:
            print("Exiting...")
            exit()


def write_config_file():
    f = open(config_dir, 'w')

    json.dump({
        "screen_size": screen_size,
        "screen_list": screen_list,
        "key_activate": key_activate,
        "key_quit": key_quit,
        "key_left": key_left,
        "key_right": key_right,
        "key_up": key_up,
        "key_down": key_down,
        "key_jump_left": key_jump_left,
        "key_jump_right": key_jump_right,
        "key_jump_up": key_jump_up,
        "key_jump_down": key_jump_down,
        "key_click_left": key_click_left,
        "key_click_right": key_click_right,
        "key_click_middle": key_click_middle,
        "key_scroll_up": key_scroll_up,
        "key_scroll_down": key_scroll_down,
        "key_scroll_up_fast": key_scroll_up_fast,
        "key_scroll_down_fast": key_scroll_down_fast,
        "key_scroll_multiplier": key_scroll_multiplier,
        "key_scroll_multiplier_fast": key_scroll_multiplier_fast,
    }, f, indent=4)

    f.close()

    print("Config file created.")


def str_to_key(input: str):
    if input in alphanumerics:
        return kb.KeyCode.from_char(input)
    else:
        return kb.Key[input]
