import cv2
import mediapipe as mp
import pyautogui

capture = cv2.VideoCapture(0)
hands_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
y_index = 0

while True:
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hands_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for fingers in hands:
            drawing_utils.draw_landmarks(frame, fingers)
            landmarks = fingers.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    x_index = screen_width/frame_width*x
                    y_index = screen_height/frame_height*y
                    pyautogui.moveTo(x_index, y_index)

                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(y_index - thumb_y))

                    if abs(y_index - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)