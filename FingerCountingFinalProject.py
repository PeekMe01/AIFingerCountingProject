import cv2
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import HandTrackingModule as htm


wCam, hCam = 640, 480


palm_facing_camera_or_left_hand_not_facing = False

hand_pointing_up = False
hand_pointing_right = False
hand_pointing_down = False
hand_pointing_left = False

diagonal_top_left = False
diagonal_top_right = False
diagonal_bottom_left = False
diagonal_bottom_right = False





def count_hand_pointing(lmList, tipIds, pointing_fingers, two_hands):
    hand_points = []
    temp_pointing_fingers = pointing_fingers
    
    #For rock / paper / scissors
    left_hand_rock = False
    left_hand_paper = False
    left_hand_scissors = False

    right_hand_rock = False
    right_hand_paper = False
    right_hand_scissors = False

    if two_hands:
        hand_points.append(21)
        hand_points.append(22)
        hand_points.append(38)

    else:
        hand_points.append(0)
        hand_points.append(1)
        hand_points.append(17)

    # Palm facing camera or not
    if ((((lmList[hand_points[1]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] > lmList[hand_points[0]][2])) or ((lmList[hand_points[1]][2] > lmList[hand_points[0]][2]))) and ((lmList[hand_points[2]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] > lmList[hand_points[0]][2])) or
            (((lmList[hand_points[1]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] > lmList[0][2])) or ((lmList[hand_points[1]][2] > lmList[hand_points[0]][2]))) and ((lmList[hand_points[2]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] < lmList[hand_points[0]][2])) or
            (((lmList[hand_points[1]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] < lmList[0][2])) or ((lmList[hand_points[1]][2] < lmList[hand_points[0]][2]))) and ((lmList[hand_points[2]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] < lmList[hand_points[0]][2])) or
            (((lmList[hand_points[1]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] < lmList[0][2])) or ((lmList[hand_points[1]][2] < lmList[hand_points[0]][2]))) and ((lmList[hand_points[2]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] > lmList[hand_points[0]][2]))):
        palm_facing_camera_or_left_hand_not_facing = True

    else:
        palm_facing_camera_or_left_hand_not_facing = False

    if palm_facing_camera_or_left_hand_not_facing:
        # print(lmList[1])
        # print(lmList[0])
        # print(lmList[17])
        if ((lmList[hand_points[1]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] < lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] < lmList[hand_points[0]][2])):
            hand_pointing_up = True

        else:
            hand_pointing_up = False

        if ((lmList[hand_points[1]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] > lmList[hand_points[0]][2]) + 20) and ((lmList[hand_points[2]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] < lmList[hand_points[0]][2])):
            hand_pointing_right = True
            hand_pointing_up = False

        else:
            hand_pointing_right = False

        if ((lmList[hand_points[1]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] > lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] > lmList[hand_points[0]][2])):
            hand_pointing_down = True

        else:
            hand_pointing_down = False

        if ((lmList[hand_points[1]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] < lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] > lmList[hand_points[0]][2])):
            hand_pointing_left = True

        else:
            hand_pointing_left = False

    else:
        if ((lmList[hand_points[1]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] < lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] < lmList[hand_points[0]][2])):
            hand_pointing_up = True

        else:
            hand_pointing_up = False

        if ((lmList[hand_points[1]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] < lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] > lmList[hand_points[0]][2])):
            hand_pointing_right = True

        else:
            hand_pointing_right = False

        if ((lmList[hand_points[1]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] > lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] > lmList[hand_points[0]][2])):
            hand_pointing_down = True

        else:
            hand_pointing_down = False

        if ((lmList[hand_points[1]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] > lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] < lmList[hand_points[0]][2])):
            hand_pointing_left = True

        else:
            hand_pointing_left = False

        # Diagonal Positions (Same for both palm sides except depending on wether they facing up or right as well y and x for thumb detection change):

    if ((lmList[hand_points[1]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] < lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] < lmList[hand_points[0]][2])):
        diagonal_top_right = True

    else:
        diagonal_top_right = False

    if ((lmList[hand_points[1]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] < lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] < lmList[hand_points[0]][2])):
        diagonal_top_left = True

    else:
        diagonal_top_left = False

    if ((lmList[hand_points[1]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] > lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] > lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] > lmList[hand_points[0]][2])):
        diagonal_bottom_right = True

    else:
        diagonal_bottom_right = False

    if ((lmList[hand_points[1]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[1]][2] > lmList[hand_points[0]][2])) and ((lmList[hand_points[2]][1] < lmList[hand_points[0]][1]) and (lmList[hand_points[2]][2] > lmList[hand_points[0]][2])):
        diagonal_bottom_left = True

    else:
        diagonal_bottom_left = False

    # Test for thumb
    if palm_facing_camera_or_left_hand_not_facing:
        if hand_pointing_up or diagonal_top_right or diagonal_top_left:
            if hand_pointing_up and not diagonal_top_right and not diagonal_top_left:
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 2][1]:
                    pointing_fingers += 1
            elif diagonal_top_right and not diagonal_top_left:
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    pointing_fingers += 1

            elif diagonal_top_left and not diagonal_top_right:
                if lmList[tipIds[0]][2] < lmList[tipIds[0] - 1][2]:
                    pointing_fingers += 1

        elif hand_pointing_right and not diagonal_top_right and not diagonal_bottom_right:
            if lmList[tipIds[0]][2] > lmList[tipIds[0] - 1][2]:
                pointing_fingers += 1

        elif hand_pointing_down or diagonal_bottom_right or diagonal_bottom_left:

            if hand_pointing_down and not diagonal_bottom_right and not diagonal_bottom_left:
                if lmList[tipIds[0]][1] < lmList[tipIds[0] - 2][1]:
                    pointing_fingers += 1
            elif diagonal_bottom_right and not diagonal_bottom_left:
                if lmList[tipIds[0]][2] < lmList[tipIds[0] - 1][2]:
                    pointing_fingers += 1

            elif diagonal_bottom_left and not diagonal_bottom_right:
                if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                    pointing_fingers += 1

        elif hand_pointing_left and not diagonal_bottom_left and not diagonal_top_left:
            # If y value of thumb tip smaller than y value of under thumb tip
            if lmList[tipIds[0]][2] < lmList[tipIds[0] - 1][2]:
                pointing_fingers += 1

    else:

        if hand_pointing_up or diagonal_top_right or diagonal_top_left:
            if hand_pointing_up and not diagonal_top_right and not diagonal_top_left:
                if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                    pointing_fingers += 1
            elif diagonal_top_right and not diagonal_top_left:
                if lmList[tipIds[0]][2] < lmList[tipIds[0] - 1][2]:
                    pointing_fingers += 1

            elif diagonal_top_left and not diagonal_top_right:
                if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                    pointing_fingers += 1

        elif hand_pointing_right and not diagonal_bottom_right and not diagonal_top_right:
            if lmList[tipIds[0]][2] < lmList[tipIds[0] - 1][2]:
                pointing_fingers += 1

        elif hand_pointing_down or diagonal_bottom_right or diagonal_bottom_left:

            if hand_pointing_down and not diagonal_bottom_right and not diagonal_bottom_left:
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 2][1]:
                    pointing_fingers += 1
            elif diagonal_bottom_right and not diagonal_bottom_left:
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    pointing_fingers += 1

            elif diagonal_bottom_left and not diagonal_bottom_right:
                if lmList[tipIds[0]][2] > lmList[tipIds[0] - 1][2]:
                    pointing_fingers += 1

        elif hand_pointing_left and not diagonal_bottom_left and not diagonal_top_left:
            # If y value of thumb tip smaller than y value of under thumb tip
            if lmList[tipIds[0]][2] > lmList[tipIds[0] - 1][2]:
                pointing_fingers += 1

    # Test for number of finger pointing
    if hand_pointing_up or diagonal_top_right or diagonal_top_left:
        if hand_pointing_up and not diagonal_top_right and not diagonal_top_left:
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    pointing_fingers += 1
        elif diagonal_top_right and not diagonal_top_left:
            for id in range(1, 5):
                if lmList[tipIds[id]][1] > lmList[tipIds[id] - 2][1]:
                    pointing_fingers += 1

        elif diagonal_top_left and not diagonal_top_right:
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    pointing_fingers += 1

    elif hand_pointing_right and not diagonal_bottom_right and not diagonal_top_right:
        for id in range(1, 5):
            if lmList[tipIds[id]][1] > lmList[tipIds[id]-2][1]:
                pointing_fingers += 1

    elif hand_pointing_down or diagonal_bottom_right or diagonal_bottom_left:

        if hand_pointing_down and not diagonal_bottom_right and not diagonal_bottom_left:
            for id in range(1, 5):
                if lmList[tipIds[id]][2] > lmList[tipIds[id] - 2][2]:
                    pointing_fingers += 1
        elif diagonal_bottom_right and not diagonal_bottom_left:
            for id in range(1, 5):
                if lmList[tipIds[id]][1] > lmList[tipIds[id] - 2][1]:
                    pointing_fingers += 1

        elif diagonal_bottom_left and not diagonal_bottom_right:
            for id in range(1, 5):
                if lmList[tipIds[id]][1] < lmList[tipIds[id] - 2][1]:
                    pointing_fingers += 1

    elif hand_pointing_left and not diagonal_bottom_left and not diagonal_top_left:
        for id in range(1, 5):
            if lmList[tipIds[id]][1] < lmList[tipIds[id]-2][1]:
                pointing_fingers += 1
                
    
    if two_hands:
        added = pointing_fingers - temp_pointing_fingers
        
        if added == 2:
            right_hand_scissors = True
        else:
             right_hand_scissors = False
        if added == 0:
            right_hand_rock = True
        else:
            right_hand_rock = False
        if added == 5:
            right_hand_paper = True
        else:
            right_hand_paper = False
    
    else:
        if pointing_fingers == 2:
            left_hand_scissors = True
        else:
            left_hand_scissors = False
        if pointing_fingers == 0:
            left_hand_rock = True
        else:
            left_hand_rock = False
        if pointing_fingers == 5:
            left_hand_paper = True
        else:
            left_hand_paper = False
        

    return pointing_fingers, left_hand_rock, left_hand_paper, left_hand_scissors, right_hand_rock, right_hand_paper, right_hand_scissors


def aquire_information(lmList, tipIds, secound_hand_ids):
    # Gets number of pointing fingers
    pointing_fingers = 0
    two_hands = False
    
    #For rock / paper / scissors
    left_hand_rock = False
    left_hand_paper = False
    left_hand_scissors = False

    right_hand_rock = False
    right_hand_paper = False
    right_hand_scissors = False
    
    temp1 = False
    temp2 = False
    temp3 = False
    temp4 = False
    temp5 = False
    temp6 = False

    if len(lmList) > 21:
        two_hands = True
    else:
        two_hands = False

        # Two hands or not
    if not two_hands:
        pointing_fingers, temp1, temp2, temp3, temp4, temp5, temp6 = count_hand_pointing(
            lmList, tipIds, pointing_fingers, False)

    else:
        #Counts points on first hand
        pointing_fingers, left_hand_rock, left_hand_paper, left_hand_scissors, temp1, temp2, temp3 = count_hand_pointing(
            lmList, tipIds, pointing_fingers, False)
        
        #Counts points on secound hand
        pointing_fingers, temp1, temp2, temp3, right_hand_rock, right_hand_paper, right_hand_scissors = count_hand_pointing(
            lmList, secound_hand_ids, pointing_fingers, True)

    return pointing_fingers, two_hands, left_hand_rock, left_hand_paper, left_hand_scissors, right_hand_rock, right_hand_paper, right_hand_scissors


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)




pTime = 0

detector = htm.handDetector(detectionConfidence=0.90)

# first hand markers are from 0 to 20, second hand from 21 to 41
tipIds = [4, 8, 12, 16, 20]
secound_hand_ids = [20 + 5, 20 + 9, 20 + 13,
                    20 + 17, 20 + 21]  # 25, 29, 33, 37, 41


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPositions(img, draw=False)
    # print(len(lmList))
   

    if len(lmList) != 0:
        
        # Aquires all information of the hand position
         
    
        fingers, two_hands, left_hand_rock, left_hand_paper, left_hand_scissors, right_hand_rock, right_hand_paper, right_hand_scissors  = aquire_information(lmList, tipIds, secound_hand_ids)


        cv2.putText(img, str(fingers), (45, 375),
                    cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
        if two_hands:
            #Conditions for ties
            if left_hand_paper and right_hand_paper:
                cv2.putText(img, f'Paper Tie !', (200, 150),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            elif left_hand_scissors and right_hand_scissors:
                cv2.putText(img, f'Scissors Tie !', (200, 150),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                
            elif left_hand_rock and right_hand_rock:
                cv2.putText(img, f'Rock Tie !', (200, 150),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                
                
                
            #Conditions for wins
            elif left_hand_rock and right_hand_paper:
                cv2.putText(img, f'Left Player Wins!', (200, 150),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            elif right_hand_rock and left_hand_paper:
                cv2.putText(img, f'Right Player Wins!', (200, 150),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                
                
               
            elif left_hand_paper and right_hand_scissors:
                cv2.putText(img, f'Left Player Wins!', (200, 150),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            elif right_hand_paper and left_hand_scissors:
                cv2.putText(img, f'Right Player Wins!', (200, 150),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                
                
             
                
            elif left_hand_scissors and right_hand_rock:
                cv2.putText(img, f'Left Player Wins!', (200, 150),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            elif right_hand_scissors and left_hand_rock:
                cv2.putText(img, f'Right Player Wins!', (200, 150),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                
            
            

    
    cv2.putText(img, f'Press 1 to exit:', (100, 50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    
    if key == ord('1'):
        break

cv2.destroyAllWindows()
