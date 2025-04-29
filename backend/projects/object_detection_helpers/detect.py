import cv2
import time
from picamera2 import Picamera2

from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import projects.object_detection_helpers.utils as utils

import threading
import sys

model = "projects/object_detection_helpers/efficientdet_lite0.tflite"
num_threads = 4

dispW = 1280
dispH = 720

picam2 = Picamera2()
picam2.preview_configuration.main.size = (dispW, dispH)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

pos = (20, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1.5
weight = 3
myColor = (255,0,0)

base_options = core.BaseOptions(file_name=model, use_coral=False, num_threads=num_threads)
detection_options = processor.DetectionOptions(max_results=8, score_threshold=0.3)
options = vision.ObjectDetectorOptions(base_options=base_options, detection_options=detection_options)
detector = vision.ObjectDetector.create_from_options(options)

def detect(detected: list, mutex: threading.Lock):
    
    fps = 0

    tStart = time.time()

    while True:
        im = picam2.capture_array()
        imRGB = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        imTensor = vision.TensorImage.create_from_array(imRGB)
        detections = detector.detect(imTensor)
        image = utils.visualize(im, detections, detected, mutex)
        cv2.putText(im, str(int(fps)) + "FPS", pos, font, height, myColor, weight)
        # cv2.imshow("Camera", im)
        
        if cv2.waitKey(1) == ord("q"):
            break
        tEnd = time.time()
        
        loopTime = tEnd - tStart
        fps = 0.9 * fps + 0.1 * 1 / loopTime
        
        tStart = time.time()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    print("HERE")
    detect([0, 0], threading.Lock())