#C://Python27/python.exe

"""
MOTHERSHIPS

A game in which players vie for their place on a galactic battlefield.

"""

# __________________________79_CHARACTERS______________________________________


import pygame
from pygame.locals import *
import game

# set up pygame
SIZE = (700, 400)
DISPSURF = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Motherships')
pygame.init()

# set up Clock
FPS = 30
fps_clock = pygame.time.Clock()


def main():
    going = True

    while going:
        going = controller_tick()
        view_tick()
        fps_clock.tick(FPS) # clock


def controller_tick():
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        if event.type == KEYDOWN:
            if event.key == K_q:
                return False
            game.key_press(event.key)
    return True


def view_tick():
    pass


if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
        # sys.exit() #temporary