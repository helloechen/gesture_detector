import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
from cvzone.ClassificationModule import Classifier


labels = ["one","two","three","six","OK","good","up","down"] 

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgSize = 300

classifier = Classifier(r"D:\hands\model\keras_model.h5",r"D:\hands\model\labels.txt")

while True:
    success, img = cap.read()
    if not success:
        print("无法从摄像头读取帧")
        break

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        img_white = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        # 确保不会裁剪到图像外部
        imgCrop = img[max(y - offset, 0):min(y + h + offset, img.shape[0]),
                      max(x - offset, 0):min(x + w + offset, img.shape[1])]

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            resized_img = cv2.resize(imgCrop, (wCal, imgSize))

            w_offset = math.ceil((imgSize - wCal) / 2)
            img_white[:, w_offset:wCal + w_offset] = resized_img
            
            prediction, index =classifier.getPrediction(img_white)
            print(prediction)
            
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            resized_img = cv2.resize(imgCrop, (imgSize, hCal))

            h_offset = math.ceil((imgSize - hCal) / 2)
            img_white[h_offset:hCal + h_offset, :] = resized_img
            
            prediction, index =classifier.getPrediction(img_white)
            print(prediction)
         
         
        cv2.rectangle(img,(x-offset,y-offset-50),(x+w+offset,y-offset),(255,0,255),thickness=-1) #类别标注外面的矩形框
        cv2.putText(img,labels[index],(x,y-26),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,255,255),2)   #写类别标注
        cv2.rectangle(img,(x-offset,y-offset),(x+w+offset,y+h+offset),(255,0,255),2)    #绘制手外面的矩形框
            
            
            

        

    cv2.imshow("image", img)
    key = cv2.waitKey(1)

    if key == ord("q"):  # 检查是否按下了'q'键
        break  # 如果按下了'q'键，则终止循环

# 释放摄像头资源
cap.release()

# 关闭所有OpenCV窗口
cv2.destroyAllWindows()
