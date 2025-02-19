import cv2
from utils import limits
from PIL import Image

wc = cv2.VideoCapture(0)
wc.set(cv2.CAP_PROP_AUTO_WB, 0)

bgr = [0, 0, 0]

while True:
    
    ret, frame = wc.read()

    if not ret:
        cv2.waitKey(1)
        continue
    
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = limits(color = bgr)

    mask = cv2.inRange(hsv_img, lower_limit, upper_limit)

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('COLOR DETECTION', frame)
    # cv2.imshow('MASK', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

wc.release()
cv2.destroyAllWindows()