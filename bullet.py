#C:\\Python27\python.exe

from pygame import image, sprite
from game_utils import coordinates_pygame_to_cartesian as p2c, rot_center
from game_constants import BULLET_SPEED
import math


class Bullet(sprite.Sprite):
    def __init__(self, img_file_flying, img_file_splat, surf, (x,y), angle):
        super(Bullet, self).__init__()
        self.surf = surf
        self.image = image.load(img_file_flying)
        self.img_splat = image.load(img_file_splat)
        self.img_size_flying = (4, 28) # image size in pixels
        self.img_size_splat = (19, 19)
        self.x_pos = x
        self.y_pos = y
        self.angle = angle + 90
        self.speed = BULLET_SPEED

    # update self on self.surf
    def update(self):
        angle_rad = math.radians(self.angle)
        self.x_pos += self.speed * math.cos(angle_rad)

    # draw self
    def draw(self, surf):
        surf.blit(rot_center(self.image, self.angle),
                    p2c((self.x_pos - self.img_size[0]/2,
                        self.y_pos + self.img_size[1]/2)))

    # set self.angle, accounting for 90 degree shift
    def set_angle(self, angle):
        self.angle = angle + 90
