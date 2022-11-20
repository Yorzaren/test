"""

Run logical tests to make sure I haven't broken anything when I changed the code.

How you originally generated the correct data: (DON'T RUN AGAIN)

    #sort_graphs("g6/graph4c.g6", "g6/graph3c.g6", "4vertex_graph_with_3_conn_minors.txt", "4vertex_graph_without_3_conn_minors.txt")
    #sort_graphs("g6/graph3c.g6", "g6/graph4c.g6", "3vertex_graph_with_4_conn_minors.txt" , "3vertex_graph_without_4_conn_minors.txt")
    #sort_graphs("g6/graph7.g6", "g6/planar_conn.6.g6", "pc_7vertex_graph_with_6_conn_planar_minors.txt", "pc_7vertex_graph_without_6_conn_planar_minors.txt")
    #sort_graphs("g6/graph6c.g6", "g6/forbidden_planar_minors.g6", "pc_6conn_graph_with_forbidden_planar_minors.txt", "pc_6conn_graph_without_forbidden_planar_minors.txt")

"""
import unittest
from graph6_sorter import sort_graphs, read_file_into_g6_list


class TestCheckGraphOutputs(unittest.TestCase):
    def test_4c_to_3c(self):
        sort_graphs("g6/graph4c.g6", "g6/graph3c.g6")
        test_with = read_file_into_g6_list("with.txt")
        test_without = read_file_into_g6_list("without.txt")
        correct_with = read_file_into_g6_list("tests/4vertex_graph_with_3_conn_minors.txt")
        correct_without = read_file_into_g6_list("tests/4vertex_graph_without_3_conn_minors.txt")
        self.assertEqual(test_with, correct_with)
        self.assertEqual(test_without, correct_without)
        # check that a 4c graph are minors of 3c graphs; All things 4c are also 3c

    def test_3c_to_4c(self):
        sort_graphs("g6/graph3c.g6", "g6/graph4c.g6")
        test_with = read_file_into_g6_list("with.txt")
        test_without = read_file_into_g6_list("without.txt")
        correct_with = read_file_into_g6_list("tests/3vertex_graph_with_4_conn_minors.txt")
        correct_without = read_file_into_g6_list("tests/3vertex_graph_without_4_conn_minors.txt")
        self.assertEqual(test_with, correct_with)
        self.assertEqual(test_without, correct_without)
        # Check that 3c are not minors of 4c graphs.

    def test_7vertex_to6_conn_planar(self):
        sort_graphs("g6/graph7.g6", "g6/planar_conn.6.g6")
        test_with = read_file_into_g6_list("with.txt")
        test_without = read_file_into_g6_list("without.txt")
        correct_with = read_file_into_g6_list("tests/pc_7vertex_graph_with_6_conn_planar_minors.txt")
        correct_without = read_file_into_g6_list("tests/pc_7vertex_graph_without_6_conn_planar_minors.txt")
        self.assertEqual(test_with, correct_with)
        self.assertEqual(test_without, correct_without)
        # pc prefix means possibly correct, I'm not 100% sure the data is correct. But I have checked it some...

    def test_6conn_find_planars(self):
        sort_graphs("g6/graph6c.g6", "g6/forbidden_planar_minors.g6")
        test_with = read_file_into_g6_list("with.txt")
        test_without = read_file_into_g6_list("without.txt")
        correct_with = read_file_into_g6_list("tests/pc_6conn_graph_with_forbidden_planar_minors.txt")
        correct_without = read_file_into_g6_list("tests/pc_6conn_graph_without_forbidden_planar_minors.txt")
        self.assertEqual(test_with, correct_with)
        self.assertEqual(test_without, correct_without)
        # pc prefix means possibly correct, for some reason it not aligning with the data from the site, but it makes
        # the correct amount of "planar" graphs... Looking at the rejects, those seem correct.


if __name__ == '__main__':
    unittest.main()