from picarx import Picarx
import time
import random
import numpy as np
import heapq
import math
from time import sleep

MOTION_PRIMITIVES = [
    (1, 0, 0),    # Forward
    (-1, 0, 0),   # Forward Right
    (0, 1, 0),   # Forward Left
    (0, -1, 0),   # Reverse
]
class AStarSearch():
    def __init__ (self, start, goal, grid_ref):
        self.cur_location = start
        self.goal = goal
        self.grid = grid_ref

        self.to_visit = []
        self.visited = set()
        heapq.heappush(self.to_visit, (0, self.cur_location))


    def is_valid(self, x, y):
        """Check if the position is within grid and not an obstacle"""
        if 0 <= y < self.grid.shape[0] and 0 <= x < self.grid.shape[1] and self.grid[int(y)][int(x)] == 0:
            return True
        return False

    def heuristic(self, node, goal):
        """We use the distance to the goal as the heuristic"""
        return math.sqrt((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2)


    def get_next_steps(self, num_steps = 10):
        print()
        steps = []

        while self.to_visit:
            cost, (x, y, theta) = heapq.heappop(self.to_visit)
            if (x, y, theta) in self.visited:
                continue
            if (self.grid[y][x] == 1):
                continue
            self.visited.add((x, y, theta))
            steps.append((x, y, theta))


            ## All direction we can go
            for dx, dy, dtheta in MOTION_PRIMITIVES:
                new_x = x + dx
                new_y = y + dy
                new_theta = (theta + dtheta) % 360
                valid = self.is_valid(new_x, new_y)
                blocked = not self.is_blocked(new_x, new_y, dx, dy)
                visited = (new_x, new_y, new_theta) not in self.visited

                if valid and blocked and visited:
                    heapq.heappush(self.to_visit, (self.heuristic((new_x, new_y), self.goal), (new_x, new_y, new_theta)))

            if (len(steps) == num_steps):
                self.cur_location = steps[-1]
                return steps
        return steps  # No path found

    def is_blocked(self, x_start, y_start, dx, dy, steps = 10):
        """
        returns if starting at start, taking the motion primitive is possible
        or if it will crash.

        It will basiclly move in the x direction then in the y direction making sure
        there are no points between them
        """


        for i in range(steps + 1):
            alpha = i / steps
            x_interp = x_start + alpha * dx
            y_interp = y_start + alpha * dy
            # theta_interp = (theta_start + alpha * dtheta) % 360  # if needed

            gx = int(round(x_interp))
            gy = int(round(y_interp))

            if not self.is_valid(gx, gy):
                return True  # Out of bounds => blocked

            if self.grid[gy, gx] == 1:
                return True
                
    def update_location(self, new_loc):
        self.cur_location = new_loc