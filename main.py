import networkx as nx
import matplotlib.pyplot as plt

class Info_about_vertex:
    сonnect_with_nodes = [] # Stores information about which nodes a particular node is associated with
    edge_weights = []       # The matrix of weights
    start_vertex = 0        # Stores information about the starting vertex
    order_of_the_graph = 0  # Stores information about the order of the graph

    def __init__(self, сonnection_with_nodes, edge_weights, start_vertex, order_of_the_graph):
        self.сonnection_with_nodes = сonnection_with_nodes
        self.edge_weights = edge_weights
        self.start_vertex = start_vertex
        self.order_of_the_graph = order_of_the_graph

    def print_info(self):
        print("Connection with nodes: ", self.сonnection_with_nodes)
        print("Edge weights: ", self.edge_weights)
        print("Start vertex: ", self.start_vertex)
        print("Order of the graph: ", self.order_of_the_graph)

def work_with_file():
    file = open("input.in", "r")
    lines = file.readlines()
    file.close()
    return lines

def parsing_weights(lines):
    matrix_of_weights = []
    string_of_weights = []

    # To skip the first line
    helper = lines[0]
    lines.pop(0)

    for line in lines:
        string_of_weights.append(line.split())

    for elem in string_of_weights:
        for i in range(0, len(string_of_weights)):
            if elem[i] == '*':
                elem[i] = 0
            elem[i] = int(elem[i])
        matrix_of_weights.append(elem)
        #print(matrix_of_weights)
    #print(matrix_of_weights)
    lines.insert(0, helper)
    return matrix_of_weights

def parsing_starting_vertex(lines):
    helper = lines[0]
    helper = helper.split()
    starting_vertex = int(helper[1])
    #print(starting_vertex)
    return starting_vertex

def parsing_order_of_the_graph(lines):
    helper = lines[0]
    helper = helper.split()
    order = int(helper[0])
    #print(order)
    return order

def connection_nodes(matrix_of_weights):
    connect_nodes = []
    helper = []

    for  i in range(0, len(matrix_of_weights)):
        for j in range(0, len(matrix_of_weights)):
            if matrix_of_weights[i][j] != 0:
                helper.append(j)
        connect_nodes.append(helper)
        helper = []
    return connect_nodes
    #print(connect_nodes)
#In progress
def bellman_ford(сonnect_nodes, matrix_of_weights,  starting_vertex, order):
    D = [0] * order # The sum of the weights
    P = [0] * order   # Which node did we come from (Penultimate node)
    #print(D)
    #print(P)
    D[starting_vertex - 1] = 0
    P[starting_vertex - 1] = 1

    for step in range(1, order + 1):
        print('Step -', step)
        for i in range(0, step):
            for j in range(0, len(сonnect_nodes[i])):
                print(сonnect_nodes[starting_vertex - 1][j])
                D[сonnect_nodes[starting_vertex - 1][j]] = matrix_of_weights[сonnect_nodes[starting_vertex - 1][j]][i]

        print(D)
        print(P)
        pass

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

    GInfo = Info_about_vertex(connection_nodes(matrix_of_weights), matrix_of_weights, parsing_starting_vertex(lines), parsing_order_of_the_graph(lines))
    GInfo.print_info()
    #bellman_ford(GInfo.сonnection_with_nodes, GInfo.edge_weights, GInfo.start_vertex, GInfo.order_of_the_graph)
