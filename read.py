import cv2 as cv


# READING IMAGES AND VIDEOS

# Reading Images

img = cv.imread('Photos/Lion.jpg')

cv.imshow('LION', img)

cv.waitKey(0)
    
# Reading Videos

capture = cv.VideoCapture('Videos/Kitten.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('KITTEN', frame)

    if cv.waitKey(20) & 0xFF == ord('a'):
        break

capture.release()
cv.destroyAllWindows
