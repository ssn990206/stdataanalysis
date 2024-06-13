import json
import numpy as np

def extract_punches(data):
    left_hand_punches = {}
    right_hand_punches = {}
    current_frame = 0
    current_punch = 0
    left_punch_id = 1
    right_punch_id = 1
    left_hand_data = data["lefthand"]
    right_hand_data = data["righthand"]
    chest_data = data["chest"]
    
    while current_punch < len(data['avatarPunchData']):
        punch_data = data['avatarPunchData'][current_punch]
        
        if punch_data == 0:
            lh_transfered = []
            ch_transfered = []
            for lh, ch in zip(left_hand_data[current_frame + 5:current_frame + 30], chest_data[current_frame + 5:current_frame + 30]):
                lh_transfered.append({'x': lh['x'], 'y': lh['y'], 'z': lh['z']})
                ch_transfered.append({'x': ch['x'], 'y': ch['y'], 'z': ch['z']})
            max_distance_index = calculate_max_distance_frame(lh_transfered, ch_transfered, "left")

            left_hand_punch = data['lefthand'][current_frame + 5:current_frame + max_distance_index]
            if len(left_hand_punch) >= 10:
                left_hand_punches[f"{left_punch_id:02}"] = left_hand_punch
                left_punch_id += 1

        elif punch_data == 1:
            rh_transfered = []
            ch_transfered = []
            for rh, ch in zip(right_hand_data[current_frame + 5:current_frame + 30], chest_data[current_frame + 5:current_frame + 30]):
                rh_transfered.append({'x': rh['x'], 'y': rh['y'], 'z': rh['z']})
                ch_transfered.append({'x': ch['x'], 'y': ch['y'], 'z': ch['z']})
            max_distance_index = calculate_max_distance_frame(rh_transfered, ch_transfered, "right")

            right_hand_punch = data['righthand'][current_frame + 5:current_frame + max_distance_index]
            if len(right_hand_punch) >= 10:
                right_hand_punches[f"{right_punch_id:02}"] = right_hand_punch
                right_punch_id += 1
        current_frame += 50
        current_punch += 1
    

    return left_hand_punches, right_hand_punches

# 計算最小距離的frame 
def calculate_min_distance_frame(punch_frames, robot_frames, hand):
    min_distance_index = 0
    # initial is infinite
    min_distance = float('inf')

    for i, (punch_frame, robot_frame) in enumerate(zip(punch_frames, robot_frames)):
        distance = np.linalg.norm(np.array([punch_frame['x'], punch_frame['y'], punch_frame['z']]) -
                                  np.array([robot_frame['x'], robot_frame['y'], robot_frame['z']]))
        if distance < min_distance:
            min_distance = distance
            min_distance_index = i

    print(f'{hand} : {min_distance_index}')
    return min_distance_index

# 計算最大距離的frame 
def calculate_max_distance_frame(punch_frames, robot_frames, hand):
    max_distance_index = 0
    # initial is negative infinite
    max_distance = float('-inf')

    for i, (punch_frame, robot_frame) in enumerate(zip(punch_frames, robot_frames)):
        distance = np.linalg.norm(np.array([punch_frame['x'], punch_frame['y'], punch_frame['z']]) -
                                  np.array([robot_frame['x'], robot_frame['y'], robot_frame['z']]))
        if distance > max_distance:
            max_distance = distance
            max_distance_index = i

    print(f'{hand} : {max_distance_index}')
    return max_distance_index
