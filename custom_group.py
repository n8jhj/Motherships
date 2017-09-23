#C:\\Python27\python.exe

from pygame import sprite


class CustomGroup(sprite.Group):
    def __init__(self, *sprites):
        super(CustomGroup, self).__init__(*sprites)

    def draw(self, *args):
        """Call the draw method of every contained sprite.
        """
        for s in self.sprites():
            s.draw(*args)

    def contains(self, obj_type):
        value = False
        for s in self.sprites():
            if isinstance(s, obj_type):
                return s
