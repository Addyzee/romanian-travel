# DFS Pathfinding on Romanian Cities

This project demonstrates how to use a Depth-First Search (DFS) algorithm to find a route between two cities, represented as an undirected graph. Each city is connected to others through roads, with distances provided. The goal is to explore paths from one city to another and print the route if it exists.

### Overview

The project takes an input file with city connections (name of city 1, name of city 2, distance between them) and builds a graph. It then uses DFS to explore paths from a specified starting city to a destination city.

### Example Map
![Romania Map](/romania.png)

### Example Path
![Arad to Bucharest](/path-chosen.png)

### How It Works

1. **Graph Representation**:
   - The cities are represented as nodes, each storing the neighboring cities and distances.
   - The graph is loaded from a file, which lists city connections in the format: `City1, City2, Distance`.

2. **Depth-First Search**:
   - The DFS algorithm starts from a given starting city and explores all possible routes recursively until it finds the destination city.
   - If a path is found, it will print the cities in the order they are visited.

3. **Output**:
   - The program prints the cities visited along the path if a route exists; otherwise, it indicates that no path was found.

### Project Structure

- **Node Class**: Represents each city (node) with its neighboring cities and distances.
- **DFS Algorithm**: Recursively searches through the graph to find a path between two cities.
- **File Input**: City connections are loaded from a file `input.txt`.

### Setup

1. **Requirements**:
   - Python 3.x

2. **File Format**:
   - The input file `input.txt` should contain lines with the format: `City1, City2, Distance`.

### Usage

1. **Run the Script**:
   - Set the starting and destination cities in the code.
   - The program will then find a route from the start city to the destination city (if one exists) and print the path.

2. **Example**:
   - Input file (example `input.txt`):
     ```
     Arad,Zerind,75
     Zerind,Oradea,71
     Oradea,Sibiu,151
     Sibiu,Fagaras,99
     Fagaras,Bucharest,211
     ```
   - Output (for `Arad` to `Bucharest`):
     ```
     Path from Arad to Bucharest : Arad -> Zerind -> Oradea -> Sibiu -> Fagaras -> Bucharest
     ```


