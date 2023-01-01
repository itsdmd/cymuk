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


def isValidBox(topLeft, bottomRight):
    if (topLeft[0] >= bottomRight[0]) or (topLeft[1] >= bottomRight[1]):
        print("Invalid box.")
        return False
    return True


def moveToCenter(topLeft=(0, 0), bottomRight=(0, 0)):
    if not isValidBox(topLeft, bottomRight):
        return
    pag.moveTo((topLeft[0]+bottomRight[0])/2, (topLeft[1]+bottomRight[1])/2)


def jumpUp(topLeft=(0, 0), bottomRight=(0, 0)):
    if not isValidBox(topLeft, bottomRight):
        return
    pag.moveTo((topLeft[0]+bottomRight[0])/2, (topLeft[1]+bottomRight[1])/4)


def jumpDown(topLeft=(0, 0), bottomRight=(0, 0)):
    if not isValidBox(topLeft, bottomRight):
        return
    pag.moveTo((topLeft[0]+bottomRight[0])/2, (topLeft[1]+bottomRight[1])*3/4)


def jumpLeft(topLeft=(0, 0), bottomRight=(0, 0)):
    if not isValidBox(topLeft, bottomRight):
        return
    pag.moveTo((topLeft[0]+bottomRight[0])/4, (topLeft[1]+bottomRight[1])/2)


def jumpRight(topLeft=(0, 0), bottomRight=(0, 0)):
    if not isValidBox(topLeft, bottomRight):
        return
    pag.moveTo((topLeft[0]+bottomRight[0])*3/4, (topLeft[1]+bottomRight[1])/2)
