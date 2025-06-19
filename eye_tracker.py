import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

LEFT_TOP = 159
LEFT_BOTTOM = 145
RIGHT_TOP = 386
RIGHT_BOTTOM = 374

def get_landmarks(image_rgb):
    results = face_mesh.process(image_rgb)
    return results.multi_face_landmarks

def eye_aspect_ratio(landmarks, top_idx, bottom_idx):
    top = landmarks[top_idx]
    bottom = landmarks[bottom_idx]
    return abs(top.y - bottom.y)

def detect_blinks(landmarks, threshold=0.018):
    left_ear = eye_aspect_ratio(landmarks, LEFT_TOP, LEFT_BOTTOM)
    right_ear = eye_aspect_ratio(landmarks, RIGHT_TOP, RIGHT_BOTTOM)

    left_closed = left_ear < threshold
    right_closed = right_ear < threshold

    return left_closed, right_closed
