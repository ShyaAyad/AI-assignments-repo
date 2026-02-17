# pip install mediapipe opencv-python numpy (Install this in the terminal first)

import cv2
import mediapipe as mp
import json
import time

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

prev_landmarks = None
movement_threshold = 0.03
last_movement_time = 0
still_time_required = 0.5

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

        # default hand movements 
        hand_moving = True 
        hand_still = False
        
        if prev_landmarks is not None:
            total_movement = 0
            for i in range(21):
                dx = landmarks_list[i]["x"] - prev_landmarks[i]["x"]
                dy = landmarks_list[i]["y"] - prev_landmarks[i]["y"]
                dz = landmarks_list[i]["z"] - prev_landmarks[i]["z"]
                
                dist = (dx**2 + dy**2 + dz**2)**0.5             
                if dist < 0.002:  # ignore micro jitter
                    dist = 0
                total_movement += dist
            hand_moving = total_movement >= movement_threshold
            
            # detect if hand is moving or not
            current_time = time.time()
            if hand_moving:
                last_movement_time = current_time
                hand_still = False
            else:
                if current_time - last_movement_time >= still_time_required:
                    hand_still = True
                else:
                    hand_still = False

        prev_landmarks = landmarks_list
        # Send json format response for the next agent that detects the signs 
        send_data({
            "hand_detected": True,
            "landmarks": landmarks_list,
            "hand_moving": hand_moving,
            "hand_still": hand_still
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
