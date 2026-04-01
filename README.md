# 🚗 SafelyDriven — AI Driver Drowsiness Detection System

A real-time AI-powered driver safety system that detects drowsiness, blink rate, yawning, and head pose — with SOS SMS alerts and a live analytics dashboard.

## ✨ Features

- 👁️ **Drowsiness Detection** — Monitors Eye Aspect Ratio (EAR) in real-time
- 😮 **Yawn Detection** — Detects yawning using mouth aspect ratio
- 🧠 **Head Pose Estimation** — Tracks head tilt and nodding
- 🔔 **Audio Alarm** — Plays an alert sound when drowsiness is detected
- 📱 **SOS SMS** — Sends emergency SMS via Twilio after 10s of drowsy state
- 📊 **Live Analytics Dashboard** — Real-time charts with Chart.js
- 🗺️ **Emergency Map** — Interactive Leaflet.js map for incident location
- 🎞️ **Black Box History** — Session snapshot gallery for post-event analysis
- 🛡️ **Face Liveness Check** — Anti-spoofing using head movement detection

## 🛠️ Tech Stack

- **Backend:** Python, OpenCV, dlib, Flask/WebSocket
- **Frontend:** HTML, CSS, JavaScript (Chart.js, Leaflet.js)
- **SMS:** Twilio API
- **Face Detection:** dlib 68-point facial landmarks

## 📦 Setup

### 1. Clone the repository
```bash
git clone https://github.com/ARYAN2307A/MDP.git
cd MDP
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install opencv-python dlib flask flask-socketio twilio numpy scipy
```

### 4. Download the AI Model / Dataset (Required)
The Dlib facial landmark model is too large for GitHub (100MB) and is required to run the code. 
*(Note: This pre-trained model was originally trained on the **iBUG 300-W face landmark dataset**).*

1. Download the compressed model here: **[shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)**
2. Extract the `.bz2` archive to get the `.dat` file.
3. Place the extracted `shape_predictor_68_face_landmarks.dat` file directly in your main project folder.

### 5. Set up environment variables
Create a `.env` file in the root directory:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1xxxxxxxxxx
EMERGENCY_CONTACT=+91xxxxxxxxxx
```

### 6. Run the application
```bash
python detector.py
```

Then open `http://localhost:5000` in your browser.

## ⚠️ Notes

- The `shape_predictor_68_face_landmarks.dat` file (~99MB) is **not** included in the repo. Download it separately.
- Never commit your `.env` file — it contains API secrets.
- Requires a webcam for real-time detection.

## 📸 Dashboard Preview

> Real-time drowsiness monitoring with live analytics, emergency map, and session history.

## Final Product Presentation

[AI-Powered-Driver-Drowsiness-Detection-System.pptx](https://github.com/user-attachments/files/26393826/AI-Powered-Driver-Drowsiness-Detection-System.pptx)

## Project Report

[REPORT.docx](https://github.com/user-attachments/files/26394145/REPORT.docx)

