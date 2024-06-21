import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# THIS IS FOR DATA COLLECTION FROM RAW DATA

def read_json():
    file_name = input()
    file_path = "data/user_5_" + file_name + ".json"
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to extract coordinates from TrackerPositions based on TrackerIndex
def extract_coordinates(data, index):
    for tracker in data['VTrackerDatas']:
        if tracker['TrackerIndex'] == index:
            positions = tracker['TrackerPositions']
            x = [pos['x']* -1 for pos in positions]
            z = [pos['y'] for pos in positions] 
            y = [pos['z']* -1 for pos in positions]
            return x, y, z
    return [], [], []

def print_statistics(label, x, y, z):
    average_x = round(np.average(x), 2)
    average_y = round(np.average(y), 2)
    average_z = round(np.average(z), 2)
    std_x = round(np.std(x), 2)
    std_y = round(np.std(y), 2)
    std_z = round(np.std(z), 2)
    print(f"{label}: Avg({average_x}, {average_y}, {average_z}), StdDev({std_x}, {std_y}, {std_z})")


# Function to plot the 3D scatter plot
def plot_3d_data(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xticks([0,3])
    ax.set_yticks([-3,0])
    ax.set_zticks([-3,0])
    # 0-3,0--3,0--3

    
    # Plotting each category with different colors
    A_x, A_y, A_z = extract_coordinates(data, "RS")
    B_x, B_y, B_z = extract_coordinates(data, "LS")
    C_x, C_y, C_z = extract_coordinates(data, "RE")
    D_x, D_y, D_z = extract_coordinates(data, "LE")
    E_x, E_y, E_z = extract_coordinates(data, "RK")
    F_x, F_y, F_z = extract_coordinates(data, "LK")
    G_x, G_y, G_z = extract_coordinates(data, "RF")
    H_x, H_y, H_z = extract_coordinates(data, "LF")
    I_x, I_y, I_z = extract_coordinates(data, "CH")


    ax.plot3D(A_x, A_y, A_z, c='blue', label='A', alpha= 0.8)
    ax.plot3D(B_x, B_y, B_z, c='brown', label='B', alpha= 0.8)
    ax.plot3D(C_x, C_y, C_z, c='green', label='C', alpha= 0.8)
    ax.plot3D(D_x, D_y, D_z, c='orange', label='D', alpha= 0.8)
    ax.plot3D(E_x, E_y, E_z, c='yellow', label='E', alpha= 0.8)
    ax.plot3D(F_x, F_y, F_z, c='red', label='F', alpha= 0.8)
    ax.plot3D(G_x, G_y, G_z, c='purple', label='G', alpha= 0.8)
    ax.plot3D(H_x, H_y, H_z, c='gray', label='H', alpha= 0.8)
    ax.plot3D(I_x, I_y, I_z, c='pink', label='I', alpha= 0.8)

    # LSH, MR, RSH, RH, LH, CH, RL, LL

    print_statistics("A", A_x, A_y, A_z)
    print_statistics("B", B_x, B_y, B_z)
    print_statistics("C", C_x, C_y, C_z)
    print_statistics("D", D_x, D_y, D_z)
    print_statistics("E", E_x, E_y, E_z)
    print_statistics("F", F_x, F_y, F_z)
    print_statistics("G", G_x, G_y, G_z)
    print_statistics("H", H_x, H_y, H_z)
    print_statistics("I", I_x, I_y, I_z)

    # Labeling axes
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Z Coordinate')

    # Adding a legend
    ax.legend()

    # Showing the plot
    plt.show()

    # Saving the plot to a file
    # fig.savefig('3d_plot.png')

# 3_2 V Tpose
# 3_3 V 繞著但有跑
# 3_5 V 繞著
# 3_7 V 亂跑
# 3_8 V 繞著拳擊手
# Example usage
if __name__ == '__main__':
    # Adjust the path to your JSON file
    file_path = 'data/user_5_2.json'
    data = read_json()
    plot_3d_data(data)
