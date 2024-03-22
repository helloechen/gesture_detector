import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import os

folder=r"D:\hands\images\stone"
# 确保文件夹存在
if not os.path.exists(folder):
    os.makedirs(folder)

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgSize = 300
counter = 0

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
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            resized_img = cv2.resize(imgCrop, (imgSize, hCal))

            h_offset = math.ceil((imgSize - hCal) / 2)
            img_white[h_offset:hCal + h_offset, :] = resized_img

        cv2.imshow("img_white", img_white)

    cv2.imshow("image", img)
    key = cv2.waitKey(1)

    if key == ord("s"):
        counter += 1
        cv2.imwrite(os.path.join(folder, f'{counter}.jpg'), img_white)
        print(counter)
    elif key == ord("q"):  # 检查是否按下了'q'键
        break  # 如果按下了'q'键，则终止循环

# 释放摄像头资源
cap.release()

# 关闭所有OpenCV窗口
cv2.destroyAllWindows()
