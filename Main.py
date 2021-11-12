from typing import overload
import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

#Size
brush = 15
eraser = 60
#Color
drawColor = (255, 0, 255) #Pink

#Background Folder
folderPath = "Pic"
myList = os.listdir(folderPath)
#print(myList)
count = 0
mode = 0
overlayList = []
#Save image in folderPath to overlayList
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
#print(len(overlayList))

#Setting background
header = overlayList[3]

cap = cv2.VideoCapture(0)
#Width = 1280
cap.set(3, 1280)
#Height = 720  
cap.set(4, 720)

detector = htm.handDetector(detectionCon = 0.85)
#Previous position
x0, y0 = 0, 0

imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    #Show camera
    success, img = cap.read()
    #Flip camera 
    img = cv2.flip(img, 1)
    #Draw landmarks
    img = detector.findHands(img)
    lmList = detector.findPos(img, draw=False)

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    if len(lmList)!=0:
        #print(lmList)

        #Index finger
        x1, y1 = lmList[8][1:]
        #Middle finger
        x2, y2 = lmList[12][1:]

        #Checking finger (Up/Down)
        finger = detector.fingerUP()
        #print(finger)

        #Drawing Mode
        if finger[1]==True and finger[2]==False:
            cv2.circle(img, (x1,y1), 15, drawColor, cv2.FILLED)
            #print("Drawing Mode")
            if x0 == 0 and y0 == 0:
                x0, y0 = x1, y1
            #Draw & Eraser line in img:
            if mode == 2:
                cv2.line(img, (x0, y0), (x1, y1), drawColor, eraser)
                cv2.line(imgCanvas, (x0, y0), (x1, y1), drawColor, eraser)
            elif mode == 1:
                cv2.line(img, (x0, y0), (x1, y1), drawColor, brush)
                cv2.line(imgCanvas, (x0, y0), (x1, y1), drawColor, brush)

            x0, y0 = x1, y1

        #Selecting Mode
        if finger[1] and finger[2]:
            #print("Selection Mode")
            x0, y0 = 0, 0
            if 0< y1 < 125: 
                if 102 < x1 < 240: 
                    header = overlayList[0]
                    drawColor = (255, 0, 255) 
                    mode = 1

                elif 569 < x1 < 707: 
                    header = overlayList[1]
                    drawColor = (0, 0, 0)   
                    mode = 2 

                elif 1074 < x1 < 1181: 
                    header = overlayList[2]
                    pw_r = "password_record.png"
                    img_r = "image_record.png"
                    cv2.imwrite(pw_r, imgInv)
                    cv2.imwrite(img_r, img)
                    break
                    #Export passwork screen to file png

            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

    #Setting header image
    img[0:125, 0:1280] = header
    #img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
    cv2.imshow("Image",img)
    #cv2.imshow("Canvas",imgCanvas)
    #cv2.imshow("Inv",imgInv)
    key = cv2.waitKey(1)
    if key == ord('s'):
        break