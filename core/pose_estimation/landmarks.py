import cv2
import numpy as np
import mediapipe as mp

# initialise mediapipe pose and drawing
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

# to capture video
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("error")
        break

    # detect landmarks
    with mp_pose.Pose(
        static_image_mode=True, min_detection_confidence=0.5, model_complexity=2
    ) as pose:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)
        # draw landmarks
        if results.pose_landmarks:
            mp_draw.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
            )

    #cv2.imshow("Pose", rgb_frame)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
