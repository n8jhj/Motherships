#C:\\Python27\python.exe

from pygame import display
from pygame.locals import *
from mothership import Mothership
from colors import *


class Game(object):
    def __init__(self, surf):
        self.surf = surf
        self.key_function = {
            K_UP:       self.accel_ship_forward,
            K_DOWN:     self.accel_ship_backward,
            K_LEFT:     self.torque_ship_left,
            K_RIGHT:    self.torque_ship_right,
            K_s:        self.stop_ship
            }
        self.pressed = {}
        self.ship = Mothership(self.surf, (50,50))

    def update(self):
        for key in self.pressed:
            if self.pressed[key]:
                self.key_function[key]()
        self.ship.update_pos()

    def draw(self):
        self.surf.fill(BLACK)
        self.ship.draw()
        display.update()

    def key_action(self, key, press):
        self.pressed[key] = press

    def accel_ship_forward(self):
        self.ship.accelerate_forward()

    def accel_ship_backward(self):
        self.ship.accelerate_backward()

    def stop_ship(self):
        self.ship.stop()

    def torque_ship_left(self):
        self.ship.torque(1)

    def torque_ship_right(self):
        self.ship.torque(-1)
