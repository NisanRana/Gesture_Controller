import sys
import os
import cv2
from collections import deque

# ----------------------------
# FIX IMPORT PATHS
# ----------------------------
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from detector import predict
from controls import execute
from utils.cooldown import allowed
from config import CONFIDENCE, COOLDOWN

print("🔥 Gesture Controller Started")

# ----------------------------
# CAMERA
# ----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not opening")
    exit()

# ----------------------------
# SMOOTHING STATE
# ----------------------------
gesture_buffer = deque(maxlen=5)
stable_gesture = None

# ----------------------------
# MAIN LOOP
# ----------------------------
while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Frame error")
        break

    # ----------------------------
    # PREDICTION (Roboflow)
    # ----------------------------
    gesture, conf = predict(frame)

    # ----------------------------
    # DEBUG
    # ----------------------------
    if gesture:
        print(f"Detected: {gesture} {conf:.2f}")

    # ----------------------------
    # SMOOTHING LOGIC
    # ----------------------------
    if gesture and conf >= CONFIDENCE:
        gesture_buffer.append(gesture)

        if len(gesture_buffer) == gesture_buffer.maxlen:
            most_common = max(set(gesture_buffer), key=gesture_buffer.count)

            if most_common != stable_gesture:
                stable_gesture = most_common

                if allowed(COOLDOWN):
                    execute(stable_gesture)

    else:
        gesture_buffer.clear()

    # ----------------------------
    # DISPLAY
    # ----------------------------
    cv2.imshow("Gesture Controller", frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

# ----------------------------
# CLEAN EXIT
# ----------------------------
cap.release()
cv2.destroyAllWindows()