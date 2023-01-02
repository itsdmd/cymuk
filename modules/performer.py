# Perform Action Upon Pressing Key Sequence Defined In the Config File

import modules.keyboard_listener as kl
import modules.mouse_jump as mj
from pyautogui import click, moveRel, mouseDown, mouseUp, scroll


def fn_parser(name):
    if name == 'key_quit':
        key_quit()
    elif name == 'key_centralize':
        key_centralize()
    elif name == 'key_centralize_root':
        key_centralize_root()
    elif name == 'key_next_screen':
        key_next_screen()
    elif name == 'key_previous_screen':
        key_previous_screen()
    elif name == 'key_left':
        key_left()
    elif name == 'key_right':
        key_right()
    elif name == 'key_up':
        key_up()
    elif name == 'key_down':
        key_down()
    elif name == 'key_jump_left':
        key_jump_left()
    elif name == 'key_jump_right':
        key_jump_right()
    elif name == 'key_jump_up':
        key_jump_up()
    elif name == 'key_jump_down':
        key_jump_down()
    elif name == 'key_click_left':
        key_click_left()
    elif name == 'key_click_right':
        key_click_right()
    elif name == 'key_click_middle':
        key_click_middle()
    elif name == 'key_toggle_hold_left':
        key_toggle_hold_left()
    elif name == 'key_toggle_hold_right':
        key_toggle_hold_right()
    elif name == 'key_toggle_hold_middle':
        key_toggle_hold_middle()
    elif name == 'key_scroll_up':
        key_scroll_up()
    elif name == 'key_scroll_down':
        key_scroll_down()
    else:
        return


def execute_key_combination():
    # print(kl.current_key_combination)
    current_key_combination_str = ""
    for key in kl.current_key_combination:
        current_key_combination_str += str(key).replace("Key.", "").lower()
        if not key == kl.current_key_combination[-1]:
            current_key_combination_str += "+"

    for keymap in kl.config_items:
        if current_key_combination_str == keymap[1]:
            fn_parser(keymap[0])
            return


def key_quit():
    print("\nquit")
    kl.listener.stop()
    exit()


def key_left():
    print("\nleft")
    moveRel(-kl.config_json["step_multiplier"], 0)


def key_right():
    print("\nright")
    moveRel(kl.config_json["step_multiplier"], 0)


def key_up():
    print("\nup")
    moveRel(0, -kl.config_json["step_multiplier"])


def key_down():
    print("\ndown")
    moveRel(0, kl.config_json["step_multiplier"])


def key_centralize():
    print("\ncentralize")
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def key_centralize_root():
    print("\ncentralize root")
    kl.set_current_boundary(kl.screens[kl.current_screen_index][0],
                            kl.screens[kl.current_screen_index][1])
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def key_next_screen():
    print("\nnext screen")
    new_index = kl.current_screen_index + 1
    if new_index >= len(kl.screens):
        new_index = 0
    kl.set_current_screen_index(new_index)
    mj.jumpToCenter(kl.screens[new_index][0], kl.screens[new_index][1])


def key_previous_screen():
    print("\nprevious screen")
    new_index = kl.current_screen_index - 1
    if new_index < 0:
        new_index = len(kl.screens) - 1
    kl.set_current_screen_index(new_index)
    mj.jumpToCenter(kl.screens[new_index][0], kl.screens[new_index][1])


def key_jump_left():
    print("\njump left")
    new_boundary = mj.cut_boundary_left(kl.current_boundary[0],
                                        kl.current_boundary[1])
    kl.set_current_boundary(new_boundary[0], new_boundary[1])
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def key_jump_right():
    print("\njump right")
    new_boundary = mj.cut_boundary_right(kl.current_boundary[0],
                                         kl.current_boundary[1])
    kl.set_current_boundary(new_boundary[0], new_boundary[1])
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def key_jump_up():
    print("\njump up")
    new_boundary = mj.cut_boundary_up(kl.current_boundary[0],
                                      kl.current_boundary[1])
    kl.set_current_boundary(new_boundary[0], new_boundary[1])
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def key_jump_down():
    print("\njump down")
    new_boundary = mj.cut_boundary_down(kl.current_boundary[0],
                                        kl.current_boundary[1])
    kl.set_current_boundary(new_boundary[0], new_boundary[1])
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def key_click_left():
    print("\nclick left")
    click(button='left')


def key_click_right():
    print("\nclick right")
    click(button='right')


def key_click_middle():
    print("\nclick middle")
    click(button='middle')


def key_toggle_hold_left():
    if kl.mouse_left_holding:
        mouseUp(button='left')
        print("\ntoggle hold left (up)")
    else:
        mouseDown(button='left')
        print("\ntoggle hold left (down)")

    kl.set_mouse_left_holding(not kl.mouse_left_holding)


def key_toggle_hold_right():
    if kl.mouse_right_holding:
        mouseUp(button='right')
        print("\ntoggle hold right (up)")
    else:
        mouseDown(button='right')
        print("\ntoggle hold right (down)")

    kl.set_mouse_right_holding(not kl.mouse_right_holding)


def key_toggle_hold_middle():
    if kl.mouse_middle_holding:
        mouseUp(button='middle')
        print("\ntoggle hold middle (up)")
    else:
        mouseDown(button='middle')
        print("\ntoggle hold middle (down)")

    kl.set_mouse_middle_holding(not kl.mouse_middle_holding)


def key_scroll_up():
    print("\nscroll up")
    scroll(kl.config_json["scroll_multiplier"])


def key_scroll_down():
    print("\nscroll down")
    scroll(-kl.config_json["scroll_multiplier"])
