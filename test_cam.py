import cv2
import dlib
import imutils
from imutils import face_utils

print("Loading dlib detector...")
detect = dlib.get_frontal_face_detector()
print("Loading dlib predictor...")
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

print("Opening camera...")
cap = cv2.VideoCapture(1) # Try 1 first as in detector.py
ret, frame = cap.read()

if not ret:
    print("Camera 1 failed, trying Camera 0...")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

if ret:
    print("Camera success!")
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detect(gray, 0)
    print(f"Detected {len(rects)} faces.")
    for rect in rects:
        shape = predict(gray, rect)
        print("Landmarks predictor success!")
else:
    print("Camera failed completely.")

cap.release()
print("Test complete.")
