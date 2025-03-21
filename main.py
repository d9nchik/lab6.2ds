def get_data():
    data = []
    with open("input.txt") as iFile:
        while True:
            line = iFile.readline()
            if not line:
                break
            temp = list(map(int, (line[:len(line)] + line[len(line) + 1:]).split()))
            data.append(temp)
    return data


def create_adjacency_matrix(idata):
    matrix = [0] * idata[0][0]
    for x in range(idata[0][0]):
        matrix[x] = [0] * idata[0][0]

    for y in range(1, len(idata)):
        matrix[idata[y][0] - 1][idata[y][1] - 1] = 1
        matrix[idata[y][1] - 1][idata[y][0] - 1] = 1
    return matrix


def get_power_matrix(adjacency_matrix):
    matrix_of_power = []
    for x in range(len(adjacency_matrix)):
        total = 0
        for y in range(len(adjacency_matrix)):
            total += adjacency_matrix[x][y]
        matrix_of_power.append(total)
    return matrix_of_power


def get_maximum_index(colour_of_nodes, matrix_power):
    max_index = -1
    maximum = -1
    for x in range(len(matrix_power)):
        if colour_of_nodes[x] == -1 and matrix_power[x] > maximum:
            maximum = matrix_power[x]
            max_index = x
    return max_index


def colour_graph(adjacency_matrix):
    colour_of_nodes = [-1] * len(adjacency_matrix)
    counter = 1
    matrix_power = get_power_matrix(adjacency_matrix)
    maximum_index = get_maximum_index(colour_of_nodes, matrix_power)
    while maximum_index != -1:
        will_be_coloured = [maximum_index]
        unvisited = True
        while unvisited:
            unvisited = False
            colour_of_nodes[will_be_coloured[-1]] = counter
            for x in range(len(adjacency_matrix)):
                if colour_of_nodes[x] == -1:
                    unvisited = True
                    for y in will_be_coloured:
                        if adjacency_matrix[x][y] == 1:
                            unvisited = False
                            break
                    if unvisited:
                        will_be_coloured.append(x)
                        break
        counter += 1
        maximum_index = get_maximum_index(colour_of_nodes, matrix_power)
    return colour_of_nodes


def show_coloured_graph(colour):
    maximum = max(colour)
    for x in range(1, maximum + 1):
        print("Колір %d" % x, end=": ")
        for y in range(len(colour)):
            if colour[y] == x:
                print(y + 1, end=", ")
        print()


show_coloured_graph(colour_graph(create_adjacency_matrix(get_data())))
