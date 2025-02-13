import numpy as np
import cv2

def limits(color):

    c = np.uint8([[color]])
    hsv_C = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # lower_limit = np.array([max(hsv_C[0][0][0] - 15, 0), 20, 20], dtype = np.uint8)
    # upper_limit = np.array([min(hsv_C[0][0][0] + 15, 180), 255, 255], dtype = np.uint8)
    
    lower_limit = np.array([35, 100, 100], dtype=np.uint8)
    upper_limit = np.array([85, 255, 255], dtype=np.uint8)

    print("Lower HSV:", lower_limit)
    print("Upper HSV:", upper_limit)

    return lower_limit, upper_limit