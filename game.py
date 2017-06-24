import pygame
from pygame.locals import *


def key_press_up():
    print 'up'


def key_press_down():
    print 'down'


def key_press_left():
    print 'left'


def key_press_right():
    print 'right'


key_dict = {
    K_UP:       key_press_up,
    K_DOWN:     key_press_down,
    K_LEFT:     key_press_left,
    K_RIGHT:    key_press_right
    }


def key_press(key):
    key_dict[key]()
