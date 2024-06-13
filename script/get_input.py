import json
import math
from script.function import download_file

def get_input_coordinates(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    A = get_data(data, "RE")
    B = get_data(data, "LE")
    C = get_data(data, "RS")
    D = get_data(data, "LS")
    E = get_data(data, "CH")
    F = get_data(data, "RF")
    G = get_data(data, "LF")
    H = get_data(data, "KB")

    avatarPunchData = data['AvatarPunchData']
    
    return A, B, C, D, E, F, G, H, avatarPunchData

# def get_data(data, index):
#     for tracker in data['VTrackerDatas']:
#         if tracker['TrackerIndex'] == index:
#             positions = tracker['TrackerPositions']
#             return [{'x': pos['x']*-1, 'y': pos['z']*-1, 'z': pos['y']} for pos in positions]
#     return []

def get_data(data, index):
    pre_position = {'x': None, 'y': None, 'z': None}
    for tracker in data['VTrackerDatas']:
        if tracker['TrackerIndex'] == index:
            positions = tracker['TrackerPositions']
            result = []
            for pos in positions:
                if (pos['z'] <= -50 or pos['y'] <= -50 or pos['z'] <= -50) and pre_position['z'] is not None:
                    result.append(pre_position)
                else:
                    current_position = {'x': pos['x'],'y': pos['z'],'z': pos['y']}
                    result.append(current_position)
                    pre_position = current_position
            return result
    return []

if __name__ == "__main__":
    LSH, MR, RSH, RH, LH, CH, RL, LL = get_input_coordinates('data/user_3_2.json')