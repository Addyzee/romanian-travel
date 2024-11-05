from typing import List, Dict, Optional

class Node:
    def __init__(self, name: str):
        self.name = name
        self.neighbours: Dict['Node', int] = {}
        
    def __repr__(self):
        neighbours_str = {
            neighbour.name: distance for neighbour, distance in self.neighbours.items()
        }
        return f"{self.name} -> {neighbours_str}"

    def __str__(self):
        return self.__repr__()

def load_graph(filename: str) -> Dict[str, Node]:
    """Parse input file and return a dictionary of city nodes with neighbors and distances."""
    cities_dict = {}
    
    with open(filename, "r") as file:
        for line in file:
            city, neighbour, distance = line.split(",")
            distance = int(distance.strip())
            
            if city not in cities_dict:
                cities_dict[city] = Node(city)
            if neighbour not in cities_dict:
                cities_dict[neighbour] = Node(neighbour)
            
            # Update neighbors in both directions
            cities_dict[city].neighbours[cities_dict[neighbour]] = distance
            cities_dict[neighbour].neighbours[cities_dict[city]] = distance

    return cities_dict

def dfs(node_start: Node, node_end: Node, visited: Optional[set] = None, path: Optional[List[Node]] = None) -> Optional[List[Node]]:
    """
    Perform DFS to find a path from node_start to node_end.

    Args:
        node_start (Node): The starting node.
        node_end (Node): The destination node.
        visited (set): Set of visited nodes to avoid cycles.
        path (list): Current path of nodes.

    Returns:
        list: A list of nodes representing the path, or None if no path found.
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # Add current node to path and mark as visited
    path.append(node_start)
    visited.add(node_start)

    # Check if destination is reached
    if node_start == node_end:
        return path

    # Explore each unvisited neighbour
    for neighbour in node_start.neighbours:
        if neighbour not in visited:
            result = dfs(neighbour, node_end, visited, path)
            if result:  # Path found
                return result

    # Backtrack if no path found
    path.pop()
    return None


# Main
if __name__ == "__main__":
    cities_obj = load_graph("input.txt")
    
    start_city = "Arad"
    end_city = "Bucharest"
    
    path_result = dfs(cities_obj[start_city], cities_obj[end_city])
    
    if path_result:
        print("Path from", start_city, "to", end_city, ":", " -> ".join([node.name for node in path_result]))
    else:
        print("No path found from", start_city, "to", end_city)
