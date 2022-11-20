# graphminors

Takes as inputs two .g6 files "list.g6" and "minors.g6" and outputs two other files "with.g6" and "without.g6". The program checks all the graphs in list.g6 and selects those which have no minors in minors.g6 and outputs them to without.g6, and outputs the rest in with.g6. 

### What is a .g6?

Graph6 graph data format. Esentially a .txt with heavily compressed graph data into letters and symbols.

### Graph6 Examples: 

https://users.cecs.anu.edu.au/~bdm/data/graphs.html

### Nauty Traces

https://pallini.di.uniroma1.it/

geng -C 11 15:34

## Usage OUTDATED:

Clone the code on to your machine:
```
git clone https://github.com/Yorzaren/graphminors
```

Change directories into the cloned folder:

```
cd graphminors
```

Install the dependencies using pip

```
pip install -r requirements.txt
```

Call the code:

```
python run_script.py "g6/graph4c.g6", "g6/graph3c.g6"
```

Optional define the name of the output files. 

```
python run_script.py "g6/graph4c.g6", "g6/graph3c.g6" --output-with "graphswithminors.g6" --output-without "graphswithoutminors.g6"
```
