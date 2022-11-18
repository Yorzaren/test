"""
1. Write out a Mathematica or C++ or Python or Java code  which takes as inputs two .g6 files "list.g6" and "minors.g6"
    and outputs two other files "with.g6" and "without.g6". The program checks all the graphs in list.g6 and
    selects those which have no minors in minors.g6 and outputs them to without.g6, and outputs the rest in with.g6.
    The program should have enough comments so that someone like me could understand the code.
"""

# Import libraries
import ast
from minorminer import find_embedding  # There's no reason to reinvent the wheel if there's already a library
# End import

# Start defining functions
def read_file_into_list(file_name):  # Example: graphs.txt
    with open(file_name, "r") as data_file:
        data = []  # Used to append during the reading
        for line in data_file:
            data.append(ast.literal_eval(line))  # Read in the lines correctly as a list
            # Must be interpreted correctly, or it will be cast as a string and will not work with minorminer.
        # End of for loop
    # End of the open file call

    ### DEBUGGING TEXT ###
    # Check that the list_of_graphs_to_check is a list
    #print("The value of data:")
    #print(data)

    # Check the type of list_of_graphs_to_check is a list
    #print("Check that data is a list: " + str(isinstance(data, list)))

    # Check that the things within are tuples
    #print("data[0][0]) is a tuple: " + str(isinstance(data[0][0], tuple)))

    if isinstance(data, list) == False or isinstance(data[0][0], tuple) == False:
        raise ValueError('DevMessage: The data wasnt read in correctly, check the debug text.')

    return data  # Return the data, so it can be assigned to a difference var later

def test_data():
    # Data from the minorminer page. A square graph is a minor of a triangle graph.
    list_of_graphs_to_check = read_file_into_list("squaregraphs.txt")
    list_of_minors = read_file_into_list("trianglegraphs.txt")

    square = list_of_graphs_to_check[0]
    square2 = list_of_graphs_to_check[1]
    triangle = list_of_minors[0]

    embedding = find_embedding(triangle, square)
    print("This should be 3: " + str(len(embedding)))  # 3, one set for each variable in the triangle
    embedding = find_embedding(triangle, square2)
    print("This should be 3: " + str(len(embedding)))  # 3, one set for each variable in the triangle


def sort_graphs(input_graphs_textfile, input_minors_textfile):
    list_of_graphs_to_check = read_file_into_list(input_graphs_textfile)
    list_of_minors = read_file_into_list(input_minors_textfile)
    list_of_graphs_with_minors = []
    list_of_graphs_with_no_minors = []

    for test_graph in list_of_graphs_to_check: # Loop through the test graphs
        #print("Test Graph: " + str(test_graph))
        for minor_graph in list_of_minors: # For each of the test graphs, run though the minors and test if it in there,
            #print("Test Minor: " + str(minor_graph))
            if len(find_embedding(minor_graph, test_graph)) > 0:
                #print(str(test_graph) + " is a minor of " + str(minor_graph))
                list_of_graphs_with_minors.append(test_graph)
            else:
                #print(str(test_graph) + " is a NOT minor of " + str(minor_graph))
                list_of_graphs_with_no_minors.append(test_graph)
        # END OF MINOR GRAPH FOR LOOP
    # END OF TEST GRAPH FOR LOOP


    print("list_of_graphs_with_minors:")
    print(list_of_graphs_with_minors)
    print("list_of_graphs_with_no_minors:")
    print(list_of_graphs_with_no_minors)


    # Write the output to the files
    with open(r'with.txt', 'w') as fp:
        for item in list_of_graphs_with_minors:
            # write each item on a new line
            fp.write("%s\n" % item)
    with open(r'without.txt', 'w') as fp:
        for item in list_of_graphs_with_no_minors:
            # write each item on a new line
            fp.write("%s\n" % item)
    # END file write


# Run once in main
if __name__ == '__main__':
    #test_data()
    #sort_graphs("squaregraphs.txt", "trianglegraphs.txt")
    sort_graphs("squaregraphs.txt", "graphb.txt")






#
#test = [[(0, 1), (0, 2), (1, 3), (2, 3)], [(0, 1), (1, 2), (2, 3), (3, 0)]]
#print(type(test[0][0][0]))