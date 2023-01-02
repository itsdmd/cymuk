# Mouse Jump Movement

# "Boundary" is the area that have the mouse cursor at the center of it. The
# 	base boundary is the screen.
#
# Jump functions will move the cursor to the center of the boundary half the
# 	area of the original boundary in the direction of the jump.
#
# For example, if you perform a jump to the right, the cursor will move to the
# 	center point between its original position and the right side of the
# 	boundary, which is also the center of the boundary that takes up half the
# 	area to the right of the original boundary.

import pyautogui as pag		# Control mouse cursor


def isValidBoundary(topLeft: tuple[int, int], bottomRight: tuple[int, int]):
    print("\nValidating boundary (", str(topLeft), str(bottomRight), ")")
    if (topLeft[0] >= bottomRight[0]) or (topLeft[1] >= bottomRight[1]):
        print("\nInvalid boundary!")
        return False
    return True


def jumpToCenter(topLeft: tuple[int, int], bottomRight: tuple[int, int]):
    if isValidBoundary(topLeft, bottomRight):
        pag.moveTo(
            (topLeft[0] + bottomRight[0]) // 2,
            (topLeft[1] + bottomRight[1]) // 2)


def cut_boundary_left(topLeft: tuple[int, int],
                      bottomRight: tuple[int, int]):
    return (topLeft,
            ((topLeft[0] + bottomRight[0]) // 2, bottomRight[1]))


def cut_boundary_right(topLeft: tuple[int, int],
                       bottomRight: tuple[int, int]):
    return (((topLeft[0] + bottomRight[0]) // 2, topLeft[1]),
            bottomRight)


def cut_boundary_up(topLeft: tuple[int, int],
                    bottomRight: tuple[int, int]):
    return (topLeft,
            (bottomRight[0], (topLeft[1] + bottomRight[1]) // 2))


def cut_boundary_down(topLeft: tuple[int, int],
                      bottomRight: tuple[int, int]):
    return ((topLeft[0], (topLeft[1] + bottomRight[1]) // 2),
            bottomRight)
