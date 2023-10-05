import cv2
import numpy as np
import mediapipe
import cvzone
from cvzone.PoseModule import PoseDetector
import math

count=0
direction=0

cap = cv2.VideoCapture("pushup.mp4")
pd = PoseDetector(trackCon=0.70, detectionCon=0.70)

def angles(lmlist,p1,p2,p3,p4,p5,p6,drawpoints):
    global count
    global direction

    if len(lmlist)!= 0:
        point1 = lmlist[p1]
        point2 = lmlist[p2]
        point3 = lmlist[p3]
        point4 = lmlist[p4]
        point5 = lmlist[p5]
        point6 = lmlist[p6]


        #points = [2,3,4,5,6]

        x1, y1 = point1[0:-1]
        x2, y2 = point2[0:-1]
        x3, y3 = point3[0:-1]
        x4, y4 = point4[0:-1]
        x5, y5 = point5[0:-1]
        x6, y6 = point6[0:-1]

        if drawpoints == True:
            cv2.circle(img, (x1, y1), 10, (255, 0, 255), 5)
            cv2.circle(img, (x1, y1), 15, (0, 255, 0), 5)
            cv2.circle(img, (x2, y2), 10, (255, 0, 255), 5)
            cv2.circle(img, (x2, y2), 15, (0, 255, 0), 5)
            cv2.circle(img, (x3, y3), 10, (255, 0, 255), 5)
            cv2.circle(img, (x3, y3), 15, (0, 255, 0), 5)
            cv2.circle(img, (x4, y4), 10, (255, 0, 255), 5)
            cv2.circle(img, (x4, y4), 15, (0, 255, 0), 5)
            cv2.circle(img, (x5, y5), 10, (255, 0, 255), 5)
            cv2.circle(img, (x5, y5), 15, (0, 255, 0), 5)
            cv2.circle(img, (x6, y6), 10, (255, 0, 255), 5)
            cv2.circle(img, (x6, y6), 15, (0, 255, 0), 5)
            cv2.line(img, (x1, y1),(x2,y2),(0,0,255),6)
            cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)
            cv2.line(img, (x1, y1), (x4, y4), (0, 0, 255), 6)
            cv2.line(img, (x4, y4), (x5, y5), (0, 0, 255), 6)
            cv2.line(img, (x5, y5), (x6, y6), (0, 0, 255), 6)

            lefthandangle = math.degrees(math.atan2(y3-y2,x3-x2)-
                                        math.atan2(y1-y2,x1-x2))
            righthandangle = math.degrees(math.atan2(y6 - y5 , x6 - x5) -
                                         math.atan2(y4 - y5, x4 - x5))

            #print(lefthandangle,righthandangle)
            lefthandangle = np.interp(lefthandangle, [-46, 183], [100, 0])
            righthandangle = np.interp(righthandangle, [39, 177], [100, 0])
            # print(lefthandangle, righthandangle)
            # print(lefthandangle)
            # print(righthandangle)
            left, right = lefthandangle, righthandangle
            # print(left, right)
            # if left >= 70 and right >= 70:
            #      if direction == 0:
            #         count += 0.5
            #         direction = 1
            # if left <= 70 and right <= 70:
            #      if direction == 1:
            #         count += 0.5
            #         direction = 0
            # cv2.rectangle(img, (0,0), (120, 120),(255,0,0), -1)
            # cv2.putText(img, str(int(count)), (4, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
            #             1.6,(0, 0, 255), 7)
            # leftval = np.interp(left, [0,100], [400,200])
            # rightval = np.interp(right, [0,100], [400,200])
            #
            # # righthand bar
            # cv2.rectangle(img, (8, 200), (50,400),(0, 255, 0), 5)
            # cv2.rectangle(img, (8, int(rightval)), (50,400),(0, 25, 0), -1)
            # # lefthand bar
            # cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
            # cv2.rectangle(img, (952, int(leftval)), (995, 400), (0, 255, 0), -1)
            if left >= 70 and right >= 70:
                if direction == 0:
                    count += 0.5
                    direction = 1
            if left <= 70 and right <= 70:
                if direction == 1:
                    count += 0.5
                    direction = 0

            cv2.rectangle(img, (0, 0), (120, 120), (255, 0, 0), -1)
            cv2.putText(img, str(int(count)), (20, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (0, 0, 255), 7)

            # leftval  = np.interp(left,[0,100],[400,200])
            rightval = np.interp(right, [0, 100], [400, 200])
            reference_range = [200, 400]
            percentage = ((rightval - reference_range[1]) / (reference_range[0] - reference_range[1])) * 100
            # print(percentage)

            # Display the percentage
            percentage_str = f"Form Accuracy: {percentage:.2f}%"
            #     accuracyRate = accuracy[len(percentage)]/len(percentage)
            #     percentage_str = f"Form Accuracy: {accuracyRate:.2f}%"
            #     cv2.putText(img, accuracyRate, (650, 190),
            #     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)
            cv2.putText(img, percentage_str, (650, 190),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)
            cv2.putText(img,'Muscle Intensity', (20, 190),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 4)
            cv2.rectangle(img, (28,200), (70,400), (0,255,0),5)
            cv2.rectangle(img, (28, int(rightval)), (70, 400), (255,0, 0), -1)

            # cv2.putText(img, 'L', (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 4)
            # cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
            # cv2.rectangle(img, (952, int(leftval)), (995, 400), (255, 0, 0), -1)


            # if left > 70:
            #     cv2.rectangle(img, (952, int(leftval)), (995, 400), (0, 0, 255), -1)

            if right > 70:
                cv2.rectangle(img, (28, int(rightval)), (70, 400), (0, 0, 255), -1)
            accuracy = []
            # while percentage > 95:
            #     accuracy.append(percentage)
            # print(accuracy)



while 1:
    ret, img = cap.read()
    if not ret:
        cap = cv2.VideoCapture("pushup.mp4")

        continue

    img = cv2.resize(img, (1000, 500))
    pd.findPose(img, draw=0)
    lmlist, bbox = pd.findPosition(img, draw=0, bboxWithHands=0)

    angles(lmlist,11,13,15,12,14,16, drawpoints=1)
    # print(lmlist[13])
    # point = lmlist[14]
    # cx, cy = point[1], point[2]
    # cv2.circle(img, (cx, cy),12, (0,0
    # ,255), -1)
    cv2.imshow('frame', img)
    cv2.waitKey(1)