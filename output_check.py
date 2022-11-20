"""

Used to glance and check the output

"""
import networkx as nx  # Use to convert g6 into a list of points
import matplotlib.pyplot as plt


def readfile(file_name):  # Example: graphs.g6
    with open(file_name, "r") as data_file:
        data = []  # Used to append during the reading
        for line in data_file:
            data.append(line.replace('\n', ''))  # Read in the lines correctly as a list
        # End of for loop
    # End of the open file call
    return data  # Return data which should be an array of g6 bits


def get_num_edges(g6_graph):
    return int(str(g6_graph).rpartition(' edges')[0].split('and ')[1])


def info_graph(graph_data,  show_graph=False):
    g6_graph_bytes = bytes(graph_data, 'utf8')  # Convert into bytes to use nx.from_graph6_bytes
    g6_graph = nx.from_graph6_bytes(g6_graph_bytes)
    if get_num_edges(g6_graph) >= 5:  # Change this to reflect things logically
        print(g6_graph)
        if show_graph:
            plt.title(graph_data)
            nx.draw(g6_graph, with_labels=True, font_weight='bold')
            plt.show()

def loop(file, show_graph=False):
    test = readfile(file)
    for x in test:
        info_graph(x, show_graph=show_graph)


if __name__ == '__main__':
    #test = readfile("with.txt")
    #loop("without.txt", show_graph=True)
    loop("with.txt", show_graph=True)
    #loop("k3,3.g6", show_graph=True)

    #info_graph("FCXjW", show_graph=True)
    #info_graph("ETmw", show_graph=True)