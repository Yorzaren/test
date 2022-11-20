"""

    USE: sort_graphs(input_graphs_textfile, input_minors_textfile)

    Code takes in .g6 files to test


    Graphs are written in the g6 format which is compressed as a text string
    We use networkx to decode them into form looking something like [(0,1),(1,2),(2,3)]
    which can be used by minorminer.


    The output is written into two files:
     - "with.g6" (graphs that have a minor in the given input file)
     - "without.g6" (graphs without a minor in the given input file)
"""

# Import libraries
from minorminer import find_embedding  # There's no reason to reinvent the wheel if there's already a library
import networkx as nx  # Use to convert g6 into a list of points
# End import


# Start defining functions
def read_file_into_g6_list(file_name):  # Example: graphs.g6
    with open(file_name, "r") as data_file:
        data = []  # Used to append during the reading
        for line in data_file:
            data.append(line.replace('\n', ''))  # Read in the lines correctly as a list
        # End of for loop
    # End of the open file call
    return data  # Return data which should be an array of g6 bits


def sort_graphs(input_graphs_textfile, input_minors_textfile, output_with_file='with.g6', output_without_file='without.g6'):
    # Without the output_with_file or output_without_file specified it will default to those values
    list_of_g6_graphs_to_check = read_file_into_g6_list(input_graphs_textfile)
    list_of_g6_minors = read_file_into_g6_list(input_minors_textfile)
    list_of_g6_graphs_with_minors = []
    list_of_g6_graphs_with_no_minors = []

    SIZE_OF_GRAPHS_TO_CHECK = str(len(list_of_g6_graphs_to_check))
    SIZE_OF_MINORS_TO_CHECK = str(len(list_of_g6_minors))
    test_graph_index = 1
    minor_graph_index = 1

    print("list_of_g6_graphs_to_check:")
    print(list_of_g6_graphs_to_check)
    print("list_of_g6_minors:")
    print(list_of_g6_minors)

    i = 0
    while i < len(list_of_g6_graphs_to_check):
        has_not_deleted = True
        g6_test_graph = list_of_g6_graphs_to_check[i]
        #print("Test Graph: " + g6_test_graph)  # Is still in the form of g6 string compression
        g6_graph_bytes = bytes(g6_test_graph, 'utf8')  # Convert into bytes to use nx.from_graph6_bytes
        g6_graph = nx.from_graph6_bytes(g6_graph_bytes)
        test_graph = list(g6_graph.edges())  # Should be in [(X, X)] form now which can be used by minorminer
        #print(test_graph)  # Print this to check that it is.

        print("\n---Test Graph (" + str(test_graph_index) + " of " + SIZE_OF_GRAPHS_TO_CHECK + "): " + g6_test_graph + " - " + str(test_graph))

        for g6_minor_graph in list_of_g6_minors:  # For each of the test graphs, run through the minors and test if its in there.
            # print("Test Minor: " + g6_minor_graph)  # Is still in the form of g6 string compression
            g6_minor_bytes = bytes(g6_minor_graph, 'utf8')  # Convert into bytes to use nx.from_graph6_bytes
            g6_minor = nx.from_graph6_bytes(g6_minor_bytes)
            test_minor = list(g6_minor.edges())  # Should be in [(X, X)] form now which can be used by minorminer
            #print(test_minor)  # Print this to check that it is.

            print("Test Minor (" + str(minor_graph_index) + " of " + SIZE_OF_MINORS_TO_CHECK + "): " + g6_minor_graph + " - " + str(test_minor))

            if test_graph == []:  # If its empty it will crash on the next line so skip it
                print("Error might occur - Tossing graph: " + g6_test_graph + " - " + str(test_graph))
                break
            if len(find_embedding(test_minor, test_graph)) > 0:
                print("--> HIT: " + str(test_graph) + " is a minor of " + str(test_minor))
                list_of_g6_graphs_with_minors.append(g6_test_graph)  # Add it to the list
                # SEE: https://stackoverflow.com/a/52947607
                del list_of_g6_graphs_to_check[i]
                has_not_deleted = False  # Use this to help set the correct index after removing the item
                break  # Make sure to break here to stop the minor for loop. If not, you're wasting time checking again.
                # Basically you found the graph is a minor, so you remove it from the list and stop checking the minors.
            # END OF IF
            minor_graph_index += 1  # Increment
        # END OF MINOR GRAPH FOR LOOP

        test_graph_index += 1  # Increment
        minor_graph_index = 1  # Reset it for the other loops
        if has_not_deleted:  # If something was deleted, don't move the index (a new item has taken the old index), otherwise move it.
            i += 1

    # END OF TEST GRAPH FOR LOOP

    # The remaining graphs in the list DON'T have minors    
    for graph in list_of_g6_graphs_to_check:
        list_of_g6_graphs_with_no_minors.append(graph)
    # END OF FOR LOOP

    print("list_of_graphs_with_minors:")
    print(list_of_g6_graphs_with_minors)
    print("list_of_graphs_with_no_minors:")
    print(list_of_g6_graphs_with_no_minors)

    # Write the output to the files
    with open(output_with_file, 'w') as fp:
        for item in list_of_g6_graphs_with_minors:
            fp.write("%s\n" % item)  # Each item printed onto a newline
    with open(output_without_file, 'w') as fp:
        for item in list_of_g6_graphs_with_no_minors:
            fp.write("%s\n" % item)
    # END file write
    print("\n\nGraph sorting has finished.\nInputs were input_graphs_textfile: " + input_graphs_textfile
          + " and input_minors_textfile: " + input_minors_textfile +
          "\nCheck: " + output_with_file + " and " + output_without_file)


# Main method
if __name__ == '__main__':
    # Just keep this here because it throws error when everything is commented out
    print("Starting to sort the graphs")
    #sort_graphs("g6/graph4c.g6", "g6/graph3c.g6")
    #sort_graphs("g6/graph7.g6", "g6/planar_conn.6.g6")
    #sort_graphs("g6/graph3c.g6", "g6/graph4c.g6")
    sort_graphs("g6/graph6c.g6", "g6/forbidden_planar_minors.g6")
