import cv2
import time
from picamera2 import Picamera2

from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import projects.object_detection_helpers.utils as utils

import threading
import sys

model = "./efficientdet_lite0.tflite"
num_threads = 4

picam2 = Picamera2()
picam2.start()

base_options = core.BaseOptions(file_name=model, use_coral=False, num_threads=num_threads)
detection_options = processor.DetectionOptions(max_results=8, score_threshold=0.5)
options = vision.ObjectDetectorOptions(base_options=base_options, detection_options=detection_options)
detector = vision.ObjectDetector.create_from_options(options)

def detect():
    
    im = picam2.capture_array()
    imRGB = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    imTensor = vision.TensorImage.create_from_array(imRGB)
    detections = detector.detect(imTensor)
    
    return list(set([detection.categories[0].category_name for detection in detections.detections]))