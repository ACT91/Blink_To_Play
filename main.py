import cv2
from eye_tracker import get_landmarks, detect_blinks
from media_keys import play_pause, next_track, prev_track, seek_forward, seek_backward
from utils import BlinkTimer

def main():
    cap = cv2.VideoCapture(0)
    left_timer = BlinkTimer()
    right_timer = BlinkTimer()
    last_action_time = 0
    cooldown = 1  # seconds between actions

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = get_landmarks(rgb)

        if faces:
            landmarks = faces[0].landmark
            left_closed, right_closed = detect_blinks(landmarks)

            left_timer.update(left_closed)
            right_timer.update(right_closed)

            now = time.time()

            # Detect both eyes closed (play/pause)
            if left_closed and right_closed:
                if now - last_action_time > cooldown:
                    play_pause()
                    print("Play/Pause")
                    last_action_time = now

            # Single-eye blinks
            elif left_closed and not right_closed:
                if now - last_action_time > cooldown:
                    prev_track()
                    print("Previous Track")
                    last_action_time = now

            elif right_closed and not left_closed:
                if now - last_action_time > cooldown:
                    next_track()
                    print("Next Track")
                    last_action_time = now

            # Long blinks
            if left_timer.is_long_blink():
                seek_backward()
                print("Seeking Backward")

            if right_timer.is_long_blink():
                seek_forward()
                print("Seeking Forward")

        cv2.imshow("Blink Music Controller", frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import time
    main()
# This code is a simple blink-based music controller using OpenCV and media keys.
# It captures video from the webcam, detects blinks using facial landmarks,