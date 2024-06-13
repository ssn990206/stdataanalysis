import math
import numpy as np

def twospot_distance_caculation(a, b):
    distance = []
    frame = 0
    for a, b in zip(a, b):
        Xa, Ya, Za = a['x'], a['y'], a['z']
        Xb, Yb, Zb = b['x'], b['y'], b['z']
        distance.append(math.dist([Xa, Ya], [Xb, Yb]))

    distance_average = np.average(distance)
    distance_std = np.std(distance)
    return distance_average, distance_std

def movement_caculation(a):
    movement_distance = []
    X_pre = 0
    Y_pre = 0
    Z_pre = 0
    for spot in a:
        if X_pre == 0 and Y_pre == 0 and Z_pre == 0:
            X_pre, Y_pre, Z_pre = spot['x'], spot['y'], spot['z']
        else:
            X, Y, Z = spot['x'], spot['y'], spot['z']
            movement_distance.append(math.dist([X_pre, Y_pre], [X, Y]))
            X_pre, Y_pre, Z_pre = X, Y, Z
    
    distance_sum = sum(movement_distance)
    distance_average = np.average(movement_distance)
    distance_std = np.std(movement_distance)
    return distance_sum, distance_average, distance_std

def hand_movement_caculation(a):
    movement_distance = []
    X_pre = 0
    Y_pre = 0
    Z_pre = 0
    for spot in a:
        if X_pre == 0 and Y_pre == 0 and Z_pre == 0:
            X_pre, Y_pre, Z_pre = spot['x'], spot['y'], spot['z']
        else:
            X, Y, Z = spot['x'], spot['y'], spot['z']
            movement_distance.append(math.dist([X_pre, Y_pre], [X, Y]))
            X_pre, Y_pre, Z_pre = X, Y, Z
    
    distance_sum = sum(movement_distance)
    distance_average = (distance_sum) / 15
    # distance_std = np.std(movement_distance)
    return distance_average