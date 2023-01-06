# Continuously Prints The Mouse Position To The Console

import pyautogui as pag
from time import sleep

pag.PAUSE = 0.1


def main():
    msg = str(pag.position())

    while True:
        if msg != str(pag.position()):
            msg = str(pag.position())
            print(msg)
        sleep(pag.PAUSE)
