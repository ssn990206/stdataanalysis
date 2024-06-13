import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def calculate_dtw_similarity(result, hands):
    punches = result[hands]
    punch_data = []
    for punch in punches.values():
        frames = np.array([[frame['x'], frame['y'], frame['z']] for frame in punch])
        punch_data.append(frames)
    
    n_punches = len(punch_data)

    dtw_distances = np.zeros((n_punches, n_punches))

    for i in range(n_punches):
        for j in range(i + 1, n_punches):
            distance, _ = fastdtw(punch_data[i], punch_data[j], dist=euclidean)
            dtw_distances[i, j] = distance
            dtw_distances[j, i] = distance

    # caculate each punches' similarity mean
    average_dtw_distances = np.mean(dtw_distances, axis=1)

    # caculate hand's similarity mean
    overall_similarity = np.mean(average_dtw_distances)
    return overall_similarity

