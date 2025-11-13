import pyxel,random

class City:
    def __init__(self):
        pyxel.init(600,950, title="City Generator and NPCs", display_scale=2)
        pyxel.run(self.update,self.draw)
    def gen_world(self):
        #build buildings, place buildings
        #
        pass
    def update(self):
        pass

    def draw(self):
        pass
    def create_building(self,pos):
        '''takes a position and returns a list of coords for a building placement with 90° angles'''
        x,y = pos
        pos_list = []
        
        return pos_list
        pass

    def building_place(self,pos):
            pyxel.line(pos[0],pos[1],pos[2],pos[3],7)
            pyxel.line(pos[0], pos[1], pos[2], pos[3], 7)
            pyxel.line(pos[0], pos[1], pos[2], pos[3], 7)
            pyxel.line(pos[0], pos[1], pos[2], pos[3], 7)

'''what we want:
buildings (obstacles), roads (pats)--> coords? --> Blocky or continuous?'''
