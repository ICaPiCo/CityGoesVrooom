"""Actual pathfinding prototype to impement for later"""
import pyxel


class Findpath:
    def __init__(self,oX,oY,fX,fY):
        self.all_existing_paths = []
        pyxel.init(500,500,title="Path finding bot", display_scale=2)
        pyxel.run(self.update,self.draw)

    def update(self):
        pass

    def draw(self):
        pass
