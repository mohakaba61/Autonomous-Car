from picarx import Picarx
import time
import random
import numpy as np
import heapq
import math
from time import sleep

RADIUS = 5
class AdvancedMapping:
    def __init__(self, px, grid):
        self.px = px
        self.grid = grid

    def is_valid(self, x, y):
        """Check if the position is within grid and not an obstacle"""
        if 0 <= x < self.grid.shape[1] and 0 <= y < self.grid.shape[0] and self.grid[int(y)][int(x)] == 0:
            return True
        return False

# Suppose angle 0 is in the direction the robot started
    def scan_enviornment(self, start):
        """
        Given start (x, y, theta) record where all objects are
        Updates the grid matrix to show where the objects are.
        """
        start_x, start_y, start_angle = start ## Step 1 moe servo to -30

        ## Step 2 for every 5 degrees get reading
        for angle in range (-30, 31, 10):
            self.px.set_cam_pan_angle(angle)
            distance = round(self.px.ultrasonic.read(), 2)
            delta_y = distance * np.sin(angle)
            delta_x = distance * np.cos(angle)

            reading_x = start_x
            reading_y = start_y

            if (90 < angle < 270):
                reading_x -= delta_x
            else:
                reading_x += delta_x

            if (0 < angle < 180):
                reading_y -= delta_y
            else:
                reading_y += delta_y
            if (self.is_valid(reading_y, reading_x)):
                self.mark_radius(reading_x, reading_y)
            sleep(0.5)
        # sleep(1)

    def mark_radius(self, y, x):
        x = int(x)
        y = int(y)
        self.grid[x][y] = 1
        for i in range(x - 2* RADIUS, x):
            for j in range(y, y+2 * RADIUS):
                if self.is_valid(i, j):
                    self.grid[i][j] = 1


# Keep track of stack of movements done, we can then go back from by doing reverse.

