import cv2
import os

capture = cv2.VideoCapture("8.mp4")
i = 0
directory = './crashedCars'
os.chdir(directory)
while True:
    ret, frame = capture.read()
    cv2.imwrite("frame8_%d.jpg" % i, frame)
    i = i + 1