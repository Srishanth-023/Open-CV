import cv2
import face_recognition
import os
import numpy as np
import mediapipe as mp
import torch
from torchvision import transforms
from PIL import Image

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False, 
    max_num_faces=100,  
    refine_landmarks=True,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)

REFERENCE_DIR = "reference_faces"
known_face_encodings = []
known_face_names = []

for filename in os.listdir(REFERENCE_DIR):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        person_name = os.path.splitext(filename)[0]
        img_path = os.path.join(REFERENCE_DIR, filename)
        try:
            image = face_recognition.load_image_file(img_path)
            encoding = face_recognition.face_encodings(image, model="hog", num_jitters=1)  # Faster
            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_names.append(person_name)
        except Exception:
            pass

if not known_face_encodings:
    exit()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame, model="hog")  # Switched to hog for speed
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations, num_jitters=1)  # Faster

    results = face_mesh.process(rgb_frame)  # Use pre-initialized face mesh

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.4)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances) if len(face_distances) > 0 else -1
        name = "Unmatched"

        if best_match_index != -1 and matches[best_match_index]:
            name = known_face_names[best_match_index]

        color = (0, 255, 0) if name != "Unmatched" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Optimized Multi-Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
