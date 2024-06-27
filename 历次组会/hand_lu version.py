import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
# 设置摄像头ID
cap = cv2.VideoCapture(0)
# 设置视频分辨率
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 将灰度图像转换为彩色图像（如果需要的话）
    if frame.shape[2] == 1:  # 检查图像是否为灰度图像（只有一个通道）
        gray = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # 将灰度图像转换为彩色图像
    else:
        gray = frame  # 如果图像已经是彩色图像，则不需要转换
    
    # 将图像传递给手势识别模型进行识别
    results = hands.process(gray)
    if results.multi_hand_landmarks:
        # 获取手势的轮廓点坐标和置信度等数据
        landmarks = results.multi_hand_landmarks[0]
        # 在图像上绘制轮廓线（可根据需要自定义绘制方式）
        mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
    
    cv2.imshow('Mediapipe Hands', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break