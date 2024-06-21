import json
import plotly.graph_objects as go
import plotly.subplots as sp
import numpy as np

# Function to read JSON data
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def print_statistics(label, x, y, z):
    average_x = round(np.average(x), 2)
    average_y = round(np.average(y), 2)
    average_z = round(np.average(z), 2)
    std_x = round(np.std(x), 2)
    std_y = round(np.std(y), 2)
    std_z = round(np.std(z), 2)
    stats = {
        'label': label,
        'avg_x': average_x,
        'avg_y': average_y,
        'avg_z': average_z,
        'std_x': std_x,
        'std_y': std_y,
        'std_z': std_z
    }
    return stats

def downsample(data, factor):
    return data[::factor]

# Function to plot the 3D line plot
def plot_3d_data(data, file_path):
    fig = sp.make_subplots(
        rows=2, cols=2,
        column_widths=[0.65, 0.35],
        row_heights=[0.55, 0.45],
        subplot_titles=(f"{file_path}: 3D Visualization", "Body Poistion Information", "Distance Information"),
        specs=[[{'type': 'scatter3d', "rowspan": 2}, {'type': 'table'}],
                [            None                    , {"type": "table"}]]
    )

    # Helper function to extract coordinates from the list of dictionaries
    def extract_coordinates(items):
        x = [item['x'] for item in items]
        y = [item['y'] for item in items]
        z = [item['z'] for item in items]
        return x, y, z

    # Plotting each category with different colors
    def add_trace(label, color, coordinates):
        x, y, z = extract_coordinates(coordinates)
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', name=label, line=dict(color=color)))
        stats.append(print_statistics(label, x, y, z))

    stats = []
    add_trace('chest', 'red', data['chest'])
    add_trace('Right Hand', 'green', data['righthand'])
    add_trace('Left Hand', 'blue', data['lefthand'])
    # add_trace('Right Shoulder', 'orange', data['rightshoulder'])
    # add_trace('Left Shoulder', 'yellow', data['leftshoulder'])
    # add_trace('Right Leg', 'purple', data['rightleg'])
    # add_trace('Left Leg', 'gray', data['leftleg'])
    add_trace('Moving Robot', 'brown', data['movingrobot'])

    # Prepare table data for the statistics
    sta_table_header = ['Body Part', 'Avg X', 'Avg Y', 'Avg Z', 'Std X', 'Std Y', 'Std Z']
    sta_table_cells = [
        [stat['label'] for stat in stats],
        [stat['avg_x'] for stat in stats],
        [stat['avg_y'] for stat in stats],
        [stat['avg_z'] for stat in stats],
        [stat['std_x'] for stat in stats],
        [stat['std_y'] for stat in stats],
        [stat['std_z'] for stat in stats]
    ]

    # Add table to the second subplot
    fig.add_trace(
        go.Table(
            columnwidth = [250,130,130,130,130,130,130],
            header=dict(
                values=sta_table_header, 
                fill_color='#474342', 
                align=['center', 'center'], 
                height= 50, 
                font= dict(color= 'white')),
            cells=dict(
                values=sta_table_cells, 
                fill_color='#dbdfdf', 
                align=['center', 'center'], 
                height= 30)
        ),
        row=1, col=2
    )

    dis_table_header = ['Total Movement', 'Result']
    dis_table_cells = [
        ['Total Movement (m)', 'Ave. Distance Between Boxer (m)', '👊Left Hand Similarity', 
         'Right Hand Similarity👊', '👊LH Average Movement (m)', 'RH Average Movement👊 (m)'],
        [round(data['movementDistanceSum'], 3), round(data['chestDistanceAverage'], 3), round(data['leftHandSimilarity'], 3), 
         round(data['rightHandSimilarity'], 3), round(data['lhMovementDistanceSum'], 3), round(data['rhMovementDistanceSum'], 3)]
    ]

    fig.add_trace(
        go.Table(
            header=dict(
                values=dis_table_header, 
                fill_color='#34364B', 
                align='center', 
                height= 30, 
                font= dict(color= 'white')),
            cells=dict(
                values=dis_table_cells, 
                fill_color='#dbdfdf', 
                align='center', 
                height= 30)
        ),
        row=2, col=2
    )

    # Labeling axes
    fig.update_layout(
        scene=dict(
            xaxis_title='X Coordinate',
            yaxis_title='Y Coordinate',
            zaxis_title='Z Coordinate',
            aspectmode='cube'
        ),
        legend=dict(
            yanchor="top", 
            y=0.8,
            xanchor="right", 
            x=0.6, 
        )
    )

    # Showing the plot
    fig.show()

    # Saving the plot to a file (optional)
    # fig.write_image("3d_plot.png")

def write_visualization(path):
    file_path = path
    data = read_json(file_path)

    # downsample_factor = 10
    # data['chest'] = downsample(data['chest'], downsample_factor)
    # data['righthand'] = downsample(data['righthand'], downsample_factor)
    # data['lefthand'] = downsample(data['lefthand'], downsample_factor)
    # data['rightshoulder'] = downsample(data['rightshoulder'], downsample_factor)
    # data['leftshoulder'] = downsample(data['leftshoulder'], downsample_factor)
    # data['rightleg'] = downsample(data['rightleg'], downsample_factor)
    # data['leftleg'] = downsample(data['leftleg'], downsample_factor)
    # data['movingrobot'] = downsample(data['movingrobot'], downsample_factor)

    plot_3d_data(data, file_path)


# Example usage
if __name__ == '__main__':
    # Adjust the path to your JSON file
    file_path = 'data/user_4_9.json'
    data = read_json(file_path)

    # RH, LH, RSH, LSH, CH, RL, LL, MR (A, B, C, D, E, F, G, H)

    downsample_factor = 10  # Adjust this factor based on your data size and desired performance
    data['chest'] = downsample(data['chest'], downsample_factor)
    data['righthand'] = downsample(data['righthand'], downsample_factor)
    data['lefthand'] = downsample(data['lefthand'], downsample_factor)
    # data['rightshoulder'] = downsample(data['rightshoulder'], downsample_factor)
    # data['leftshoulder'] = downsample(data['leftshoulder'], downsample_factor)
    # data['rightleg'] = downsample(data['rightleg'], downsample_factor)
    # data['leftleg'] = downsample(data['leftleg'], downsample_factor)
    data['movingrobot'] = downsample(data['movingrobot'], downsample_factor)

    plot_3d_data(data)
