# pip3 install pandas
# pip3 install graphviz

import pandas as pd
from graphviz import Graph

# (This is a modified graphviz demo project lolol)

# Assume we have a CSV file with columns 'binary_name', 'dependency_name' representing library relationships
df = pd.read_csv('opt-sys-combined.csv')

graph = Graph()

for index, row in df.iterrows():
    binary_name = row['binary_name']
    dependency_name = row['dependency_name']
    graph.node(binary_name)
    graph.node(dependency_name)
    # import name first, since they're the parent of library_name
    graph.edge(dependency_name, binary_name)

graph.render('library_graph', view=True)
