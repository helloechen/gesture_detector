
# 导入所需的库
import mediapipe as mp  # 使用mediapipe库进行手部识别
import cv2  # 使用OpenCV库进行图像处理

# 配置mediapipe
hand_drawing_utils = mp.solutions.drawing_utils  # 绘图工具
mp_hands = mp.solutions.hands  # 手部识别api
my_hands = mp_hands.Hands()  # 创建手部识别对象

# 打开摄像头，参数0表示默认摄像头
cap = cv2.VideoCapture(0)

# 通过循环读取每一帧图像
while True:
    # 从摄像头读取一帧图像
    success, img = cap.read()

    # 检查摄像头是否成功打开
    if not success:
        print('摄像头打开失败')
        break

    # 将BGR图像转换为RGB格式，因为mediapipe库使用RGB格式
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 使用mediapipe库识别图像中的手势，并返回结果
    results = my_hands.process(img)

    # 将RGB图像转换回BGR格式，以便使用OpenCV绘制图像
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # 判断是否检测到手部关键点
    if results.multi_hand_landmarks:
        # 遍历每个检测到的手
        for hand_landmark in results.multi_hand_landmarks:
            
            
            for hand_landmark in results.multi_hand_landmarks:
            # 获取腕部的关键点坐标
                wrist = hand_landmark.landmark[0]
                wrist_x = wrist.x
                wrist_y = wrist.y
                wrist_z = wrist.z
                print(f"腕部坐标: ({wrist_x}, {wrist_y}, {wrist_z})")
                
                # 获取五个手指尖的关键点坐标并输出
                fingertips = [
                    (mp_hands.HandLandmark.INDEX_FINGER_TIP, "食指"),
                    (mp_hands.HandLandmark.MIDDLE_FINGER_TIP, "中指"),
                    (mp_hands.HandLandmark.RING_FINGER_TIP, "无名指"),
                    (mp_hands.HandLandmark.PINKY_TIP, "小指"),
                    (mp_hands.HandLandmark.THUMB_TIP, "拇指")
                ]
                for landmark, finger_name in fingertips:
                    fingertip = hand_landmark.landmark[landmark]
                    fingertip_x = fingertip.x
                    fingertip_y = fingertip.y
                    fingertip_z = fingertip.z
                    print(f"{finger_name}手指尖坐标: ({fingertip_x}, {fingertip_y}, {fingertip_z})")
                
                hand_gesture = results.multi_handedness[0].classification[0].label
                print(f"检测到的手势类型: {hand_gesture}")

                
                print("\n")    

            
            # 使用mediapipe的绘图工具绘制手部关键点和连接线
            hand_drawing_utils.draw_landmarks(img,
                                              hand_landmark,
                                              mp_hands.HAND_CONNECTIONS,
                                              mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
                                              mp.solutions.drawing_styles.get_default_hand_connections_style())
            
            

    # 左右镜像翻转图像，使得图像在显示时更符合自然习惯
    img = cv2.flip(img, 1)

    # 在窗口中显示图像
    cv2.imshow("frame", img)

    # 检测键盘输入，如果按下 'q' 键则退出循环
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# 释放摄像头资源
cap.release()

# 关闭所有OpenCV窗口
cv2.destroyAllWindows()




