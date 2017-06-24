#C:\\Python27\python.exe

from pygame import display
from pygame.locals import *
from mothership import Mothership
from colors import *


class Game(object):
    def __init__(self, surf):
        self.surf = surf
        self.key_dict = {
            K_UP:       self.key_up,
            K_DOWN:     self.key_down,
            K_LEFT:     self.key_left,
            K_RIGHT:    self.key_right,
            K_a:        self.key_a,
            K_d:        self.key_d,
            K_s:        self.key_s
            }
        self.ship = Mothership(self.surf, (50,50))

    def update(self):
        self.ship.update_pos()

    def draw(self):
        self.surf.fill(BLACK)
        self.ship.draw()
        display.update()

    def key_action(self, key, press):
        self.key_dict[key](press)

    def key_up(self, press):
        self.ship.accelerate((0,1))

    def key_down(self, press):
        self.ship.accelerate((0,-1))

    def key_left(self, press):
        self.ship.accelerate((-1,0))

    def key_right(self, press):
        self.ship.accelerate((1,0))

    def key_a(self, press):
        self.ship.torque(1)

    def key_d(self, press):
        self.ship.torque(-1)

    def key_s(self, press):
        self.ship.stop()
