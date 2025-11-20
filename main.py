import random, pyxel, math
from idlelib.window import add_windows_to_menu


class Maze:
    def __init__(self,size):
        x,y = size
        self.x,self.y = x,y
        self.grid = {(i,j):0 for i in range(x) for j in range(y)}

        #print(self.grid)
    def neighbors(self, pos):
        x0, y0 = pos
        candidates = [(x0 - 1, y0), (x0 + 1, y0), (x0, y0 - 1), (x0, y0 + 1)]
        return [p for p in candidates if p in self.grid]
    def pp_walls(self):
        '''prepp and place walls for the map'''

        dist = int(math.sqrt(self.x**2 + self.y**2)/2)
        for i in range(dist):
            wall_pos = (i+random.randint(-1,1),random.randint(0,self.y)) if i not in (0,self.x) else (i)
            wall_size = (random.randint(1, int((self.x - 1) / 2))), random.randint(1, int((self.y - 1) / 2))
            for y in range(wall_pos[1],wall_size[1]):
                for x in range(wall_pos[0],wall_pos[1]):
                    self.grid[(x,y)] = 1

        # instead make the bot trace paths from the get go and trace walls around
    def __str__(self):
        for i in range
        print(self.grid)

    def screen(self):
        pyxel.init(200,200,title="Maze")


maze = Maze((10,10))
print(maze.neighbors((1,1)))
print(maze)