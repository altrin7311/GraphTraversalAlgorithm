# Graph Traversal Algorithm Visualization

## Overview
This Python script visualizes graph traversal using **NetworkX** and **Matplotlib**. It allows users to input graph edges, checks if the graph is connected, and animates Depth-First Search (DFS) traversal.

## Features
- **Graph Creation**: Users can input edges interactively.
- **Connectivity Check**: Determines whether the graph is connected or not.
- **Visualization**:
  - Displays nodes and edges using a circular layout.
  - Highlights the current node being traversed.
  - Animates the DFS traversal process.
- **Graph Aesthetics**:
  - Nodes are colored blue, with the current node highlighted in red.
  - Edges are visualized with arrows for better clarity.
  - Displays a text label indicating graph connectivity.

## Installation
Ensure you have Python installed along with the required libraries:
```sh
pip install networkx matplotlib
```

## Usage
Run the script and enter edges as prompted:
```sh
python graph_traversal.py
```
- Enter edges as space-separated values (e.g., `1 2`).
- Type `done` when finished.
- The script will visualize and animate the traversal.

## Example Input
```
Enter an edge as 'node1 node2' (or type 'done' to finish): 1 2
Enter an edge as 'node1 node2' (or type 'done' to finish): 2 3
Enter an edge as 'node1 node2' (or type 'done' to finish): done
```

## Expected Output
- A visual representation of the graph.
- Animation of the DFS traversal process.
- Connectivity status displayed on the graph.

## Notes
- The script uses **DFS** for traversal visualization.
- Graphs are displayed using **Matplotlib's animation feature**.
- Nodes are positioned using a **circular layout** for better visualization.

## License
This project is open-source and available under the MIT License.

