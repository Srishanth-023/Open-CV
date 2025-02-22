import cv2

alg = "E:\\Open CV\\haarcascade_frontalface_default.xml"
haar_cascade_face = cv2.CascadeClassifier(alg)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret: break

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = haar_cascade_face.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 1)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('FD', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()