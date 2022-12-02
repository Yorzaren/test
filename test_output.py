"""

Run logical tests to make sure I haven't broken anything when I changed the code.

How you originally generated the correct data: (DON'T RUN AGAIN)

    #sort_graphs("g6/graph4c.g6", "g6/graph3c.g6", "4vertex_graph_with_3_conn_minors.g6", "4vertex_graph_without_3_conn_minors.g6")
    #sort_graphs("g6/graph3c.g6", "g6/graph4c.g6", "3vertex_graph_with_4_conn_minors.g6" , "3vertex_graph_without_4_conn_minors.g6")
    #sort_graphs("g6/graph7.g6", "g6/planar_conn.6.g6", "pc_7vertex_graph_with_6_conn_planar_minors.g6", "pc_7vertex_graph_without_6_conn_planar_minors.g6")
    #sort_graphs("g6/graph6c.g6", "g6/forbidden_planar_minors.g6", "pc_6conn_graph_with_forbidden_planar_minors.g6", "pc_6conn_graph_without_forbidden_planar_minors.g6")

"""
import pytest
from graph6_sorter import sort_graphs, read_file_into_g6_list
import os
import glob

"""
# FORCE the test_output to be clean from the prior tests
@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    # Setup: fill with any logic you want
    files = glob.glob('tests/test_output/*')
    for f in files:
        os.remove(f)

    yield  # this is where the testing happens

    # Teardown : fill with any logic you want
    files = glob.glob('tests/test_output/*')
    for f in files:
        os.remove(f)
"""

def test_4c_to_3c():
    sort_graphs("g6/graph4c.g6", "g6/graph3c.g6", "tests/test_output/4c_to_3c_W.g6", "tests/test_output/4c_to_3cWO.g6")
    test_with = read_file_into_g6_list("tests/test_output/4c_to_3c_W.g6")
    test_without = read_file_into_g6_list("tests/test_output/4c_to_3cWO.g6")
    correct_with = read_file_into_g6_list("tests/4vertex_graph_with_3_conn_minors.g6")
    correct_without = read_file_into_g6_list("tests/4vertex_graph_without_3_conn_minors.g6")
    assert test_with == correct_with
    assert test_without == correct_without
    # check that a 4c graph are minors of 3c graphs; All things 4c are also 3c

def test_3c_to_4c():
    sort_graphs("g6/graph3c.g6", "g6/graph4c.g6", "tests/test_output/3c_to_4cW.g6", "tests/test_output/3c_to_4cWO.g6")
    test_with = read_file_into_g6_list("tests/test_output/3c_to_4cW.g6")
    test_without = read_file_into_g6_list("tests/test_output/3c_to_4cWO.g6")
    correct_with = read_file_into_g6_list("tests/3vertex_graph_with_4_conn_minors.g6")
    correct_without = read_file_into_g6_list("tests/3vertex_graph_without_4_conn_minors.g6")
    assert test_with == correct_with
    assert test_without == correct_without
    # Check that 3c are not minors of 4c graphs.

def test_7vertex_to6_conn_planar():
    sort_graphs("g6/graph7.g6", "g6/planar_conn.6.g6", "tests/test_output/7vertex_to6_conn_planarW.g6",
                "tests/test_output/7vertex_to6_conn_planarWO.g6")
    test_with = read_file_into_g6_list("tests/test_output/7vertex_to6_conn_planarW.g6")
    test_without = read_file_into_g6_list("tests/test_output/7vertex_to6_conn_planarWO.g6")
    correct_with = read_file_into_g6_list("tests/pc_7vertex_graph_with_6_conn_planar_minors.g6")
    correct_without = read_file_into_g6_list("tests/pc_7vertex_graph_without_6_conn_planar_minors.g6")
    assert test_with == correct_with
    assert test_without == correct_without
    # pc prefix means possibly correct, I'm not 100% sure the data is correct. But I have checked it some...

def test_6conn_find_planars():
    sort_graphs("g6/graph6c.g6", "g6/forbidden_planar_minors.g6", "tests/test_output/6conn_find_planarsW.g6",
                "tests/test_output/6conn_find_planarsWO.g6")
    test_with = read_file_into_g6_list("tests/test_output/6conn_find_planarsW.g6")
    test_without = read_file_into_g6_list("tests/test_output/6conn_find_planarsWO.g6")
    correct_with = read_file_into_g6_list("tests/pc_6conn_graph_with_forbidden_planar_minors.g6")
    correct_without = read_file_into_g6_list("tests/pc_6conn_graph_without_forbidden_planar_minors.g6")
    assert test_with == correct_with
    assert test_without == correct_without
    # pc prefix means possibly correct, for some reason it not aligning with the data from the site, but it makes
    # the correct amount of "planar" graphs... Looking at the rejects, those seem correct.
    # Actually, I take that back. If,they are the same things then nothing should be in without.g6
    # Run from the console...
    # python run_script.py "g6/graph6c.g6", "g6/forbidden_planar_minors.g6" --output-with "graphswithminors.g6" --output-without "graphswithoutminors.g6"
    # python run_script.py "graphswithoutminors.g6", "g6/planar_conn.6.g6"
