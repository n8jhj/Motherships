#C:\\Python27\python.exe

from pygame import image
from game_utils import p2c, rot_center
from game_constants import SHIP_MOVEMENT
import math


class Ship(object):
    def __init__(self, imgFile, surf, (x,y)):
        self.surf = surf
        self.img = image.load(imgFile)
        self.img_size = (36,36) # size of image, in pixels
        self.x_pos = x
        self.y_pos = y
        self.x_vel = 0
        self.y_vel = 0
        self.a_pos = 0 # angular position
        self.a_vel = 0 # angular velocity
        self.mvmt = SHIP_MOVEMENT

    # draw self
    def draw(self):
        self.surf.blit(rot_center(self.img, self.a_pos),
                       p2c((self.x_pos - self.img_size[0]/2,
                            self.y_pos + self.img_size[1]/2)))

    # accelerate
    def accelerate(self, (x_dir,y_dir)):
        self.x_vel += x_dir * self.mvmt
        self.y_vel += y_dir * self.mvmt

    # angular accelerate
    def torque(self, a_dir):
        self.a_vel += a_dir * self.mvmt

    # accelerate in direction ship is facing
    # forward direction is 1, backward is -1
    def accelerate_forward(self, direction=1):
        angle = math.radians(self.a_pos + 90)
        x_component = math.cos(angle) * direction
        y_component = math.sin(angle) * direction
        self.accelerate((x_component, y_component))

    # accelerate opposite direction ship is facing
    def accelerate_backward(self):
        self.accelerate_forward(-1)

    # update position
    def update_pos(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.a_pos = (self.a_pos + self.a_vel) % 360

    # stop moving
    def stop(self):
        self.x_vel = 0
        self.y_vel = 0
        self.a_vel = 0
