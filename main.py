import pyxel, random

class City:
    def __init__(self):
        pyxel.init(600,950, title="City Generator and NPCs", display_scale=2)
        pyxel.run(self.update,self.draw)

    def updtae(self):
        pass

    def draw(self):
        pass