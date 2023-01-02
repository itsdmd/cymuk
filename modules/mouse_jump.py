# Mouse Jump Movement

# "Box" is the area that have the mouse cursor at the center of it. The base
# box is the screen.
#
# Jump functions will move the cursor to the center of the box half the area of
# the original box in the direction of the jump.
#
# For example, if you perform a jump to the right, the cursor will move to the
# center point between its original position and the right side of the box,
# which is also the center of the box that takes up half the area to the right
# of the original box.

import pyautogui as pag		# Control mouse cursor


def isValidBox(topLeft: tuple[int, int], bottomRight: tuple[int, int]):
    print("\nValidating box (", str(topLeft), str(bottomRight), ")")
    if (topLeft[0] >= bottomRight[0]) or (topLeft[1] >= bottomRight[1]):
        print("\nInvalid box!")
        return False
    return True


def jumpToCenter(topLeft: tuple[int, int], bottomRight: tuple[int, int]):
    if isValidBox(topLeft, bottomRight):
        pag.moveTo(
            (topLeft[0] + bottomRight[0]) // 2,
            (topLeft[1] + bottomRight[1]) // 2)


def cut_box_left(topLeft: tuple[int, int],
                 bottomRight: tuple[int, int]):
    return (
        topLeft,
        ((topLeft[0] + bottomRight[0]) // 2, bottomRight[1]))


def cut_box_right(topLeft: tuple[int, int],
                  bottomRight: tuple[int, int]):
    return (
        ((topLeft[0] + bottomRight[0]) // 2, topLeft[1]),
        bottomRight)


def cut_box_up(topLeft: tuple[int, int],
               bottomRight: tuple[int, int]):
    return (
        topLeft,
        (bottomRight[0], (topLeft[1] + bottomRight[1]) // 2))


def cut_box_down(topLeft: tuple[int, int],
                 bottomRight: tuple[int, int]):
    return (
        (topLeft[0], (topLeft[1] + bottomRight[1]) // 2),
        bottomRight)
