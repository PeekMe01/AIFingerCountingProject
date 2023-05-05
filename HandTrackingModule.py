import cv2
import mediapipe as mp


class handDetector():

    def __init__(self, mode=False, maxHands = 2, detectionConfidence = 0.5, trackConfidence = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, 1, self.detectionConfidence, self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils  # this will draw the points and lines on the hands

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # get the image to RGB
        self.results = self.hands.process(imgRGB)  # this will proccess the frame and give us the results

        # lets extract the info from the results
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)  # this is for a single hand
        return img

    def findPositions(self, img, handNos=[0, 1], draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            for handIndex, handNo in enumerate(handNos):
                #len of hand landmarks returns number of hands detected so if 1 hand if case does handNo 0 only if 2 hands it does 0 and 1
                if handNo < len(self.results.multi_hand_landmarks):
                    myHand = self.results.multi_hand_landmarks[handNo]
                    for id, lm in enumerate(myHand.landmark):
                        h, w, c = img.shape  # height width and channel of our image
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                        if draw:
                            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList
