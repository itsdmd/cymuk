# Perform action upon pressing key combination defined in the config file

import modules.keyboard_listener as kl
import modules.mouse_jump as mj
import pyautogui as pag


def fn_parser(name):
    if name == 'key_quit':
        key_quit()
    elif name == 'key_centralize':
        key_centralize()
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
    pag.moveRel(-10, 0)


def key_right():
    print("\nright")
    pag.moveRel(10, 0)


def key_up():
    print("\nup")
    pag.moveRel(0, -10)


def key_down():
    print("\ndown")
    pag.moveRel(0, 10)


def key_centralize():
    print("\ncentralize")
    mj.jumpToCenter(kl.current_box[0], kl.current_box[1])


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
    new_box = mj.cut_box_left(kl.current_box[0], kl.current_box[1])
    kl.set_current_box(new_box[0], new_box[1])
    mj.jumpToCenter(kl.current_box[0], kl.current_box[1])


def key_jump_right():
    print("\njump right")
    new_box = mj.cut_box_right(kl.current_box[0], kl.current_box[1])
    kl.set_current_box(new_box[0], new_box[1])
    mj.jumpToCenter(kl.current_box[0], kl.current_box[1])


def key_jump_up():
    print("\njump up")
    new_box = mj.cut_box_up(kl.current_box[0], kl.current_box[1])
    kl.set_current_box(new_box[0], new_box[1])
    mj.jumpToCenter(kl.current_box[0], kl.current_box[1])


def key_jump_down():
    print("\njump down")
    new_box = mj.cut_box_down(kl.current_box[0], kl.current_box[1])
    kl.set_current_box(new_box[0], new_box[1])
    mj.jumpToCenter(kl.current_box[0], kl.current_box[1])


def key_click_left():
    print("\nclick left")
    pag.click(button='left')


def key_click_right():
    print("\nclick right")
    pag.click(button='right')


def key_click_middle():
    print("\nclick middle")
    pag.click(button='middle')


def key_toggle_hold_left():
    print("\ntoggle hold left", end='')

    if kl.mouse_left_holding:
        pag.mouseUp(button='left')
        print(" (up)")
    else:
        pag.mouseDown(button='left')
        print(" (down)")

    kl.set_mouse_left_holding(not kl.mouse_left_holding)


def key_toggle_hold_right():
    print("\ntoggle hold right", end='')

    if kl.mouse_right_holding:
        pag.mouseUp(button='right')
        print(" (up)")
    else:
        pag.mouseDown(button='right')
        print(" (down)")

    kl.set_mouse_right_holding(not kl.mouse_right_holding)


def key_toggle_hold_middle():
    print("\ntoggle hold middle", end='')

    if kl.mouse_middle_holding:
        pag.mouseUp(button='middle')
        print(" (up)")
    else:
        pag.mouseDown(button='middle')
        print(" (down)")

    kl.set_mouse_middle_holding(not kl.mouse_middle_holding)


def key_scroll_up():
    print("\nscroll up")
    pag.scroll(kl.ch.scroll_multiplier)


def key_scroll_down():
    print("\nscroll down")
    pag.scroll(-kl.ch.scroll_multiplier)
