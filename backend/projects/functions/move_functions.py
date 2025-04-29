from picarx import Picarx
import time
import math

class PicarMovement:
    
    def __init__(self, px):
        self.px = px
    
    def move_forward(self, x):
        time.sleep(0.1)
        self.px.forward(10)
        curr = self.px.ultrasonic.read()
        next = None
        while not next or curr - next < x:
            next = self.px.ultrasonic.read()
        
        self.px.forward(0)
    
    def move_backward(self, x):
    
        time.sleep(0.1)
    
        self.px.backward(10)
    
        curr = self.px.ultrasonic.read()
        next = None
    
        while not next or next - curr < x:
            next = self.px.ultrasonic.read()
        
        self.px.backward(0)

    def turn(self, angle, speed=30):
        """Turn the car by a given angle in degrees."""
        omega = (2 * speed) / 2.25  # deg / sec

        turn_time = abs(angle) / omega # T = theta / w 
        self.px.set_dir_servo_angle(angle)
        self.px.forward(speed)

        time.sleep(turn_time)  # Wait for turn to complete
        
        self.px.stop()  # Stop motors    
    
    def move(self, start, steps, speed = 10):
        if (speed == 0): return start

        l1 = steps[-1][1] - start[1] # y-axis
        l2 = steps[-1][0] - start[0] # x-axis

        distance = (l1 ** 2 + l2 ** 2) ** 0.5

        angle_rad = math.atan2(l1, l2) #theta = arctan(delta y / delta x)
        angle_deg = math.degrees(angle_rad) # radians to degres
        new_angle = angle_deg

        cur_angle = start[2]
        diff_angle = new_angle - cur_angle

        if (diff_angle > 180):
            diff_angle -= 360
        if (diff_angle != 0):
            self.turn(diff_angle)
            self.px.set_dir_servo_angle(0)

        else:
            self.move_forward(distance)
        return (steps[-1][0], steps[-1][1], new_angle) 
    













    # def backward(self, x):
    #     self.px.backward(10)
    #     time.sleep(x)
    #     self.px.backward(0)
    
    # def turn_left(self):
    #     self.backward(0.5)
    #     self.px.set_dir_servo_angle(-45)
    #     for _ in range(7):
    #         self.forward(0.48)
    #         self.px.set_dir_servo_angle(0)
    #         self.backward(0.32)
    #         self.px.set_dir_servo_angle(-45)
    #     self.px.set_dir_servo_angle(0)
    #     self.backward(0.5)
    
    # def turn_right(self):
    #     backward(0.5)
    #     self.px.set_dir_servo_angle(45)
    #     for _ in range(7):
    #         self.forward(0.48)
    #         self.px.set_dir_servo_angle(0)
    #         self.backward(0.32)
    #     self.px.set_dir_servo_angle(45)
    #     self.px.set_dir_servo_angle(0)
    #     self.backward(0.5)

        # def run_steps(self, steps):
        # for ins, arg in steps:
        #     if ins == "f":
        #         self.move_forward(arg)
        #     elif ins == "b":
        #          self.move_backward(arg)
        #     elif ins == "l":
        #         self.turn_left()
        #     elif ins == "r":
        #         self.turn_right()
        #     else:
        #         raise "Invalid Instruction passed to run_steps()"

    
    # def move_backward(self, x):
    
    #     time.sleep(0.5)
    
    #     self.px.backward(10)
    
    #     curr = self.px.ultrasonic.read()
    #     next = None
    
    #     while not next or next - curr < x:
    #         next = self.px.ultrasonic.read()
        
    #     self.px.backward(0)