import json
import plotly.graph_objects as go

# extract each punch to max distance

# Load data from JSON file
with open('data/transformed_data_93.json') as file:
    data = json.load(file)

# Extract left and right hand punch data
left_punches = data['leftHandPunches']
right_punches = data['rightHandPunches']

# Create a 3D scatter plot
fig = go.Figure()

# Function to add lines for each punch sequence
def add_punches(punch_data, hand, color):
    for session_id, punches in punch_data.items():
        # Check if the punch data is empty
        if not punches:
            continue  # Skip this punch sequence if it's empty
        x, y, z = [], [], []
        for punch in punches:
            x.append(punch['x'])
            y.append(punch['y'])
            z.append(punch['z'])
        # Add line trace for the punch sequence
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines',
            line=dict(color=color, width=2),
            name=f'{hand} P {session_id}'))
        # Add marker trace for the starting point of the punch sequence
        fig.add_trace(go.Scatter3d(x=[x[0]], y=[y[0]], z=[z[0]], mode='markers',
            marker=dict(size=0, color=color, symbol='circle'),
            name=f'{hand} Start {session_id}'))

# Add left and right hand punches to the plot
add_punches(left_punches, 'Left', 'blue')
add_punches(right_punches, 'Right', 'green')

# Update plot layout
fig.update_layout(
    title='3D Line Plot of Left and Right Hand Punches',
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis'
    ),
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
)

fig.show()
