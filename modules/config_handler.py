# Read Config File

import json
import pynput.keyboard as kb
import pyautogui as pag

alphanumerics = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
specials = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11',
            'f12', 'left', 'right', 'up', 'down', 'page_up', 'page_down',
            'home', 'end', 'alt_l', 'alt_r', 'alt_gr', 'ctrl_l', 'ctrl_r',
            'shift_l', 'shift_r', 'tab', 'caps_lock', 'cmd', 'esc', 'space',
            'backspace', 'delete', 'enter', 'print_screen', 'pause', 'insert']

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

screen_default = 0
# Description: The index of the screen that will be used as the default screen.

# -------------------------------- Key mapping ------------------------------- #
key_quit = 'ctrl+q'
# Description: Quit the program.

key_centralize = 'ctrl+r'
# Description: Move the cursor to the center of the screen.

key_next_screen = 'ctrl+right'
# Description: Move the cursor to the center of the next
# 	screen in the screen list.

key_previous_screen = 'ctrl+left'

key_left = 'left'
# Description: Move the cursor left in continuous mode.

key_right = 'right'

key_up = 'up'

key_down = 'down'

key_jump_left = 'shift+left'
# Description: Move the cursor left in jump mode. See
# 	modules/mouse_jump.py for more info.

key_jump_right = 'shift+right'

key_jump_up = 'shift+up'

key_jump_down = 'shift+down'

key_click_left = 'space'
# Description: Emulate left mouse button click.

key_click_right = 'alt+space'

key_click_middle = 'ctrl+space'

key_toggle_hold_left = 'shift+space'
# Description: Emulate left mouse button hold/release.

key_toggle_hold_right = 'alt+shift+space'

key_toggle_hold_middle = 'ctrl+shift+space'

key_scroll_up = 'page_up'
# Description: Emulate scrolling up.

key_scroll_down = 'page_down'

# -------------------------------- Adjustments ------------------------------- #
scroll_multiplier = 5
# Description: The multiplier that will be used when scrolling up or down.

# ---------------------------------------------------------------------------- #


def read_config_file():
    try:
        f = open(config_dir, 'r')
        config_json = json.load(f)
        # print("\nConfig file loaded.")
        f.close()

        global screen_size
        global screen_list
        global screen_default
        global key_quit
        global key_centralize
        global key_next_screen
        global key_previous_screen
        global key_left
        global key_right
        global key_up
        global key_down
        global key_jump_left
        global key_jump_right
        global key_jump_up
        global key_jump_down
        global key_click_left
        global key_click_right
        global key_click_middle
        global key_toggle_hold_left
        global key_toggle_hold_right
        global key_toggle_hold_middle
        global key_scroll_up
        global key_scroll_down
        global scroll_multiplier

        try:
            screen_size = config_json['screen_size']
            screen_list = config_json['screen_list']
            screen_default = config_json['screen_default']
            key_quit = config_json['key_quit']
            key_centralize = config_json['key_centralize']
            key_next_screen = config_json['key_next_screen']
            key_previous_screen = config_json['key_previous_screen']
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
            key_toggle_hold_left = config_json['key_toggle_hold_left']
            key_toggle_hold_right = config_json['key_toggle_hold_right']
            key_toggle_hold_middle = config_json['key_toggle_hold_middle']
            key_scroll_up = config_json['key_scroll_up']
            key_scroll_down = config_json['key_scroll_down']
            scroll_multiplier = config_json['scroll_multiplier']

        except KeyError:
            print("\nConfig file is corrupted. Do you want to create a new one?")
            choice = input('y/n: ')
            if choice == 'y':
                write_config_file()
            else:
                print("\nExiting...")
                exit()

        return config_json

    except FileNotFoundError:
        print("\nConfig file not found. Do you want to create a new one?")
        choice = input('y/n: ')
        if choice == 'y':
            write_config_file()
        else:
            print("\nExiting...")
            exit()

        return {}


def write_config_file():
    f = open(config_dir, 'w')

    json.dump({
        "screen_size": screen_size,
        "screen_list": screen_list,
        "screen_default": screen_default,
        "key_quit": key_quit,
        "key_centralize": key_centralize,
        "key_next_screen": key_next_screen,
        "key_previous_screen": key_previous_screen,
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
        "key_toggle_hold_left": key_toggle_hold_left,
        "key_toggle_hold_right": key_toggle_hold_right,
        "key_toggle_hold_middle": key_toggle_hold_middle,
        "key_scroll_up": key_scroll_up,
        "key_scroll_down": key_scroll_down,
        "scroll_multiplier": scroll_multiplier,
    }, f, indent=4)

    f.close()

    print("\nConfig file created.")


def str_to_key(input: str):
    if input in alphanumerics:
        return kb.KeyCode.from_char(input)
    else:
        return kb.Key[input]
