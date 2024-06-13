import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def read_json():
    file_name = input()
    file_path = "data/transformed_data_5" + file_name + ".json"
    with open(file_path, 'r') as file:
        return json.load(file)
    
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
    # ax.set_xticks([0,3])
    # ax.set_yticks([-3,0])
    # ax.set_zticks([-3,0])

    # Helper function to extract coordinates from the list of dictionaries
    def extract_coordinates(items):
        x = [item['x'] for item in items]
        y = [item['y'] for item in items]
        z = [item['z'] for item in items]
        return x, y, z

    # Plotting each category with different colors
    chest_x, chest_y, chest_z = extract_coordinates(data['chest'])
    righthand_x, righthand_y, righthand_z = extract_coordinates(data['righthand'])
    lefthand_x, lefthand_y, lefthand_z = extract_coordinates(data['lefthand'])
    rightshoulder_x, rightshoulder_y, rightshoulder_z = extract_coordinates(data['rightshoulder'])
    leftshoulder_x, leftshoulder_y, leftshoulder_z = extract_coordinates(data['leftshoulder'])
    rightleg_x, rightleg_y, rightleg_z = extract_coordinates(data['rightleg'])
    leftleg_x, leftleg_y, leftleg_z = extract_coordinates(data['leftleg'])
    movingrobot_x, movingrobot_y, movingrobot_z = extract_coordinates(data['movingrobot'])

    # print(np.average(sandbag_x))

    ax.plot3D(chest_x, chest_y, chest_z, c='red', label='chest', alpha= 0.8)
    ax.plot3D(righthand_x, righthand_y, righthand_z, c='orange', label='Right Hand', alpha= 0.8)
    ax.plot3D(lefthand_x, lefthand_y, lefthand_z, c='yellow', label='Left Hand', alpha= 0.8)
    ax.plot3D(rightshoulder_x, rightshoulder_y, rightshoulder_z, c='green', label='Right Shoulder', alpha= 0.8)
    ax.plot3D(leftshoulder_x, leftshoulder_y, leftshoulder_z, c='blue', label='Left Shoulder', alpha= 0.8)
    ax.plot3D(rightleg_x, rightleg_y, rightleg_z, c='purple', label='Right Leg', alpha= 0.8)
    # ax.plot3D(leftleg_x, leftleg_y, leftleg_z, c='gray', label='Left Leg', alpha= 0.8)
    ax.plot3D(movingrobot_x, movingrobot_y, movingrobot_z, c='brown', label='Sandbag', alpha= 0.8)

    print_statistics("chest", chest_x, chest_y, chest_z)
    print_statistics("righthand", righthand_x, righthand_y, righthand_z)
    print_statistics("lefthand", lefthand_x, lefthand_y, lefthand_z)
    print_statistics("rightshoulder", rightshoulder_x, rightshoulder_y, rightshoulder_z)
    print_statistics("leftshoulder", leftshoulder_x, leftshoulder_y, leftshoulder_z)
    print_statistics("rightleg", rightleg_x, rightleg_y, rightleg_z)
    print_statistics("leftleg", leftleg_x, leftleg_y, leftleg_z)
    print_statistics("movingrobot", movingrobot_x, movingrobot_y, movingrobot_z)

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

# Example usage
if __name__ == '__main__':
    # Adjust the path to your JSON file
    # file_path = 'data/origin.json'
    # file_path = 'data/translated.json'
    # file_path = 'data/rotated.json'
    # file_path = 'data/transformed_data_52.json'
    data = read_json()
    plot_3d_data(data)
