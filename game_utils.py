#C:\\Python27\python.exe

from game_constants import SIZE
from pygame import transform


# Pygame to Cartesian coordinates
def coordinates_pygame_to_cartesian(xp, yp):
    return xp, SIZE[1]-yp

# rotate an image about its center and keeping its size
def rot_center(img, angle):
    orig_rect = img.get_rect()
    rot_img = transform.rotate(img, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_img.get_rect().center
    rot_img = rot_img.subsurface(rot_rect).copy()
    return rot_img
