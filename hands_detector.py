# pip install mediapipe opencv-python numpy (Install this in the terminal first)

import cv2
import mediapipe as mp
import json

# MediaPipe Setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Communication file with the next agent
OUTPUT_FILE = "hand_data.txt"

# Send data to next agent
def send_data(data):
    with open(OUTPUT_FILE, "w") as f:
        f.write(json.dumps(data))

# Camera Setup
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cv2.namedWindow("Vision Agent", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Vision Agent", 1000, 700)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    # If hand detected
    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]

        # Draw hand joints
        mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )

        # Extract landmark coordinates
        landmarks_list = []
        for lm in hand_landmarks.landmark:
            landmarks_list.append({
                "x": lm.x,
                "y": lm.y,
                "z": lm.z
            })

        # Send json format response for the next agent that detects the signs 
        send_data({
            "hand_detected": True,
            "landmarks": landmarks_list
        })

    else:
        # Send FALSE if no hand
        send_data({
            "hand_detected": False,
            "landmarks": None
        })

    # Show camera
    cv2.imshow("Vision Agent", frame)

    # Exit if window closed
    if cv2.getWindowProperty("Vision Agent", cv2.WND_PROP_VISIBLE) < 1:
        break

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
