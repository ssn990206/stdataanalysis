import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def calculate_dtw_similarity(result, hands):
    punches = result[hands]
    punch_data = []
    reasonable_punch = 0
    for punch in punches.values():
        if len(punch) >= 5:
            # print(f"{hands}: {len(punch)/25}")
            frames = np.array([[frame['x'], frame['y'], frame['z']] for frame in punch])
            punch_data.append(frames)
            reasonable_punch += 1
    print(f"reasonable_punch: {reasonable_punch}")
    
    # n_punches = len(punch_data)

    # create a n*n array
    dtw_distances = np.zeros((reasonable_punch, reasonable_punch))

    for i in range(reasonable_punch):
        for j in range(i + 1, reasonable_punch):
            distance, _ = fastdtw(punch_data[i], punch_data[j], dist=euclidean)
            dtw_distances[i, j] = distance
            dtw_distances[j, i] = distance

    # caculate each punches' similarity mean
    average_dtw_distances = np.mean(dtw_distances, axis=1)


    # caculate hand's similarity mean
    overall_similarity = np.mean(average_dtw_distances)
    return overall_similarity

