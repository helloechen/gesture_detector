from calculate_angle_copy import *
def recognize_gesture(hand_landmark,finger_statuses):
    
    thumb_index_threshold = 25  
    index_middle_threshold = 45
    
    wrist = hand_landmark[0]
    thumb_tip = hand_landmark[4]
    index_finger_tip = hand_landmark[8]
    middle_finger_tip = hand_landmark[12]
    forth_finger_tip = hand_landmark[16]
    little_finger_tip = hand_landmark[20]
    
 
    thumb_index_angle = calculate_angle(thumb_tip, wrist, index_finger_tip)
    index_middle_angle = calculate_angle(index_finger_tip, wrist, middle_finger_tip)
    middle_forth_angle = calculate_angle(middle_finger_tip,wrist,forth_finger_tip)
    forth_little_angle = calculate_angle(forth_finger_tip,wrist,little_finger_tip)
    thumb_little_angle = calculate_angle(thumb_tip,wrist,little_finger_tip)
    print(f"拇指和食指的判别角度为{thumb_index_angle}度")
    print(f"食指与中指的判别角度为{index_middle_angle}度")
    print(f"中指和无名指的判别角度为{middle_forth_angle}度")
    print(f"无名指和小指的判别角度为{forth_little_angle}度")
    print(f"拇指和小指的判别角度为{thumb_little_angle}度")
      
    if thumb_index_angle is not None and index_middle_angle is not None and middle_forth_angle is not None and forth_little_angle is not None:
        if thumb_index_angle < 9 and finger_statuses[2] and finger_statuses[3]:
            return "OK"
        elif thumb_index_angle > thumb_index_threshold and index_middle_angle < index_middle_threshold and index_middle_angle > 10 and not finger_statuses[3] and not finger_statuses[4]:
            return "Three(basketball version)"
        elif finger_statuses[1] ==finger_statuses[2] == finger_statuses[3] ==finger_statuses[4] ==False:
            return "stone"
        elif (finger_statuses[1] == finger_statuses[2] == finger_statuses[3] == True) and thumb_little_angle > 22:
            return "cloth"
        elif (finger_statuses[1] == finger_statuses[2] == finger_statuses[3] == True) and thumb_little_angle < 20 and not finger_statuses[4]:
            return "three(gesture version)"
    return "Unknown"
