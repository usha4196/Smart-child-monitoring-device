# Smart-child-monitoring-device
AI -powered child monitoring using Raspberry Pi
# Smart Child Monitoring Device 👶📹

AI-powered child monitoring system using **OpenCV** and optionally **Raspberry Pi**, designed for **indoor safety** and **harm detection**. It helps monitor a child's presence within a defined safe zone and alerts if the child moves out or harmful objects are detected.

---

## 🚀 Features

- 📸 Real-time video feed via webcam or Raspberry Pi camera
- 👶 Face detection to track child position
- 🛑 Safe zone alert system
- 🚨 Buzzer alert (simulated on PC / real on Raspberry Pi)
- ⚠️ Placeholder logic for harmful object detection (can integrate TFLite model)

---

## 🖥️ Technologies Used

- Python 3.13
- OpenCV (cv2)
- JSON for configuration
- GPIO (only when run on Raspberry Pi)

---

## 🔧 Setup Instructions

### ✅ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
