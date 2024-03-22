import numpy as np

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