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
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
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

### 4. Download the facial landmark model
Download `shape_predictor_68_face_landmarks.dat` from:
> https://github.com/davisking/dlib-models

Place it in the project root directory.

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


