from ship import Ship

class Mothership(Ship):
    def __init__(self, surf, (x,y)):
        super(Mothership, self).__init__(
            'ship_test.png', surf, (x,y)
            )
