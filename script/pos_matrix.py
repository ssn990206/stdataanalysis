import numpy as np
import math
import json
from script.function import download_file

def translate_to_origin(LSH, MR, RSH, RH, LH, CH, RL, LL ):
    translated_leftshoulder = []
    translated_movingrobot = []
    translated_rightshoulder = []
    translated_righthand = []
    translated_lefthand = []
    translated_chest = []
    translated_leftleg = []
    translated_rightleg = []

    # robot height = 0.56m
    averageHeightGet = 0
    # for mr in MR:


    for lsh, mr, rsh, rh, lh, ch, rl, ll in zip(LSH, MR, RSH, RH, LH, CH, RL, LL ):
        if(averageHeightGet == 0):
            robotHeight = 0.56 - mr['z']
            averageHeightGet += 1

        Xlsh, Ylsh, Zlsh = lsh['x'], lsh['y'], lsh['z']
        Xmr, Ymr, Zmr = mr['x'], mr['y'], mr['z']
        Xrsh, Yrsh, Zrsh = rsh['x'], rsh['y'], rsh['z']
        Xrh, Yrh, Zrh = rh['x'], rh['y'], rh['z']
        Xlh, Ylh, Zlh = lh['x'], lh['y'], lh['z']
        Xch, Ych, Zch = ch['x'], ch['y'], ch['z']
        Xrl, Yrl, Zrl = rl['x'], rl['y'], rl['z']
        Xll, Yll, Zll = ll['x'], ll['y'], ll['z']
        translation_matrix = np.array([[1, 0, 0, -Xch],
                                       [0, 1, 0, -Ych],
                                       [0, 0, 1, robotHeight],
                                       [0, 0, 0, 1]])
        chest_translated = np.dot(translation_matrix, np.array([Xch, Ych, Zch, 1]))
        rightshoulder_translated = np.dot(translation_matrix, np.array([Xrsh, Yrsh, Zrsh, 1]))
        leftshoulder_translated = np.dot(translation_matrix, np.array([Xlsh, Ylsh, Zlsh, 1]))
        righthand_translated = np.dot(translation_matrix, np.array([Xrh, Yrh, Zrh, 1]))
        lefthand_translated = np.dot(translation_matrix, np.array([Xlh, Ylh, Zlh, 1]))
        rightleg_translated = np.dot(translation_matrix, np.array([Xrl, Yrl, Zrl, 1]))
        leftleg_translated = np.dot(translation_matrix, np.array([Xll, Yll, Zll, 1]))
        movingrobot_translated = np.dot(translation_matrix, np.array([Xmr, Ymr, Zmr, 1]))

        translated_chest.append({'x': chest_translated[0], 'y': chest_translated[1], 'z': chest_translated[2]})
        translated_movingrobot.append({'x': movingrobot_translated[0], 'y': movingrobot_translated[1], 'z': movingrobot_translated[2]})
        translated_rightshoulder.append({'x': rightshoulder_translated[0], 'y': rightshoulder_translated[1], 'z': rightshoulder_translated[2]})
        translated_leftshoulder.append({'x': leftshoulder_translated[0], 'y': leftshoulder_translated[1], 'z': leftshoulder_translated[2]})
        translated_righthand.append({'x': righthand_translated[0], 'y': righthand_translated[1], 'z': righthand_translated[2]})
        translated_lefthand.append({'x': lefthand_translated[0], 'y': lefthand_translated[1], 'z': lefthand_translated[2]})
        translated_rightleg.append({'x': rightleg_translated[0], 'y': rightleg_translated[1], 'z': rightleg_translated[2]})
        translated_leftleg.append({'x': leftleg_translated[0], 'y': leftleg_translated[1], 'z': leftleg_translated[2]})

    # download_file(translated_chest, translated_righthand, translated_lefthand, translated_rightshoulder, translated_leftshoulder, translated_rightleg, translated_leftleg, translated_movingrobot, "translated")
    return translated_righthand, translated_lefthand, translated_rightshoulder, translated_leftshoulder, translated_chest, translated_rightleg, translated_movingrobot, translated_leftleg

def rotate_to_positive_x(RH, LH, RSH, LSH, CH, RL, MR, LL):
    rotated_leftshoulder = []
    rotated_movingrobot = []
    rotated_rightshoulder = []
    rotated_righthand = []
    rotated_lefthand = []
    rotated_chest = []
    rotated_rightleg = []
    rotated_leftleg = []

    for lsh, mr, rsh, rh, lh, ch, rl, ll in zip(LSH, MR, RSH, RH, LH, CH, RL, LL):
        Xlsh, Ylsh, Zlsh = lsh['x'], lsh['y'], lsh['z']
        Xmr, Ymr, Zmr = mr['x'], mr['y'], mr['z']
        Xrsh, Yrsh, Zrsh = rsh['x'], rsh['y'], rsh['z']
        Xrh, Yrh, Zrh = rh['x'], rh['y'], rh['z']
        Xlh, Ylh, Zlh = lh['x'], lh['y'], lh['z']
        Xch, Ych, Zch = ch['x'], ch['y'], ch['z']
        Xrl, Yrl, Zrl = rl['x'], rl['y'], rl['z']
        Xll, Yll, Zll = ll['x'], ll['y'], ll['z']
        
        angle = np.arctan2(Ymr, Xmr)
        # if angle < 0:
        #     angle += 2 * np.pi

        # Calculate the angle for rotation around the Z-axis using trigonometric identities
        # magnitude = math.sqrt(Xs**2 + Ys**2)
        # cos_angle = Xs / magnitude
        # angle = math.acos(cos_angle)
        # if Ys < 0:
        #     angle = 2 * math.pi - angle

        rotation_matrix = np.array([[np.cos(angle), np.sin(angle), 0, 0],
                                    [-np.sin(angle), np.cos(angle), 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]])
        rightshoulder_rotated = np.dot(rotation_matrix, np.array([Xrsh, Yrsh, Zrsh, 1]))
        leftshoulder_rotated = np.dot(rotation_matrix, np.array([Xlsh, Ylsh, Zlsh, 1]))
        righthand_rotated = np.dot(rotation_matrix, np.array([Xrh, Yrh, Zrh, 1]))
        lefthand_rotated = np.dot(rotation_matrix, np.array([Xlh, Ylh, Zlh, 1]))
        rightleg_rotated = np.dot(rotation_matrix, np.array([Xrl, Yrl, Zrl, 1]))
        leftleg_rotated = np.dot(rotation_matrix, np.array([Xll, Yll, Zll, 1]))
        movingrobot_rotated = np.dot(rotation_matrix, np.array([Xmr, Ymr, Zmr, 1]))

        rightshoulder_rotated[np.abs(rightshoulder_rotated) < 1e-10] = 0
        leftshoulder_rotated[np.abs(leftshoulder_rotated) < 1e-10] = 0
        righthand_rotated[np.abs(righthand_rotated) < 1e-10] = 0
        lefthand_rotated[np.abs(lefthand_rotated) < 1e-10] = 0
        rightleg_rotated[np.abs(rightleg_rotated) < 1e-10] = 0
        leftleg_rotated[np.abs(leftleg_rotated) < 1e-10] = 0
        movingrobot_rotated[np.abs(movingrobot_rotated) < 1e-10] = 0
        
        rotated_movingrobot.append({'x': movingrobot_rotated[0], 'y': movingrobot_rotated[1], 'z': movingrobot_rotated[2]})
        rotated_rightshoulder.append({'x': rightshoulder_rotated[0], 'y': rightshoulder_rotated[1], 'z': rightshoulder_rotated[2]})
        rotated_leftshoulder.append({'x': leftshoulder_rotated[0], 'y': leftshoulder_rotated[1], 'z': leftshoulder_rotated[2]})
        rotated_righthand.append({'x': righthand_rotated[0], 'y': righthand_rotated[1], 'z': righthand_rotated[2]})
        rotated_lefthand.append({'x': lefthand_rotated[0], 'y': lefthand_rotated[1], 'z': lefthand_rotated[2]})
        rotated_rightleg.append({'x': rightleg_rotated[0], 'y': rightleg_rotated[1], 'z': rightleg_rotated[2]})
        rotated_leftleg.append({'x': leftleg_rotated[0], 'y': leftleg_rotated[1], 'z': leftleg_rotated[2]})

    # download_file(rotated_chest, rotated_righthand, rotated_lefthand, rotated_rightshoulder, rotated_leftshoulder, rotated_rightleg, rotated_leftleg, rotated_movingrobot, "rotated")
    return rotated_righthand, rotated_lefthand, rotated_rightshoulder, rotated_leftshoulder, rotated_rightleg, rotated_movingrobot, rotated_leftleg

# if __name__ == "__main__":
    # righthand_translated, lefthand_translated, rightshoulder_translated, leftshoulder_translated, chest_translated, rightleg_translated, movingrobot_translated, leftleg_translated