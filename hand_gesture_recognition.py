from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)

detector = HandDetector(
    detectionCon=0.8,
    maxHands=1
)

while True:

    success, img = cap.read()

    if not success:
        break

    hands, img = detector.findHands(img)

    if hands:

        hand = hands[0]

        fingers = detector.fingersUp(hand)

        totalFingers = fingers.count(1)

        gesture = ""

        if totalFingers == 0:
            gesture = "Fist"

        elif totalFingers == 1:
            gesture = "One Finger"

        elif totalFingers == 2:
            gesture = "Two Fingers"

        elif totalFingers == 3:
            gesture = "Three Fingers"

        elif totalFingers == 4:
            gesture = "Four Fingers"

        elif totalFingers == 5:
            gesture = "Open Palm"

        cv2.putText(
            img,
            f"Gesture: {gesture}",
            (20, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Hand Gesture Recognition", img)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()