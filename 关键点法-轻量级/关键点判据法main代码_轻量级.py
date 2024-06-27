import cv2 
from calculate_angle_copy import *
from recognize_gesture_copy import recognize_gesture
from cvzone.HandTrackingModule import HandDetector

fingers_tips = [4, 8, 12, 16, 20]
finger_second = [3,7,11,15,19]
finger_third = [2,6,10,14,18]
fingers_dips = [1,5,9,13,17]

def main():
    
    count  = 0
    count2 = 0
    isalive = True
    issure = False
    handtemp = ""
    model = ""
    detector = HandDetector(staticMode=False,  # 非静态模式，持续检测
                        maxHands=2,         # 最多检测两只手
                        modelComplexity=1,  # 手部识别模型复杂度
                        detectionCon=0.5,   # 手部检测的最小置信度
                        minTrackCon=0.5)    # 追踪的最小置信度

    cap = cv2.VideoCapture(0)


    while True:
        success, img = cap.read()
        
        if not success:
            print('摄像头打开失败')
            break

        hands, img = detector.findHands(img, draw=False, flipType=True)
        
        if hands:
            for hand1 in hands:
            # 遍历每个检测到的手
                lmList1 = hand1["lmList"]  # 21个关键点坐标列表
                handType1 = hand1["type"]   # 手型（"Left" 或 "Right"）
                fingers1 = detector.fingersUp(hand1)
                
                if isalive:
                    print(f"手指张开情况{fingers1}")
                    result = recognize_gesture(lmList1,fingers1)
                    hand_gesture = handType1
                    if(handtemp ==hand_gesture):
                        count2 = count2+1
                    else:
                        handtemp = hand_gesture
                        count2 = 0
                    if(count2 == 3):
                        issure = True
                        count2 = 0
                    if(issure):
                        print(f"检测到的手势类型: {hand_gesture}")
                        model = result 
                        print(result)
                        issure = False
                    print("------------------------------------")
                    isalive = False
                    
                count = count + 1
                    
                if count == 5:
                    count = 0
                    isalive = True
                    
        cv2.putText(img, model, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA) 

        cv2.namedWindow("gesture detection",cv2.WINDOW_NORMAL)
        cv2.resizeWindow("gesture detection",800,600)
        img = cv2.copyMakeBorder(img,5,5,5,5,cv2.BORDER_CONSTANT,value = [0, 0, 0] )
        cv2.imshow("gesture detection", img)
        
        key = cv2.waitKey(1) & 0xFF  #imshow后面必须要有waitkey(delay)函数,否则窗口一闪而过。单位ms,0默认，<=0为永久延迟直到按键，没按则返回-1，按了就返回对应按键
        if key == ord('q'):
            break
        
        
    cap.release()


    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()

                