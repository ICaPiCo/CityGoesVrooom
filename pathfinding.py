import pyxel, random, math
import heapq


class Findpath:
    def __init__(self, size):
        self.size = size
        self.walls = []
        self.oX = 0
        self.oY = 0
        self.fX = 0
        self.fY = 0
        self.scanned = False
        self.grid = [[999999 for _ in range(self.size)] for _ in range(self.size)]
        self.found_path = False

        pyxel.init(self.size, self.size, title="Path finding bot")
        pyxel.load("my_resource.pyxres")
        # Initialize queue after scanning walls
        self.queue = []

        pyxel.run(self.update, self.draw)

    def scan_walls(self, colors):
        if not self.scanned:
            for i in range(self.size):
                for j in range(self.size):
                    if pyxel.pget(i, j) in colors:
                        self.walls.append((i, j))  # Use tuples for consistency

            # Convert to set for O(1) lookup
            self.walls = set(self.walls)

            # Generate valid start and end positions
            while True:
                self.oX = random.randint(0, self.size - 1)
                self.oY = random.randint(0, self.size - 1)
                self.fX = random.randint(0, self.size - 1)
                self.fY = random.randint(0, self.size - 1)

                if ((self.oX, self.oY) not in self.walls and
                        (self.fX, self.fY) not in self.walls and
                        not (self.oX == self.fX and self.oY == self.fY)):
                    break

            # Initialize queue with starting position
            heapq.heappush(self.queue, (0, self.oX, self.oY, 0))
            self.scanned = True

    def spread_step(self):
        """Process one step of pathfinding per frame"""
        if not self.queue or self.found_path:
            return

        for _ in range(100):
            if not self.queue:
                break

            priority, x, y, dist = heapq.heappop(self.queue)

            if not (0 <= x < self.size and 0 <= y < self.size):
                continue

            # Skip if this is a wall
            if (x, y) in self.walls:
                continue

            if self.grid[x][y] <= dist:
                continue

            self.grid[x][y] = dist

            if x == self.fX and y == self.fY:
                self.found_path = True
                return

            # Add neighbors
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if (nx, ny) not in self.walls and self.grid[nx][ny] > dist + 1:
                        priority = (nx - self.fX) ** 2 + (ny - self.fY) ** 2
                        heapq.heappush(self.queue, (priority, nx, ny, dist + 1))

    def update(self):
        if not self.scanned:
            self.scan_walls([7])
        self.spread_step()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 16, 16, 0)

        # Draw explored cells
        for x in range(self.size):
            for y in range(self.size):
                val = self.grid[x][y]
                if val < 999999:
                    pyxel.pset(x, y, 5)  # Fixed: use (x, y) not (y, x)

        # Draw start and end points
        pyxel.pset(self.oX, self.oY, 8)
        pyxel.pset(self.fX, self.fY, 11)


Findpath(16)