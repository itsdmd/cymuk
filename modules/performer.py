# Perform Action Upon Pressing Key Sequence Defined In the Config File

from modules.global_properties import get_verbose
from pyautogui import click, dragTo, dragRel, moveTo, moveRel, mouseDown, mouseUp, vscroll, hscroll
from time import sleep
import modules.keyboard_listener as kl
import modules.mouse_jump as mj


def fn_parser(name, args=[]):
    if 'quit' in name:
        try:
            quit(int(args[0]))
        except IndexError:
            quit()
    elif 'centralize_root' in name:
        centralize_root()
    elif 'centralize' in name:
        centralize()
    elif 'screen_index' in name:
        try:
            screen_index(int(args[0]))
        except IndexError:
            print("ERROR: {} missing arguments".format(name))
            quit(1)
    elif 'screen_next' in name:
        try:
            screen_next(args[0])
        except IndexError:
            screen_next()
    elif 'screen_prev' in name:
        try:
            screen_prev(args[0])
        except IndexError:
            screen_prev()
    elif 'jump_left' in name:
        jump_left()
    elif 'jump_right' in name:
        jump_right()
    elif 'jump_up' in name:
        jump_up()
    elif 'jump_down' in name:
        jump_down()
    elif 'click_left' in name:
        try:
            click_left(int(args[0]), int(args[1]),
                       int(args[2]), int(args[3]))
        except IndexError:
            click_left()
    elif 'click_right' in name:
        try:
            click_right(int(args[0]), int(args[1]),
                        int(args[2]), int(args[3]))
        except IndexError:
            click_right()
    elif 'click_middle' in name:
        try:
            click_middle(int(args[0]), int(args[1]),
                         int(args[2]), int(args[3]))
        except IndexError:
            click_middle()
    elif 'toggle_hold_left' in name:
        toggle_hold_left()
    elif 'toggle_hold_right' in name:
        toggle_hold_right()
    elif 'toggle_hold_middle' in name:
        toggle_hold_middle()
    elif 'scroll_up' in name:
        try:
            scroll_up(int(args[0]), int(args[1]))
        except IndexError:
            scroll_up()
    elif 'scroll_down' in name:
        try:
            scroll_down(int(args[0]), int(args[1]))
        except IndexError:
            scroll_down()
    elif 'scroll_left' in name:
        try:
            scroll_left(int(args[0]), int(args[1]))
        except IndexError:
            scroll_left()
    elif 'scroll_right' in name:
        try:
            scroll_right(int(args[0]), int(args[1]))
        except IndexError:
            scroll_right()
    elif 'move_abs' in name:
        try:
            move_abs(int(args[0]), int(args[1]))
        except IndexError:
            print("ERROR: {} missing arguments".format(name))
            quit(1)
    elif 'move_rel' in name:
        try:
            move_rel(int(args[0]), int(args[1]))
        except IndexError:
            print("ERROR: {} missing arguments".format(name))
            quit(1)
    elif 'drag_abs' in name:
        try:
            drag_abs(args[0], int(args[1]), int(args[2]), int(args[3]))
        except IndexError:
            print("ERROR: {} missing arguments".format(name))
            quit(1)
    elif 'drag_rel' in name:
        try:
            drag_rel(args[0], int(args[1]), int(args[2]), int(args[3]))
        except IndexError:
            print("ERROR: {} missing arguments".format(name))
            quit(1)
    elif 'left' in name:
        try:
            left(args[0])
        except IndexError:
            left()
    elif 'right' in name:
        try:
            right(args[0])
        except IndexError:
            right()
    elif 'up' in name:
        try:
            up(args[0])
        except IndexError:
            up()
    elif 'down' in name:
        try:
            down(args[0])
        except IndexError:
            down()
    elif 'wait' in name:
        try:
            wait(int(args[0]))
        except IndexError:
            print("ERROR: {} missing arguments".format(name))
            quit(1)
    else:
        if get_verbose():
            print("Unassigned/Undefined")


def execute_key_combination():
    if get_verbose():
        print(kl.current_key_combination)

    current_key_combination_str = ""
    for key in kl.current_key_combination:
        current_key_combination_str += str(key).replace("Key.", "").lower()
        if not key == kl.current_key_combination[-1]:
            current_key_combination_str += "+"

    for keymap in kl.config_items:
        if current_key_combination_str == keymap[1]:
            fn_parser(keymap[0])
            return


def quit(code: int = 0):
    if get_verbose():
        print("Quit\n")
    try:
        kl.listener.stop()
    except:
        pass
    exit(code)


def left(steps: int = 1):
    if get_verbose():
        print("Left\n")
    if steps <= 0:
        print("ERROR: Steps must be greater than 0")
        quit(1)
    for i in range(steps):
        moveRel(-kl.config_json["step_multiplier"], 0)


def right(steps: int = 1):
    if get_verbose():
        print("Right\n")
    if steps <= 0:
        print("ERROR: Steps must be greater than 0")
        quit(1)
    for i in range(steps):
        moveRel(kl.config_json["step_multiplier"], 0)


def up(steps: int = 1):
    if get_verbose():
        print("Up\n")
    if steps <= 0:
        print("ERROR: Steps must be greater than 0")
        quit(1)
    for i in range(steps):
        moveRel(0, -kl.config_json["step_multiplier"])


def down(steps: int = 1):
    if get_verbose():
        print("Down\n")
    if steps <= 0:
        print("ERROR: Steps must be greater than 0")
        quit(1)
    for i in range(steps):
        moveRel(0, kl.config_json["step_multiplier"])


def centralize():
    if get_verbose():
        print("Centralize\n")
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def centralize_root():
    if get_verbose():
        print("Centralize root\n")
    kl.set_current_boundary(kl.screens[kl.current_screen_index][0],
                            kl.screens[kl.current_screen_index][1])
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def screen_index(index: int = 0):
    if get_verbose():
        print("Select screen index {}\n".format(index))
    if abs(index) >= len(kl.screens):
        print("ERROR: Screen index out of range!")
        quit(1)
    if index < 0:
        index = len(kl.screens) - abs(index)
    kl.set_current_screen_index(index)
    mj.jumpToCenter(kl.screens[index][0], kl.screens[index][1])


def screen_next(steps: int = 1):
    if get_verbose():
        print("Next screen\n")
    new_index = kl.current_screen_index + steps
    if new_index >= len(kl.screens):
        new_index = 0
    kl.set_current_screen_index(new_index)
    mj.jumpToCenter(kl.screens[new_index][0], kl.screens[new_index][1])


def screen_prev(steps: int = 1):
    if get_verbose():
        print("Previous screen\n")
    new_index = kl.current_screen_index - steps
    if new_index < 0:
        new_index = len(kl.screens) - 1
    kl.set_current_screen_index(new_index)
    mj.jumpToCenter(kl.screens[new_index][0], kl.screens[new_index][1])


def jump_left():
    if get_verbose():
        print("Jump left\n")
    new_boundary = mj.cut_boundary_left(kl.current_boundary[0],
                                        kl.current_boundary[1])
    kl.set_current_boundary(new_boundary[0], new_boundary[1])
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def jump_right():
    if get_verbose():
        print("Jump right\n")
    new_boundary = mj.cut_boundary_right(kl.current_boundary[0],
                                         kl.current_boundary[1])
    kl.set_current_boundary(new_boundary[0], new_boundary[1])
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def jump_up():
    if get_verbose():
        print("Jump up\n")
    new_boundary = mj.cut_boundary_up(kl.current_boundary[0],
                                      kl.current_boundary[1])
    kl.set_current_boundary(new_boundary[0], new_boundary[1])
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def jump_down():
    if get_verbose():
        print("Jump down\n")
    new_boundary = mj.cut_boundary_down(kl.current_boundary[0],
                                        kl.current_boundary[1])
    kl.set_current_boundary(new_boundary[0], new_boundary[1])
    mj.jumpToCenter(kl.current_boundary[0], kl.current_boundary[1])


def click_left(x: int = -1, y: int = -1, clicks: int = 1, delay_ms: int = 0):
    if get_verbose():
        print("Click left\n")
    if delay_ms < 0:
        print("ERROR: Delay must be greater than or equal to 0!")
        quit(1)
    if x > -1:
        moveTo(x)
    if y > -1:
        moveTo(y)
    click(button='left', clicks=clicks, interval=delay_ms/1000)


def click_right(x: int = -1, y: int = -1, clicks: int = 1, delay_ms: int = 0):
    if get_verbose():
        print("Click right\n")
    if delay_ms < 0:
        print("ERROR: Delay must be greater than or equal to 0!")
        quit(1)
    if x > -1:
        moveTo(x)
    if y > -1:
        moveTo(y)
    click(button='right', clicks=clicks, interval=delay_ms/1000)


def click_middle(x: int = -1, y: int = -1, clicks: int = 1, delay_ms: int = 0):
    if get_verbose():
        print("Click middle\n")
    if delay_ms < 0:
        print("ERROR: Delay must be greater than or equal to 0!")
        quit(1)
    if x > -1:
        moveTo(x)
    if y > -1:
        moveTo(y)
    click(button='middle', clicks=clicks, interval=delay_ms/1000)


def toggle_hold_left():
    if kl.mouse_left_holding:
        mouseUp(button='left')
        if get_verbose():
            print("Toggle hold left (up)\n")
    else:
        mouseDown(button='left')
        if get_verbose():
            print("Toggle hold left (down)\n")

    kl.set_mouse_left_holding(not kl.mouse_left_holding)


def toggle_hold_right():
    if kl.mouse_right_holding:
        mouseUp(button='right')
        if get_verbose():
            print("Toggle hold right (up)\n")
    else:
        mouseDown(button='right')
        if get_verbose():
            print("Toggle hold right (down)\n")

    kl.set_mouse_right_holding(not kl.mouse_right_holding)


def toggle_hold_middle():
    if kl.mouse_middle_holding:
        mouseUp(button='middle')
        if get_verbose():
            print("Toggle hold middle (up)\n")
    else:
        mouseDown(button='middle')
        if get_verbose():
            print("Toggle hold middle (down)\n")

    kl.set_mouse_middle_holding(not kl.mouse_middle_holding)


def scroll_up(steps: int = 1, delay_ms: int = 10):
    if get_verbose():
        print("Scroll up {} times with {}ms interval\n".format(steps, delay_ms))
    if delay_ms <= 0:
        print("ERROR: Delay must be greater than 0!")
        quit(1)
    for i in range(steps):
        vscroll(kl.config_json["scroll_multiplier"])
        if i != steps-1:
            sleep(delay_ms/1000)


def scroll_down(steps: int = 1, delay_ms: int = 10):
    if get_verbose():
        print("Scroll up {} times\n".format(steps))
    if delay_ms <= 0:
        print("ERROR: Delay must be greater than 0!")
        quit(1)
    for i in range(steps):
        if get_verbose():
            print("Scroll #{}".format(i+1))
        vscroll(-kl.config_json["scroll_multiplier"])
        if i != steps-1:
            sleep(delay_ms/1000)


def scroll_left(steps: int = 1, delay_ms: int = 10):
    if get_verbose():
        print("Scroll left {} times\n".format(steps))
    if delay_ms <= 0:
        print("ERROR: Delay must be greater than 0!")
        quit(1)
    for i in range(steps):
        hscroll(-kl.config_json["scroll_multiplier"])
        if i != steps-1:
            sleep(delay_ms/1000)


def scroll_right(steps: int = 1, delay_ms: int = 10):
    if get_verbose():
        print("Scroll right {} times\n".format(steps))
    if delay_ms <= 0:
        print("ERROR: Delay must be greater than 0!")
        quit(1)
    for i in range(steps):
        hscroll(kl.config_json["scroll_multiplier"])
        if i != steps-1:
            sleep(delay_ms/1000)


def move_abs(x: int = 0, y: int = 0, duration_ms: int = 0):
    if get_verbose():
        print("Move to ({}, {}) over {}ms\n".format(x, y, duration_ms))
    if duration_ms < 0:
        print("ERROR: Duration must be greater than or equal to 0!")
        quit(1)
    moveTo(x, y, duration_ms/1000)


def move_rel(x: int = 0, y: int = 0, duration_ms: int = 0):
    if get_verbose():
        print("Move relative ({}, {}) over {}ms\n".format(x, y, duration_ms))
    if duration_ms < 0:
        print("ERROR: Duration must be greater than or equal to 0!")
        quit(1)
    moveRel(x, y, duration_ms/1000)


def drag_abs(button: str = "left", x: int = 0, y: int = 0, duration_ms: int = 0):
    if get_verbose():
        print("Drag with {} button to ({}, {}) over {}ms\n".format(
            button, x, y, duration_ms))
    if duration_ms < 0:
        print("ERROR: Duration must be greater than or equal to 0!")
        quit(1)
    dragTo(x, y, duration_ms/1000, button=button)


def drag_rel(button: str = "left", x: int = 0, y: int = 0, duration_ms: int = 0):
    if get_verbose():
        print("Drag with {} button relative ({}, {}) over {}ms\n".format(
            button, x, y, duration_ms))
    if duration_ms < 0:
        print("ERROR: Duration must be greater than or equal to 0!")
        quit(1)
    dragRel(x, y, duration_ms/1000, button=button)


def wait(duration_ms: int = 0):
    if get_verbose():
        print("Wait {}ms\n".format(duration_ms))
    if duration_ms < 0:
        print("ERROR: Duration must be greater than or equal to 0!")
        quit(1)
    sleep(duration_ms/1000)
