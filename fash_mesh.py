import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(
    max_num_faces = 3,
    refine_landmarks = True,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5 ) as face_mesh:

    while cap.isOpened():
        success, image = cap.read()

        if not success:
            print('Exiting...')
            continue  

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                # BORDER AROUND FACE, EYES AND LIPS

                mp.solutions.drawing_utils.draw_landmarks(
                    image = image,
                    landmark_list = face_landmarks,
                    connections = mp.solutions.face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles
                    .get_default_face_mesh_contours_style()
                )


                # IRIS

                mp.solutions.drawing_utils.draw_landmarks(
                    image = image,
                    landmark_list = face_landmarks,
                    connections = mp.solutions.face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles
                    .get_default_face_mesh_iris_connections_style()
                )            
                
                # LANDMARKS

                mp.solutions.drawing_utils.draw_landmarks(
                    image = image,
                    landmark_list = face_landmarks,
                    connections = mp.solutions.face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles
                    .get_default_face_mesh_tesselation_style()
                )
                                

        cv2.imshow('FACE MESH', cv2.flip(image, 1))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

