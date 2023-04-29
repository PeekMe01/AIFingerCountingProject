import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) # this is for our video object

mpHands = mp.solutions.hands
hands = mpHands.Hands(False,2,1,0.5,0.5)
mpDraw = mp.solutions.drawing_utils # this will draw the points and lines on the hands

pTime = 0
cTime = 0

while True:
    success, img = cap.read() # this will give us the frame
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # get the image to RGB
    results = hands.process(imgRGB) # this will proccess the frame and give us the results
    #print(results.multi_hand_landmarks)

    # lets extract the info from the results
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape # height width and channel of our image
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx,cy)
                cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # this is for a single hand

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #display frames on GUI
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)