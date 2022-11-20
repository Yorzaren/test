"""

    USE: sort_graphs(input_graphs_textfile, input_minors_textfile)

    Code takes in .txt files to test


    Graphs are written in the form of [(0,1),(1,2),(2,3)] which would correspond to a triangle shapes graph
    To have multiple graphs in a file separate them with a single line break DONT add a comma to the end of the line

    SEE: squaregraphs.txt and mixedtest.txt

    The output is written into two files:
     - "with.txt" (graphs that have a minor in the given input file)
     - "without.txt" (graphs without a minor in the given input file)
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


"""
Note: Only test_data() call if you suspect there to be an issue with the file read in.
"""


def test_data():
    # Data from the minorminer page. A square graph is a minor of a triangle graph.
    list_of_graphs_to_check = read_file_into_list("Graphs/squaregraphs.txt")
    list_of_minors = read_file_into_list("Graphs/trianglegraphs.txt")

    square = list_of_graphs_to_check[0]
    square2 = list_of_graphs_to_check[1]
    triangle = list_of_minors[0]

    embedding = find_embedding(triangle, square)
    print("This should be 3: " + str(len(embedding)))  # 3, one set for each variable in the triangle
    embedding = find_embedding(triangle, square2)
    print("This should also be 3: " + str(len(embedding)))  # 3, one set for each variable in the triangle


def sort_graphs(input_graphs_textfile, input_minors_textfile, output_with_file='with.txt', output_without_file='without.txt'):
    # Without the output_with_file or output_without_file specified it will default to those values
    list_of_graphs_to_check = read_file_into_list(input_graphs_textfile)
    list_of_minors = read_file_into_list(input_minors_textfile)
    list_of_graphs_with_minors = []
    list_of_graphs_with_no_minors = []

    for test_graph in list_of_graphs_to_check:  # Loop through the test graphs
        #print("Test Graph: " + str(test_graph))
        for minor_graph in list_of_minors: # For each of the test graphs, run through the minors and test if its in there.
            #print("Test Minor: " + str(minor_graph))
            if len(find_embedding(minor_graph, test_graph)) > 0:
                #print(str(test_graph) + " is a minor of " + str(minor_graph))
                list_of_graphs_with_minors.append(test_graph)  # Add it to the list
                list_of_graphs_to_check.remove(test_graph)  # Then remove it because there's no reason to check it again
        # END OF MINOR GRAPH FOR LOOP
    # END OF TEST GRAPH FOR LOOP

    # The remaining graphs in the list DON'T have minors
    for graph in list_of_graphs_to_check:
        list_of_graphs_with_no_minors.append(graph)
    # END OF FOR LOOP

    print("list_of_graphs_with_minors:")
    print(list_of_graphs_with_minors)
    print("list_of_graphs_with_no_minors:")
    print(list_of_graphs_with_no_minors)

    # Write the output to the files
    with open(output_with_file, 'w') as fp:
        for item in list_of_graphs_with_minors:
            fp.write("%s\n" % item)  # Each item printed onto a newline
    with open(output_without_file, 'w') as fp:
        for item in list_of_graphs_with_no_minors:
            fp.write("%s\n" % item)
    # END file write
    print("Graph sorting has finished.\nInputs were input_graphs_textfile: " + input_graphs_textfile
          + " and input_minors_textfile: " + input_minors_textfile +
          "\nCheck: " + output_with_file + " and " + output_without_file)


# Main method
if __name__ == '__main__':
    # Just keep this here because it throws error when everything is commented out
    print("Main Method of main.py reached")

    # Reminder don't run all of these at the same time bc the output files are the same and will be overriden
    # by the last call.


    # Command sort_graphs(input_graphs_textfile, input_minors_textfile)
    sort_graphs("Graphs/squaregraphs.txt", "Graphs/trianglegraphs.txt")
    # A square graph has a minor of a triangle so both graphs should be in the with.txt

    #sort_graphs("Graphs/squaregraphs.txt", "Graphs/graphb.txt")
    # Square graphs aren't a minor of a k5 with 3 more edges. Both graphs should be in the without.txt

    #sort_graphs("Graphs/mixedtest.txt", "Graphs/k5.txt")
    # Mixed test contains two square and a k5 with 3 more edges
    # So the graph with a corresponding minor is the k5 with 3 more edges, both squares should be in the without.

    #sort_graphs("Graphs/mixedtest2.txt", "Graphs/forbidden_minors_planar_graphs.txt")
    # Contains a point, line, triangle, graphb, k2,3, k3,3.
    # So there's only two graphs with a forbidden minor: graphb a k5 with 3 more edge and k3,3.
