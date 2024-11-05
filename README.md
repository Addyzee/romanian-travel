# DFS Pathfinding on Graphs

This project implements a Depth-First Search (DFS) algorithm to find a path between two cities (or nodes) in an undirected graph. The graph is represented using nodes and edges, where each city is connected to neighboring cities by weighted edges representing distances.

The input data (`input.txt`) provides city connections in the format `City1,City2,Distance`, and the code reads these connections to create a graph structure. The algorithm then uses DFS to find a route from a specified start city to an end city, if one exists.

## Table of Contents

1. [Project Structure](#project-structure)
2. [How it Works](#how-it-works)
3. [Setup](#setup)
4. [Usage](#usage)

---

### Project Structure

- **Node Class**: Each city is represented as a `Node` object, which stores the city's name, a dictionary of its neighbors and distances, and a `visited` flag.
- **Graph Construction**: A dictionary of cities (`cities_dict`) is created, and each city is linked with its neighbors and distances.
- **DFS Function**: A recursive DFS function `dfs()` traverses the graph to find a path from the start node to the destination node.
- **Reset Function**: `reset_visited()` resets the `visited` attribute of each node after each DFS traversal.

### How it Works

1. **Parsing Input**: The code reads data from `input.txt`, with each line specifying a city, its neighboring city, and the distance between them.
2. **Graph Representation**:
   - Each city is a `Node` object with a name, neighbors, and distance values.
   - All nodes are stored in `cities_obj`, a dictionary where each key is a city name.
3. **Depth-First Search**:
   - DFS starts from the `start_city` and recursively explores neighbors.
   - The path is stored and updated until the `end_city` is reached, or there are no more unvisited neighbors.
4. **Output**: The path from the start to the end city is printed if found, or `None` if no path exists.

### Setup

1. **Requirements**:
   - Python 3
2. **File Structure**:
   - Ensure `input.txt` exists in the same directory as the script.
   - Each line in `input.txt` should be formatted as `City1,City2,Distance` (e.g., `Arad,Zerind,75`).

### Usage

1. **Run the Script**:
   - Set the `start_city` and `end_city` variables to the desired start and destination cities.
   - Run the script to see the path from the start to the end city, if available.

```python
start_city = "Arad"
end_city = "Bucharest"
path_result = dfs(cities_obj[start_city], cities_obj[end_city])

reset_visited(cities_obj)

print("Path from", start_city, "to", end_city, ":", path_result)

```

Output:

```bash
Path from Arad to Bucharest : [Arad -> {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140}, Zerind -> {'Arad': 75, 'Oradea': 71}, Oradea -> {'Zerind': 71, 'Sibiu': 151}, Sibiu -> {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80}, Fagaras -> {'Sibiu': 99, 'Bucharest': 211}, Bucharest -> {'Fagaras': 211, 'Pitesti': 101, 'Urziceni': 85, 'Giurgiu': 90}]
```
