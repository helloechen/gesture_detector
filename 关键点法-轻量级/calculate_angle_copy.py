import numpy as np

def calculate_angle(point1, point2, point3):
    vector1_x = point1[0] -point2[0]
    vector1_y = point1[1] -point2[1]
    vector1_z = point1[2] -point2[2]
    vector2_x = point3[0] -point2[0]
    vector2_y = point3[1] -point2[1]
    vector2_z = point3[2] -point2[2]
    vector1 = np.array([vector1_x,vector1_y,vector1_z],dtype='float64')
    vector2 = np.array([vector2_x,vector2_y,vector2_z],dtype='float64')

    vector1 /= np.linalg.norm(vector1)
    vector2 /= np.linalg.norm(vector2)
    
    dot_product = np.dot(vector1, vector2)
    
    angle = np.arccos(dot_product) * (180 / np.pi)
    
    return angle