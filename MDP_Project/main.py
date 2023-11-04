# MDP Assignment - 210413G
def get_utilities(epsilon, initial_values):
    # Define a discount factor for future rewards.
    discount = 0.999
    # Temporary variable for future use.
    temp = True
    # Create a 2x3 grid initialized with zeros.
    grid = [[0 for _ in range(3)] for _ in range(2)]

    # Perform 100 iterations of the value iteration algorithm.
    for i in range(100):
        # Initialize the number of iterations.
        iterations = 0
        # Create a copy of the current grid for simultaneous updates.
        grid_copy = grid[:]

        # Loop through each state in the grid.
        for i in range(2):
            for j in range(3):
                # If the state has a value of 0, set it to the initial value.
                if grid[i][j] == 0:
                    grid[i][j] = initial_values[i][j]
                else:
                    # Calculate the expected utilities of different actions (North, South, West, East, and Do Nothing).
                    north = grid[i - 1][j] if i > 0 else grid[i][j]
                    south = grid[i + 1][j] if i < len(grid) - 1 else grid[i][j]
                    west = grid[i][j - 1] if j > 0 else grid[i][j]
                    east = grid[i][j + 1] if j < len(grid[0]) - 1 else grid[i][j]
                    do_nothing = grid[i][j]

                    # print(f"State: ({i}, {j})")
                    # print(f"North: {north}")
                    # print(f"South: {south}")
                    # print(f"West: {west}")
                    # print(f"East: {east}")
                    # print(f"Do Nothing: {do_nothing}")

                    # Create a dictionary to store combinations of actions.
                    combinations = {
                        north: (west, east),
                        south: (west, east),
                        west: (north, south),
                        east: (north, south)
                    }
                    temp_vals = []

                    # Calculate the expected utility for each action.
                    for action in [north, south, west, east, do_nothing]:
                        if action is do_nothing:
                            temp_vals.append(do_nothing)
                        else:
                            random_choices = combinations[action]
                            random_choices_values = 0.05 * (grid[i][j] + discount * random_choices[0]) + 0.05 * (
                                    grid[i][j] + discount * random_choices[1])
                            val = 0.9 * (grid[i][j] + discount * action) + random_choices_values

                            # Ensure the utility value does not exceed 1.
                            if val > 1:
                                temp_vals.append(grid[i][j])
                            else:
                                temp_vals.append(val)

                    # Find the best utility among the available actions.
                    best_utility = max(temp_vals)
                    # Check if the change in utility is below the specified epsilon threshold.
                    if grid[i][j] - best_utility > epsilon:
                        # Return the current grid and the number of iterations if the threshold is met.
                        return (grid, iterations)

                    # Update the copy of the grid with the best utility value.
                    grid_copy[i][j] = best_utility
                    iterations += 1

        # Update the original grid with the values from the copy for the next iteration.
        grid = grid_copy

    # Return the final grid of utility values and the total number of iterations.
    return grid, iterations

# Set the epsilon threshold and initial values for the grid.
epsilon = 0.01
initial_values = [[-0.1, -0.1, -0.05], [-0.1, -0.1, 1]]
# Call the get_utilities function to compute the utilities for the grid.
final_state_utilities, iterations = get_utilities(epsilon, initial_values)

# Print the final state utilities and the number of iterations.
print(final_state_utilities)
print(iterations)
