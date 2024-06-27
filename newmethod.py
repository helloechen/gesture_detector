from cvzone.HandTrackingModule import HandDetector
import cv2

# 初始化摄像头以捕捉视频
# 通常 '0' 指内置摄像头
cap = cv2.VideoCapture(0)

# 初始化 HandDetector 类并设置参数
detector = HandDetector(staticMode=False,  # 非静态模式，持续检测
                        maxHands=2,         # 最多检测两只手
                        modelComplexity=1,  # 手部识别模型复杂度
                        detectionCon=0.5,   # 手部检测的最小置信度
                        minTrackCon=0.5)    # 追踪的最小置信度

# 实时从摄像头获取帧
while True:
    # 读取每一帧图像
    # 'success' 表示是否成功捕获，'img' 存储捕获的图像
    success, img = cap.read()

    # 在当前帧中寻找手部
    # 'draw' 参数决定是否在图像上绘制手部关键点和边界框
    # 'flipType' 翻转图像，便于某些检测操作
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # 检查是否检测到手
    if hands:
        # 获取第一只手的信息
        hand1 = hands[0]           # 第一只手
        lmList1 = hand1["lmList"]  # 21个关键点坐标列表
        bbox1 = hand1["bbox"]      # 手部边界框坐标
        center1 = hand1['center']  # 手心中心点坐标
        handType1 = hand1["type"]  # 手型（"Left" 或 "Right"）

        # 计算第一只手抬起的手指数量
        fingers1 = detector.fingersUp(hand1)
        print(f'H1 = {fingers1}', end=" ")  # 输出抬起手指的数量

        # 定位食指和中指指尖
        tipOfIndexFinger = lmList1[8][0:2]
        tipOfMiddleFinger = lmList1[12][0:2]

        # 计算并绘制食指与中指指尖间的距离
        length, info, img = detector.findDistance(tipOfIndexFinger, tipOfMiddleFinger, img, color=(255, 0, 255), scale=5)

        # 检查是否有第二只手
        if len(hands) == 2:
            # 获取第二只手的信息
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            center2 = hand2['center']
            handType2 = hand2["type"]

            # 计算第二只手抬起的手指数量
            fingers2 = detector.fingersUp(hand2)
            print(f'H2 = {fingers2}', end=" ")

            # 定位第二只手的食指指尖
            tipOfIndexFinger2 = lmList2[8][0:2]

            # 计算并绘制两只手食指指尖间的距离
            length, info, img = detector.findDistance(tipOfIndexFinger, tipOfIndexFinger2, img, color=(255, 0, 0), scale=10)

        print()  # 打印换行，提高输出可读性

    # 显示处理后的图像
    cv2.imshow("图像", img)

    # 保持窗口打开，等待1毫秒后显示下一帧
    cv2.waitKey(1)