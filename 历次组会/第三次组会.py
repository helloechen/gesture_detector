
import mediapipe as mp 
import cv2 
import numpy as np


hand_drawing_utils = mp.solutions.drawing_utils 
mp_hands = mp.solutions.hands  
my_hands = mp_hands.Hands() 
count  = 0
count2 = 0
isalive = True
issure = False
handtemp = ""


cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()#这里的image是一个Numpy的array数组

    
    if not success:
        print('摄像头打开失败')
        break

    height  = np.shape(img)[0]
    width = np.shape(img)[1]
    channels = np.shape(img)[2]
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    
    results = my_hands.process(img)

    # 将RGB图像转换回BGR格式，以便使用OpenCV绘制图像
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    
    if results.multi_hand_landmarks:
        # 遍历每个检测到的手
        for hand_landmark in results.multi_hand_landmarks:
            
            
            for hand_landmark in results.multi_hand_landmarks:
           
                if isalive:
                    print("本帧采样的图片样本参数：","height=",height,"width=",width,"channels=",channels)
                    
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
                    #print(hand_gesture)
                    if hand_gesture == "Left":
                        hand_gesture = "Right"
                    elif hand_gesture == "Right":
                        hand_gesture = "Left"
                    if(handtemp ==hand_gesture):
                        count2 = count2+1
                    else:
                        handtemp = hand_gesture
                        count2 = 0
                    if(count2 == 3):
                        issure = True
                        count2 = 0
                    #print(hand_gesture)
                    #print(handtemp)
                    #print(count)
                    if(issure):
                        print(f"检测到的手势类型: {hand_gesture}")
                        issure = False

                    #print("hello")
                    print("\n")
                    isalive = False    
    
            
                           
                    
                
            # 使用mediapipe的绘图工具绘制手部关键点和连接线
                hand_drawing_utils.draw_landmarks(img,
                                                hand_landmark,
                                                mp_hands.HAND_CONNECTIONS,
                                                mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
                                                mp.solutions.drawing_styles.get_default_hand_connections_style())
            
                count = count + 1
                
                if count == 12:
                    count = 0
                    isalive = True
            

    
    img = cv2.flip(img, 1)

    cv2.namedWindow("gesture detection",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("gesture detection",800,600)#可以调节到自己喜欢的大小
    cv2.imshow("gesture detection", img)
    #正常应该去先namedWindow(winname,[,flags]),但是high_level GUI模块的imshow函数会弥补
    #cv2.WINDOW_AUTOSIZE,cv2.WINDOW_NORMAL

    key = cv2.waitKey(1) & 0xFF  #imshow后面必须要有waitkey(delay)函数,否则窗口一闪而过。单位ms,0默认，<=0为永久延迟直到按键，没按则返回-1，按了就返回对应按键
    if key == ord('q'):
        break


cap.release()


cv2.destroyAllWindows()




   