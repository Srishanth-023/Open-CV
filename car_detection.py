import cv2
import numpy as np

alg = "E:\\Open CV\\haarcascade_car.xml"
haar_cascade_cars = cv2.CascadeClassifier(alg)

if haar_cascade_cars.empty():
    print("Error: Could not load Haar Cascade classifier.")
    exit()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret: break

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BAYER_BGGR2GRAY) 
    cars = haar_cascade_cars.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 4)

    for x, y, w, h in cars:
        cv2.rectangle(gray_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('CARS', gray_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()