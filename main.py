import math
from random import random
import cv2

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)
key = cv2.waitKey(1)

while True:
    sucessful_frame_read, frame = webcam.read() 

    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (random()*255, random()*255, random()*255), 2)
     
    cv2.imshow('Clever Programmer Face Detector', frame)
    
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break
