import cv2 as cv

# RESIZING IMAGES AND VIDEOS

img = cv.imread('Photos/Lion.jpg')
cv.imshow('Original Image', img)

def rescaleFrame(frame, scale = 0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Resized Image', resized_image)

capture = cv.VideoCapture('Videos/Kitten.mp4')

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    frame_resized = rescaleFrame(frame, scale = 2)

    cv.imshow('Video', frame)
    cv.imshow('Rescaled Video', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('a'):
        break

capture.release()
cv.destroyAllWindows
