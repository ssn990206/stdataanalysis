import json
import numpy as np
from script.get_input import get_input_coordinates
from script.pos_matrix import translate_to_origin, rotate_to_positive_x
from script.caculation import twospot_distance_caculation, movement_caculation, hand_movement_caculation
from script.hand_extraction import extract_punches
from script.fastDTW import calculate_dtw_similarity
from script.test import write_visualization

def main():
    # input file number
    filenum = input('file_num: ')
    # input data RH, LH, RSH, LSH, CH, RL, LL, MR (A, B, C, D, E, F, G, H)
    RH, LH, RSH, LSH, CH, RL, LL, MR, avatarPunchData = get_input_coordinates(f'data/user_8_{filenum}.json')

# Transition Matrix
    # transform matrix
    righthand_translated, lefthand_translated, rightshoulder_translated, leftshoulder_translated, chest_translated, rightleg_translated, movingrobot_translated, leftleg_translated = translate_to_origin(LSH, MR, RSH, RH, LH, CH, LL, RL )
    # rotation matrix
    righthand_rotated, lefthand_rotated, rightshoulder_rotated, leftshoulder_rotated, rightleg_rotated, movingrobot_rotated, leftleg_rotated = rotate_to_positive_x(righthand_translated, lefthand_translated, rightshoulder_translated, leftshoulder_translated, chest_translated, rightleg_translated, movingrobot_translated, leftleg_translated)
# Distance Caculation
    # chest distance caculate
    chest_distance_average, chest_distance_std = twospot_distance_caculation(chest_translated, movingrobot_rotated)
    # total movement caculate
    movement_distance_sum, movement_distance_average, movement_distance_std = movement_caculation(CH)

    rh_movement_distance_average = hand_movement_caculation(RH)
    lh_movement_distance_average = hand_movement_caculation(LH)
    
    result = {
        'chest': chest_translated,
        'righthand': righthand_rotated,
        'lefthand': lefthand_rotated,
        # 'rightshoulder': rightshoulder_rotated,
        # 'leftshoulder': leftshoulder_rotated,
        # 'rightleg': rightleg_rotated,
        # 'leftleg': leftleg_rotated,
        'movingrobot': movingrobot_rotated,
        'chestDistanceAverage': chest_distance_average,
        'chestDistanceStd': chest_distance_std,
        'movementDistanceSum': movement_distance_sum,
        'rhMovementDistanceSum': rh_movement_distance_average,
        'lhMovementDistanceSum': lh_movement_distance_average,
        # "avatarPunchData": [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        "avatarPunchData": avatarPunchData,
    }
# Extract Punches
    left_hand_punches, right_hand_punches = extract_punches(result)
    result['leftHandPunches'] = left_hand_punches
    result['rightHandPunches'] = right_hand_punches
    # DTW caculation
    left_hand_similarity = calculate_dtw_similarity(result, 'leftHandPunches')
    right_hand_similarity = calculate_dtw_similarity(result, 'rightHandPunches')
    print(left_hand_similarity, right_hand_similarity)
    result['leftHandSimilarity'], result['rightHandSimilarity'] = left_hand_similarity, right_hand_similarity
    

# write json
    with open(f'data/transformed_data_8{filenum}.json', 'w') as outfile:
        json.dump(result, outfile, indent=4)

# run visualization
    write_visualization(f'data/transformed_data_8{filenum}.json')

if __name__ == "__main__":
    main()


# 8_4 no haptic, 8_5 with haptic