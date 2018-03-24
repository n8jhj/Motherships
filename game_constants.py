#C:\\Python27\python.exe

"""
GAME_CONSTANTS.PY
Contains all constants used in the game Motherships.
"""

import ctypes


# __WINDOW_SIZE________________________________________________________________
def screen_size():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def pygame_window_size():
    screensize = screen_size()
    return (screensize[0]-2, screensize[1]-26)

BULLET_SPEED = 0.8
SHIP_THRUST = 0.1
SIZE = pygame_window_size()
