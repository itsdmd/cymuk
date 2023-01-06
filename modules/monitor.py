# Continuously Prints The Mouse Position To The Console

import pyautogui as pag
from time import sleep

pag.PAUSE = 0.1


def main():
    while True:
        print(pag.position())
        sleep(pag.PAUSE)
