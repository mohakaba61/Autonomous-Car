# from picarx import Picarx
# import time
# import numpy as np
# import math

# px = Picarx()

# WHEEL_BASE = 2.25

# def forward(x):
#     time_to_move = x / 23
#     px.forward(10)
#     time.sleep(time_to_move)
#     px.forward(0)

# def turn(angle, speed=30):
#     """Turn the car by a given angle in degrees."""
#     V_r = speed  # Right wheel speed (cm/sec)
#     V_l = -speed  # Left wheel speed (cm/sec) (for in-place turns)
#     omega = (2 * speed) / WHEEL_BASE  # deg/sec
#     if (angle < 0):
#         angle = max(-90, angle)
#     else:
#         angle = min(90, angle)

#     turn_time = abs(angle) / omega  

#     # px.set_motor_speed(1, V_l)  # Left motor
#     # px.set_motor_speed(2, V_r)  # Right motor
#     px.set_dir_servo_angle(angle)
#     px.forward(speed)

#     time.sleep(turn_time)  # Wait for turn to complete
#     px.stop()  # Stop motors


# def move(start, steps):
#     l1 = steps[-1][0] - start[0]
#     l2 = steps[-1][1] - start[1] 
#     distance = (l1 ** 2 + l2 ** 2) ** 0.5
#     angle_rad = math.atan2(l2, l1)
#     angle_deg = math.degrees(angle_rad)

#     new_angle = (360 - angle_deg) % 360
#     cur_angle = start[2]
#     diff_angle = new_angle - cur_angle
#     if (diff_angle > 180):
#         diff_angle -= 360
#     turn(diff_angle)
#     px.set_dir_servo_angle(0)
#     # print(distance)
#     forward(distance)
#     return (steps[-1][0], steps[-1][1], new_angle)    

# # START = (0, 50, 0)
# # forward(100)


from advanced_mapping import AdvancedMapping
from functions.move_functions import PicarMovement
from pathfinding import AStarSearch
from picarx import Picarx
import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

px = Picarx()
px.forward(0)
exit()
# grid = np.zeros((100, 100))
# start = (0, 50, 0) # x, y, theta


routing = AStarSearch(start, (100, 100), grid)
locations = routing.get_next_steps(num_steps = 1000)
print(locations)
movement = PicarMovement(px)
movement.move(start, locations)


# print(grid)
# print()
# print()
# print()
# mapping = AdvancedMapping(px, grid)
# mapping.scan_enviornment(start)
# print(grid)
