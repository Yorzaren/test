import argparse
from main import sort_graphs

parser = argparse.ArgumentParser()
parser.add_argument("input-graphs", help="REQUIRED: The input file for graphs you wish to test")
parser.add_argument("input-minors", help="REQUIRED: The input file for the minors you want to check against the input graphs")
parser.add_argument("--with", "--output-with", help="Name of the output file you want the graphs with minors")
parser.add_argument("--without", "--output-without", help="Name of the output file you want the graphs without minors")
args = parser.parse_args()
config = vars(args)

if __name__ == '__main__':
    # print(config)

    if config.get("with") is not None:
        if config.get("without") is not None:
            sort_graphs(config.get("input-graphs"), config.get("input-minors"), config.get("with"), config.get("without"))
        else:
            sort_graphs(config.get("input-graphs"), config.get("input-minors"), config.get("with"))
    elif config.get("without") is not None:
            sort_graphs(config.get("input-graphs"), config.get("input-minors"), output_without_file=config.get("without"))
    else:
        sort_graphs(config.get("input-graphs"), config.get("input-minors"))
