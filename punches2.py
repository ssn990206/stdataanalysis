import json
import plotly.graph_objects as go

# extract each punch

# Load data from JSON file
with open('data/transformed_data_911.json') as file:
    data = json.load(file)

# Initialize figure
fig = go.Figure()

# avatarPunchData and data extraction
avatar_punch_data = data['avatarPunchData']
righthand_data = data['righthand']
lefthand_data = data['lefthand']

# Variable to track the current index
current_index = 0

# Process data based on avatarPunchData
for punch_type in avatar_punch_data:
    x, y, z = [], [], []
    # Determine the data source based on punch type
    if punch_type == 1:
        data_source = righthand_data
    else:
        data_source = lefthand_data

    # Extract 50 data points from the current index
    for i in range(current_index, current_index + 50):
        x.append(data_source[i]['x'])
        y.append(data_source[i]['y'])
        z.append(data_source[i]['z'])

    # Add the trace to the figure
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines+markers', 
        marker=dict(size=0),
        line=dict(color='green' if punch_type == 1 else 'blue'),
        name=f'{"RH" if punch_type == 1 else "LH"} {current_index}-{current_index + 49}'))

    # Update the current index
    current_index += 50

# Update plot layout
fig.update_layout(
    title='3D Line Plot of Hand Punches Based on avatarPunchData',
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis'
    ),
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
)

fig.show()
