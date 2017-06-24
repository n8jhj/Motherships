#C:\\Python27\python.exe

"""
MOTHERSHIPS

A game in which players vie for their place on a galactic battlefield.

"""

# __________________________79_CHARACTERS______________________________________


import pygame
from pygame.locals import *
import os
import game
from game_constants import SIZE

# set up pygame
#os.environ['SDL_VIDEO_CENTERED'] = '1' # center pygame window #temporary
DISPSURF = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Motherships')
pygame.init()

# set up Clock
FPS = 30
fps_clock = pygame.time.Clock()

# set up game
m_game = game.Game(DISPSURF)


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
            m_game.key_action(event.key, True)
        if event.type == KEYUP:
            m_game.key_action(event.key, False)
    m_game.update()
    return True


def view_tick():
    m_game.draw()


if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
        # sys.exit() #temporary
