import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # red
    
    low_red = np.array([161,155,54])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red,high_red)
    mask = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    # blue
    
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255]) 
    blue_mask = cv2.inRange(hsv_frame, low_blue,high_blue)
    mask = cv2.bitwise_and(frame, frame, mask=blue_mask)
    
    # green
    low_green = np.array([40, 100, 100])
    high_green = np.array([102,255, 255])
    mask_green = cv2.inRange(hsv_frame, low_green,high_green)
    mask = cv2.bitwise_and(frame, frame, mask=mask_green)
    
    
    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('Frame', frame)
    cv2.imshow('Red',mask)
    cv2.imshow('Blue',mask)
    cv2.imshow('Green',mask)
    cv2.imshow('Result', result)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    