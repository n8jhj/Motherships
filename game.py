from pygame import image
from pygame.locals import *
from mothership import Mothership


class Game(object):
    def __init__(self, surf):
        self.surf = surf
        self.key_dict = {
            K_UP:       self.key_press_up,
            K_DOWN:     self.key_press_down,
            K_LEFT:     self.key_press_left,
            K_RIGHT:    self.key_press_right
            }
        self.ship = Mothership()

    def draw(self):
        print (self.ship.x_vel, self.ship.y_vel)
        self.surf.blit(self.ship.img, (50,50))

    def key_press(self, key):
        self.key_dict[key]()

    def key_press_up(self):
        self.ship.accelerate(0, 1)

    def key_press_down(self):
        self.ship.accelerate(0, -1)

    def key_press_left(self):
        self.ship.accelerate(-1, 0)

    def key_press_right(self):
        self.ship.accelerate(1, 0)
