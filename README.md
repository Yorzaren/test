# graphminors

Usage:

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
python run_script.py "Graphs/mixedtest2.txt" "Graphs/forbidden_minors_planar_graphs.txt" --output-with "graphswithminors.txt"
```

Optinal define the name of the output files. 
```
python run_script.py "Graphs/mixedtest2.txt" "Graphs/forbidden_minors_planar_graphs.txt" --output-with "graphswithminors.txt" --output-without "graphswithoutminors.txt"```
