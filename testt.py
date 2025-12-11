
import math
#scrolling background
class Ship:
    def __init__(self):
        posX = 0
        posY = 0
        speed = 0
        dir = 0
class Board:
    def __init__(self):
        self.ship = Ship()
        self.surface = None
        # here we can build islands and stuff on it but otherwise its just infinite blue
    def update_speed(self):
        self.Xspeed = math.sin(self.ship.dir) * self.ship.speed
        self.Yspeed = math.cos(self.ship.dir) * self.ship.speed
    def update_pos(self):
        self.posX -= self.Xspeed
        self.posY -= self.Yspeed

#we need a screen and
