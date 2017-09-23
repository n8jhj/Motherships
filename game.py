#C:\\Python27\python.exe

from pygame import display
from pygame.locals import *
from custom_group import CustomGroup
from ship import Ship
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
        self.p1_sprites = CustomGroup()
        self.static_sprites = CustomGroup()
        self.add_ships()

    # add ships to self.moving_sprites
    def add_ships(self):
        ship_1 = Ship(self, self.surf, (50,50))
        self.p1_sprites.add(ship_1)

    # update game state
    def update(self):
        for key in self.pressed:
            if self.pressed[key]:
                self.key_function[key]()
        self.p1_sprites.update()

    def draw(self):
        self.surf.fill(BLACK)
        self.p1_sprites.draw(self.surf)
        display.update()

    def key_action(self, key, press):
        self.pressed[key] = press

    def get_ship_of_player(self, pnum):
        if pnum == 1:
            return self.p1_sprites.contains(Ship)

    def accel_ship_forward(self):
        ship = self.get_ship_of_player(1)
        ship.accelerate_forward()

    def accel_ship_backward(self):
        ship = self.get_ship_of_player(1)
        ship.accelerate_backward()

    def stop_ship(self):
        ship = self.get_ship_of_player(1)
        ship.stop()

    def torque_ship_left(self):
        ship = self.get_ship_of_player(1)
        ship.torque(1)

    def torque_ship_right(self):
        ship = self.get_ship_of_player(1)
        ship.torque(-1)
