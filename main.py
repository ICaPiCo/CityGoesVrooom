import pyxel,random,math

class City:
    def __init__(self):
        self.buildings = []
        pyxel.init(950,600, title="City Generator and NPCs", display_scale=2)
        pyxel.run(self.update,self.draw)
        self.building_count = 0
    def gen_world(self):
        '''build buildings, place buildings'''
        self.place_building(self.create_building((1,1)))
        pass

    def update(self):
        pass

    def draw(self):
        pass
    def create_building(self, pos):

        """Takes a position and returns a list of coordinates for a rotated square building."""
        self.building_count += 1
        x, y = pos
        pos_list = []

        # Size and angle
        size = random.randint(5, 10)
        angle_deg = random.randint(0, 360)
        angle = math.radians(angle_deg)

        # Half size to center the building
        half = size / 2

        # Define square corners relative to the center (x, y)
        corners = [
            (-half, -half),
            (half, -half),
            (half, half),
            (-half, half)
        ]
        # Rotation formula:
        # x' = x*cos(θ) - y*sin(θ)
        # y' = x*sin(θ) + y*cos(θ) --> matrices! urgh
        for cx, cy in corners:
            rx = cx * math.cos(angle) - cy * math.sin(angle)
            ry = cx * math.sin(angle) + cy * math.cos(angle)
            pos_list.append((x + rx, y + ry))

        #print(f"Angle: {angle_deg}°, size: {size},pos_list: {pos_list}")
        return pos_list

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
