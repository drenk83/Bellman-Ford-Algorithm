import networkx as nx
import matplotlib.pyplot as plt

def work_with_file():
    file = open("input.in", "r")
    lines = file.readlines()
    file.close()
    return lines

def parsing_weights(lines):
    matrix_of_weights = []

    # To skip the first line
    helper = lines[0]
    lines.pop(0)

    for line in lines:
        matrix_of_weights.append(line.split())

    #print(matrix_of_weights)
    lines.insert(0, helper)
    return matrix_of_weights

def parsing_starting_vertex(lines):
    helper = lines[0]
    helper = helper.split()
    starting_vertex = int(helper[1])
    #print(starting_vertex)
    return starting_vertex

def work_with_visualization():
    G = nx.DiGraph(directed = True)
    #G = nx.Graph()
    print(G)

    for i in range(0, 10):
        G.add_node(i)

    print(G)

    for i in range(0, 10):
        if i < 9:
            G.add_edge(i, i + 1, weight = 1)
        else:
            G.add_edge(i, 0, weight = 1)

    print(G)

    # set layout
    pos = nx.circular_layout(G)

    nx.draw(G, pos, with_labels = True)
    plt.show()

if __name__ == "__main__":
    lines = work_with_file()
    print(lines)
    #work_with_visualization()
    matrix_of_weights = parsing_weights(lines)
    starting_vertex = parsing_starting_vertex(lines)
    print(lines)
