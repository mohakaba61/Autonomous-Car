import sys
import threading
from time import sleep
import numpy as np
from picarx import Picarx

from functions.move_functions import PicarMovement# forward, turn
from advanced_mapping import AdvancedMapping #scan_enviornment, is_valid
from pathfinding import AStarSearch
from object_detection_helpers.detect import detect


objects_detected_mutex = threading.Lock()
objects_detected = [0] * 2 # [true, false, true]
START = (0, 50, 0)

def self_drive(goal_x, goal_y):
    px = Picarx()
    px.stop()
    cur_pos = START

    grid = np.zeros((100, 100))
    routing = AStarSearch(START, (goal_x, goal_y), grid)
    mapping = AdvancedMapping(px, grid)
    movement = PicarMovement(px)

    while not (abs(cur_pos[0] - goal_x) < 5 and abs(cur_pos[1] - goal_y) < 5):
        mapping.scan_enviornment(cur_pos)
        steps = routing.get_next_steps(10)
        speed = 10
        with objects_detected_mutex:
            if (objects_detected[0]):
                speed = 5
            if (objects_detected[1]):
                speed = 0        
        cur_pos = movement.move(cur_pos, steps, speed)
        routing.update_location(cur_pos)

    

def main(goal_x, goal_y):
    global objects_detected
    thread = threading.Thread(target=detect, args=(objects_detected, objects_detected_mutex))
    thread.daemon = True
    thread.start()
    self_drive(goal_x, goal_y)

if __name__ == "__main__":
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)    
    name, goal_x, goal_y = sys.argv 
    goal_x = int(goal_x)
    goal_y = int(goal_y)
    
    main(goal_x, goal_y)