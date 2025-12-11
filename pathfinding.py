import pyxel, random, math
import heapq


class Findpath:
    def __init__(self, size):
        self.size = size
        self.init()
        pyxel.init(size, size, title="Path finding bot")
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def init(self):
        self.walls = set()
        self.scanned = False
        self.oX = self.oY = 0
        self.fX = self.fY = 0
        self.grid = [[999999 for _ in range(self.size)] for _ in range(self.size)]
        self.found_path = False
        self.queue = []
        self.queue2 = {}
        self.poss_paths = []

    def scan_walls(self, colors):
        if self.scanned:
            return

        # scan walls
        for x in range(self.size):
            for y in range(self.size):
                if pyxel.pget(x, y) in colors:
                    self.walls.add((x, y))

        # pick valid start/end
        while True:
            self.oX = random.randint(0, self.size - 1)
            self.oY = random.randint(0, self.size - 1)
            self.fX = random.randint(0, self.size - 1)
            self.fY = random.randint(0, self.size - 1)

            if (
                (self.oX, self.oY) not in self.walls and
                (self.fX, self.fY) not in self.walls and
                not (self.oX == self.fX and self.oY == self.fY)
            ):
                break

        # start A*
        h = (self.oX - self.fX)**2 + (self.oY - self.fY)**2
        heapq.heappush(self.queue, (h, self.oX, self.oY, 0))

        self.scanned = True

    def spread_step(self):
        if not self.queue or self.found_path:
            return

        for _ in range(100):
            if not self.queue:
                break

            score, x, y, dist = heapq.heappop(self.queue)

            if not (0 <= x < self.size and 0 <= y < self.size):
                continue

            # walls block movement
            if (x, y) in self.walls:
                continue

            # already visited with shorter path
            if self.grid[y][x] <= dist:
                continue

            self.grid[y][x] = dist

            if x == self.fX and y == self.fY:
                self.found_path = True
                return

            # explore neighbors
            """
            for dx, dy in [
                (1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (-1, -1), (-1, 1), (1, -1)
            ]:
            """
            # explore neighbors only 4
            for dx, dy in [
                (1, 0), (-1, 0), (0, 1), (0, -1),
            ]:
                nx, ny = x + dx, y + dy # coordinates of the target square

                if not (0 <= nx < self.size and 0 <= ny < self.size):
                    continue

                # skip walls before pushing
                if (nx, ny) in self.walls:
                    continue

                if self.grid[ny][nx] > dist + 1:
                    h = (nx - self.fX)**2 + (ny - self.fY)**2 # distance to the destination
                    f = dist + 1 + h # prev. dist+1+this_dist // priority (based on distance from init. point and to dest. point)
                    heapq.heappush(self.queue, (f, nx, ny, dist + 1))
                    self.queue2[(nx,ny)] = (f, dist+1) #why dist + 1?

    def update(self):
        self.spread_step()
        #self.do()
    def neighbors(self,queue,point):
        '''takes in parameters a dict. and a point and returns the present neighbors'''
        x,y = point
        neighbors = []
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for _dir in dirs:
            P= (x + _dir[0], y + _dir[1])
            if queue[P]:
                neighbors.append(P)
        return neighbors
    def retrace(self,path):
        initpoint = self.queue2.keys()[0]
        queue = self.queue2[::-1] # queue dictionary with points as keys
        path = [queue.keys()[0]]

        for square in queue:
            priority,x,y,distance, = square
            point = (x,y)
            neighbors = self.neighbors(queue,point)
            # tracing path?
            if len(neighbors)>2:

                new_paths = [[neighbors[i]] for i in neighbors]
                self.poss_paths.append(new_paths)
                for k in self.poss_paths:
                    self.retrace(new_paths[k])#not going to work - but why?
                #add this point,them
                #flag next points --> add to seperate poss-paths lists and check these in other/this function
                #case two, there are two or more paths from here, lets see which is (a. shortest (IFF it goes to init.point) or b. ends first.)
            else:
               path.append(point)
                #case one: there is one neighbor: therefore we continue and add it.
        #HAVE COLLECTED EACH PATH AND VERIFIED THEY GET TO THE DESTINATION. If not, destroy.
        #have COLLECTED ALL PATHS AND CHOOSE THE SHORTEST THAT WORKS.
        #use poss_path --> b_path
        #b_path --> path
        return path



    def do(self):
        if pyxel.frame_count % 60 == 0 and self.scanned:
            self.init()

    def draw(self):
        pyxel.cls(0)

        pyxel.blt(0, 0, 0, 0, 0, self.size, self.size, 0)
        if not self.scanned:
            self.scan_walls([7])

        # explored cells
        for y in range(self.size):
            for x in range(self.size):
                if self.grid[y][x] < 999999:
                    pyxel.pset(x, y, 5)

        # start / end
        pyxel.pset(self.oX, self.oY, 8)
        pyxel.pset(self.fX, self.fY, 11)


Findpath(32)