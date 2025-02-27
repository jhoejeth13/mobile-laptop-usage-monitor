import cv2
import mediapipe as mp

# Initialize MediaPipe Hand Detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB (for MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Detect hands in the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract key points
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            palm_base = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            # Compute distances
            thumb_index_dist = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5
            thumb_middle_dist = ((thumb_tip.x - middle_tip.x) ** 2 + (thumb_tip.y - middle_tip.y) ** 2) ** 0.5
            palm_size = ((palm_base.x - middle_tip.x) ** 2 + (palm_base.y - middle_tip.y) ** 2) ** 0.5

            # Condition for detecting a phone/laptop in hand
            if thumb_index_dist < 0.04 and thumb_middle_dist < 0.04 and palm_size > 0.1:
                cv2.putText(frame, "PHONE/LAPTOP DETECTED!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Show the video feed
    cv2.imshow("Classroom Monitor", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
