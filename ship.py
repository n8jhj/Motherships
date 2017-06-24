from pygame import image

class Ship(object):
    def __init__(self, imgFile):
        self.img = image.load(imgFile)
        self.x_pos = 150
        self.y_pos = 20
        self.x_vel = 0
        self.y_vel = 0

    def accelerate(self, x_acc, y_acc):
        self.x_vel += x_acc
        self.y_vel += y_acc

    def update_position(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
