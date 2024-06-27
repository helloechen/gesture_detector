import mediapipe as mp 
import cv2 
import numpy as np

fingers_tips = [4, 8, 12, 16, 20]
fingers_dips = [1, 5, 9, 13, 17]

def calculate_angle(point1, point2, point3):
    vector1_x = point1.x -point2.x
    vector1_y = point1.y -point2.y
    vector1_z = point1.z -point2.z
    vector2_x = point3.x -point2.x
    vector2_y = point3.y -point2.y
    vector2_z = point3.z -point2.z
    vector1 = np.array([vector1_x,vector1_y,vector1_z])
    vector2 = np.array([vector2_x,vector2_y,vector2_z])

    vector1 /= np.linalg.norm(vector1)
    vector2 /= np.linalg.norm(vector2)
    
    dot_product = np.dot(vector1, vector2)
    
    angle = np.arccos(dot_product) * (180 / np.pi)
    
    return angle
   
def recognize_gesture(hand_landmark,finger_statuses):
    
    thumb_index_threshold = 25  
    index_middle_threshold = 45
    
    wrist = hand_landmark.landmark[0]
    thumb_tip = hand_landmark.landmark[4]
    index_finger_tip = hand_landmark.landmark[8]
    middle_finger_tip = hand_landmark.landmark[12]
    
 
    thumb_index_angle = calculate_angle(thumb_tip, wrist, index_finger_tip)
    index_middle_angle = calculate_angle(index_finger_tip, wrist, middle_finger_tip)
    print(f"拇指和食指的判别角度为{thumb_index_angle}度")
    print(f"食指与中指的判别角度为{index_middle_angle}度")
    
    
    if thumb_index_angle is not None and index_middle_angle is not None:
        if thumb_index_angle < 13 and index_middle_angle > 15 and finger_statuses[2] and finger_statuses[3]:
            return "OK"
        elif thumb_index_angle > thumb_index_threshold and index_middle_angle < index_middle_threshold and index_middle_angle > 10 and not finger_statuses[3] and not finger_statuses[4]:
            return "Three"
    return "Unknown"




hand_drawing_utils = mp.solutions.drawing_utils 
mp_hands = mp.solutions.hands  
my_hands = mp_hands.Hands() 
count  = 0
count2 = 0
isalive = True
issure = False
handtemp = ""
model = ""


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
            #for hand_landmark in results.multi_hand_landmarks:
                landmarks = np.array([(landmark.x * img.shape[1], landmark.y * img.shape[0]) for landmark in hand_landmark.landmark], dtype=int)
           
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
                    
                    
                    finger_statuses = np.zeros(5, dtype=bool)    
        
                    for i in range(5):
                        v = landmarks[fingers_tips[i]] - landmarks[fingers_dips[i]]
                        if np.linalg.norm(v) > 60:
                            finger_statuses[i] = True 
                            
                    result = recognize_gesture(hand_landmark,finger_statuses) 
                    
                    hand_gesture = results.multi_handedness[0].classification[0].label
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
                        model = result 
                        print(result)
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
    cv2.putText(img, model, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA) 

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




