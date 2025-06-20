import cv2
from camera_module import get_camera_frame
from buzzer_alert import trigger_alert
from tracker import track_child
import json

SAFE_ZONE = {}

with open("config.json", "r") as f:
    SAFE_ZONE = json.load(f)["safe_zone"]

def detect_harmful_item(frame):
    # Dummy logic for now
    # TODO: Load TFLite model and replace this
    return False  # Always false unless integrated with real model

cap = cv2.VideoCapture(0)

while True:
    ret, frame = get_camera_frame(cap)
    if not ret:
        break

    child_position = track_child(frame)

    if child_position:
        x, y = child_position
        x0, y0, w, h = SAFE_ZONE.values()
        if not (x0 <= x <= x0 + w and y0 <= y <= y0 + h):
            print("Child out of safe zone!")
            trigger_alert("position")

        if detect_harmful_item(frame):
            print("Harmful object detected!")
            trigger_alert("object")

    cv2.imshow("Smart Monitor Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
