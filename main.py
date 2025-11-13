import pyxel,random,math

class City:
    def __init__(self):
        self.buildings = []
        #pyxel.init(950,600, title="City Generator and NPCs", display_scale=2)
        #pyxel.run(self.update,self.draw)
        self.building_count = 0
    def gen_world(self):
        '''build buildings, place buildings'''
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def create_building(self,pos):
        '''takes a position and returns a list of coords for a building placement with 90° angles'''
        self.building_count += 1
        x,y = pos
        pos_list = []
        pos_list.append((x,y))
        largeness = random.randint(5,10)
        angle = random.randint(0,360)
        print(angle,largeness)
        for i in range(3):
            x2 = x+largeness*math.sin(angle+i*90)
            y2 = y+largeness*math.cos(angle+i*90)
            pos_list.append((x2,y2))
        print(f"Position of Building #{self.building_count} corners: {pos_list}")
        return pos_list
        pass

    def create_paths(self):
        """URGH IT'S BROKEN AND IDK why creates path between buildings"""
        """
        middle_pos = [(i[0]+i[1]),((i[2]+i[3]) for i in self.buildings]
        existing_roads = []
        for i in self.middle_pos:
            for j in self.middle_pos:
                if i != j:
                    new_road = (i, j)
                    if new_road not in existing_roads:
                        existing_roads.append(new_road)
        """

    def place_building(self,pos):
        '''takes a pos_list and draws the lines between the points'''
        pyxel.line(pos[0], pos[1], pos[2], pos[3],7)
        pyxel.line(pos[1], pos[2], pos[3], pos[0], 7)
        pyxel.line(pos[2], pos[3], pos[0], pos[1], 7)
        pyxel.line(pos[3], pos[0], pos[1], pos[2], 7)

'''what we want:
buildings (obstacles), roads (pats)--> coords? --> Blocky or continuous?'''
city = City()
city.create_building((1,1))