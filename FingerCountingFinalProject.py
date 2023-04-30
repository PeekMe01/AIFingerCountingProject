import cv2
import time
import os # for storing images
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    #print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionConfidence=0.90)

#first hand markers are from 0 to 20, second hand from 21 to 41
tipIds = [4, 8, 12, 16, 20]
secound_hand_ids = [20 + 5, 20 + 9, 20 + 13, 20 + 17, 20 + 21] # 25, 29, 33, 37, 41

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPositions(img, draw=False)
    print(len(lmList))

    if len(lmList) != 0:
        fingers = []

        if lmList[tipIds[2]][1] > lmList[tipIds[4]][1]:
            # for the thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            # for the fingers
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        
        else:
            # for the thumb
            if lmList[tipIds[0]][1] < lmList[tipIds[0] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            # for the fingers
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        
        if len(lmList) > 21:
            
            if lmList[secound_hand_ids[2]][1] > lmList[secound_hand_ids[4]][1]:
                # for the thumb
                if lmList[secound_hand_ids[0]][1] > lmList[secound_hand_ids[0] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                # for the fingers
                for id in range(1,5):
                    if lmList[secound_hand_ids[id]][2] < lmList[secound_hand_ids[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
        
            else:
                # for the thumb
                if lmList[secound_hand_ids[0]][1] < lmList[secound_hand_ids[0] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                # for the fingers
                for id in range(1,5):
                    if lmList[secound_hand_ids[id]][2] < lmList[secound_hand_ids[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                


        totalFingers = fingers.count(1) # to find how many "1"'s there is
            

        #odfhoubo
        h, w, c = overlayList[0].shape
        #img[0:h,0:w]=overlayList[totalFingers-1]

        #cv2.rectangle(img, (20,255), (170,425), (0,255,0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45,375), cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)