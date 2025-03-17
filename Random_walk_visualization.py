import plotly.graph_objects as go

from random_walk import RandomWalk

#Creating a new random walk while the program remains active.
while True:
    #Preparing of random walk data.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Create the scatter plot.
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=rw.x_values, 
        y=rw.y_values, 
        mode='markers',
        marker=dict(size=2, color=list(range(rw.num_points)), colorscale='Viridis', opacity=0.6),
        name='Random walk'
    ))

    # Highlight the starting point and ending point.
    fig.add_trace(go.Scatter(
        x=[rw.x_values[0]], 
        y=[rw.y_values[0]], 
        mode='markers',
        marker=dict(size=10, color='red'),
        name='Start point'
    ))

    fig.add_trace(go.Scatter(
        x=[rw.x_values[-1]], 
        y=[rw.y_values[-1]], 
        mode='markers',
        marker=dict(size=10, color='blue'),
        name='End point'
    ))

    # Update layout.
    fig.update_layout(
        title='Random walk',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        showlegend=True,
        template='plotly_dark'
    )

    fig.write_html('Random_walk_visualization.html')

    keep_running = input("Create another random walk? (y/n):")
    if keep_running == 'n':
        break