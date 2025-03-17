from random import choice

class RandomWalk():
    """A class designed to generate a random walk."""

    def __init__(self, num_points=5000):
        """Initialization of random walk attributes."""
        self.num_points = num_points

        #The starting point has coordinates (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determining the direction and distance to cover in that direction and preparing the step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
    
    def fill_walk(self):
        """Generating all points for a random walk."""

        #Carrying out the steps until you reach the expected number of points.
        while len(self.x_values) < self.num_points:

            #Determining the direction and distance to cover in that direction..
            x_step = self.get_step()
            y_step = self.get_step()

            #Rejecting moves that lead nowhere.
            if x_step ==0 and y_step == 0:
                continue

            #Determining the next X and Y values.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)