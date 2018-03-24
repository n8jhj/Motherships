#C:\\Python27\python.exe

from pygame import display
from pygame.locals import *
from custom_group import CustomGroup
from ship import Ship
from colors import *


class Game(object):
    def __init__(self, surf):
        self.surf = surf
        self.is_going = True # whether the game has been quit
        self.key_function = {
            K_UP:       self.accel_ship_forward,
            K_DOWN:     self.accel_ship_backward,
            K_LEFT:     self.torque_ship_left,
            K_RIGHT:    self.torque_ship_right,
            K_q:        self.quit_game,
            K_s:        self.stop_ship
            }
        self.pressed = {}
        self.p1_sprites = CustomGroup()
        self.static_sprites = CustomGroup()
        self.add_ships()

    def update(self):
        '''Update game state'''
        for key in self.pressed:
            if self.pressed[key]:
                self.key_function[key]()
        self.p1_sprites.update()
        return self.is_going

    def draw(self):
        '''Draw the game window'''
        self.surf.fill(BLACK)
        self.p1_sprites.draw(self.surf)
        display.update()

    def add_ships(self):
        '''Add ships to self.moving_sprites'''
        ship_1 = Ship(self, self.surf, 50, 50)
        self.p1_sprites.add(ship_1)

    def get_ship_of_player(self, pnum):
        if pnum == 1:
            return self.p1_sprites.contains(Ship)

    def key_action(self, key, press):
        self.pressed[key] = press

    # __________KEY_PRESS_FUNCTIONS____________
    
    def accel_ship_forward(self):
        '''K_UP'''
        ship = self.get_ship_of_player(1)
        ship.accelerate_forward()

    def accel_ship_backward(self):
        '''K_DOWN'''
        ship = self.get_ship_of_player(1)
        ship.accelerate_backward()

    def torque_ship_left(self):
        '''K_LEFT'''
        ship = self.get_ship_of_player(1)
        ship.torque(1)

    def torque_ship_right(self):
        '''K_RIGHT'''
        ship = self.get_ship_of_player(1)
        ship.torque(-1)

    def quit_game(self):
        '''K_q'''
        self.is_going = False

    def stop_ship(self):
        '''K_s'''
        ship = self.get_ship_of_player(1)
        ship.stop()
