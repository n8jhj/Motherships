#C:\\Python27\python.exe

from pygame import image
from game_utils import p2c, rot_center


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
        self.mvmt = 0.2

    # draw self
    def draw(self):
        self.surf.blit(rot_center(self.img, self.a_pos),
                       p2c((self.x_pos - self.img_size[0]/2,
                            self.y_pos + self.img_size[1]/2)))

    # accelerate
    def accelerate(self, (x_dir,y_dir)):
        self.x_vel += x_dir * self.mvmt
        self.y_vel += y_dir * self.mvmt

    # accelerate in angular direction
    def torque(self, a_dir):
        self.a_vel += a_dir * self.mvmt

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
