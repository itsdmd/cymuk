# Mouse Jump Movement

from pyautogui import moveTo


def isValidBoundary(topLeft: tuple[int, int], bottomRight: tuple[int, int]):
    print("\nValidating boundary (", str(topLeft), str(bottomRight), ")")
    if (topLeft[0] >= bottomRight[0] + 2) or (topLeft[1] >= bottomRight[1] + 2):
        print("\nInvalid boundary!")
        return False
    return True


def jumpToCenter(topLeft: tuple[int, int], bottomRight: tuple[int, int]):
    if isValidBoundary(topLeft, bottomRight):
        moveTo((topLeft[0] + bottomRight[0]) // 2,
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
