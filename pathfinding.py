"""Actual pathfinding prototype to implement for later"""
import pyxel, random, math

class Findpath:
    def __init__(self, oX, oY, fX, fY, size):
        self.oX = oX
        self.oY = oY
        self.fX = fX
        self.fY = fY
        self.size = size
        # Initialize grid with large values (not lists!)
        self.grid = [[999999 for _ in range(self.size)] for _ in range(self.size)]
        self.found_path = False
        self.queue = [(oX, oY, 0)]  # Use a queue for BFS instead of recursion
        pyxel.init(self.size, self.size, title="Path finding bot", display_scale=1)
        pyxel.run(self.update, self.draw)

    def spread_step(self):
        """Process one step of pathfinding per frame"""
        if not self.queue or self.found_path:
            return

        # Process a batch of points per frame
        for _ in range(100):  # Process 100 points per frame for speed
            if not self.queue:
                break

            x, y, dist = self.queue.pop(0)

            # Skip if out of bounds
            if not (0 <= x < self.size and 0 <= y < self.size):
                continue

            # Skip if we've already found a better path to this cell
            if self.grid[x][y] <= dist:
                continue

            # Update this cell
            self.grid[x][y] = dist

            # Check if we reached the target
            if x == self.fX and y == self.fY:
                self.found_path = True
                return

            # Add neighbors to queue
            angle = math.atan2((self.fX - x),(self.fY - y)) * 180* math.pig
            temp = []
            while len(temp)<4:
                r = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)])
                if r not in temp: temp.append(r)
            for dx, dy in temp:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if self.grid[nx][ny] > dist + 1:
                        self.queue.append((nx, ny, dist + 1))

    def update(self):
        self.spread_step()

    def draw(self):
        pyxel.cls(0)
        for x in range(0, self.size, 1):  # Sample every 2 pixels for performance
            for y in range(0, self.size, 1):
                val = self.grid[x][y]
                if val < 999999:
                    # Map distance to color (0-15 for pyxel colors)
                    color = min(15, val % 16)
                    pyxel.pset(y, x, color)





        # Draw start and end points
        pyxel.circ(self.oY, self.oX, 1, 8)  # Start in red
        pyxel.circ(self.fY, self.fX, 1, 11)  # End in green

size = 500
Findpath(random.randint(0,size), random.randint(0,size), random.randint(0,size), random.randint(0,size),size)