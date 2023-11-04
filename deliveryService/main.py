# Assignment Implement - Hill Climb Algorithm - Courier Service problem.
# Introduction to AI. 210413G.
import numpy as np


# reading input file
def readFile(matrix, trucks):
    certainword = "truck"
    with open('input.txt', 'r') as File:
        for line in File:
            # splitting matrix and trucks
            if line.strip().startswith(certainword):
                parts = line.split('#')
                trucks.append([parts[0], int(parts[1])])
            else:
                elements = line.strip().split(',')

                # Replace 'N' with float('inf') and convert other elements to integers
                row = [float('inf') if element == 'N' else int(element) for element in elements]
                # Append the row to the matrix
                matrix.append(row)


def dijkstra(matrix):
    n = len(matrix)
    shortest_distances = np.array(matrix)  # Initialize the shortest_distances matrix with the input matrix
    np.fill_diagonal(shortest_distances, 0)  # Set the diagonal elements to 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if shortest_distances[i][j] > shortest_distances[i][k] + shortest_distances[k][j]:
                    shortest_distances[i][j] = shortest_distances[i][k] + shortest_distances[k][j]

    return shortest_distances


# calculate total distance traveled by all truck in list
def calculate_total_distance(trucks, permutation, shortest_path_matrix):
    total_distance = 0
    iterator = 0    # iterator to travel through list
    for truck in trucks:
        initial = 0
        for _ in range(truck[1]):
            total_distance += shortest_path_matrix[initial][permutation[iterator]]
            initial = permutation[iterator]
            iterator += 1
    return total_distance


def hillclimb_algorithm(trucks, shortest_path_matrix):
    node_list = [i for i in range(1, len(shortest_path_matrix))]
    current_permutation = np.random.permutation(node_list)   # choose a random starting combination
    current_distance = calculate_total_distance(trucks, current_permutation, shortest_path_matrix)

    # do fix amount of iterations and find the optimum. may be local optimum
    for m in range(1000): 
        neighbor_permutation = np.random.permutation(node_list)
        neighbor_distance = calculate_total_distance(trucks, neighbor_permutation, shortest_path_matrix)

        if neighbor_distance < current_distance:    # replacing previous solution if better one is met
            current_permutation = neighbor_permutation
            current_distance = neighbor_distance

    return [current_distance, current_permutation]


# convert integer to lowercase
def int_to_lowercase_letter(n):
    if 0 <= n < 26:
        return chr(ord('a') + n)
    else:
        return None  # Handle out-of-range values


# write the output to a list
def write_to_file(output_list, trucks):
    with open("210413G.txt", "w") as file:

        iterator = 0
        for truck in trucks:
            string1 = truck[0] + "#"
            for i in range(truck[1]):
                string1 = string1 + "," + int_to_lowercase_letter(output_list[1][iterator])
                iterator = iterator + 1

            # removing comma after #
            index = string1.find('#')  # Find the index of '#'
            if index != -1 and index < len(string1) - 1:
                string1 = string1[:index + 1] + string1[index + 2:]
            
            file.write(string1 + "\n")
        file.write(str(int(output_list[0])))


if __name__ == '__main__':
    matrix = []
    trucks = []

    readFile(matrix, trucks)
    shortest_path_matrix = dijkstra(matrix)

    output_list = (hillclimb_algorithm(trucks, shortest_path_matrix))
    write_to_file(output_list, trucks)
    