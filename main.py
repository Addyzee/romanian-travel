class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = {}
        self.visited = False

    def __repr__(self):
        neighbours_str = {
            neighbour.name: distance for neighbour, distance in self.neighbours.items()
        }
        return f"{self.name} -> {neighbours_str}"

    def __str__(self):
        return self.__repr__()


with open("input.txt", "r") as file:
    nodes = file.readlines()


cities_dict = {}

for node in nodes:
    city, neighbour, distance = node.split(",")
    distance = int(distance.strip())

    if city not in cities_dict:
        cities_dict[city] = {}
    if neighbour not in cities_dict:
        cities_dict[neighbour] = {}

    cities_dict[city][neighbour] = distance
    cities_dict[neighbour][city] = distance

"""
cities_dict = 
{
    'Arad': 
        {'Zerind': 75,
         'Timisoara': 118,
         'Sibiu': 140}...
}
"""


cities_obj = {}

for city in cities_dict:
    cities_obj[city] = Node(city)

"""
cities_obj =
{
    'Arad': Node('Arad'),
    'Zerind': Node('Zerind'),
    'Timisoara': Node('Timisoara'),
    'Sibiu': Node('Sibiu'),
    ...
}
"""


# adding neighbours and distances to the nodes
for city, neighbours in cities_dict.items():
    for neighbour, distance in neighbours.items():
        """
        eg
        city = 'Arad', neighbour = 'Zerind', distance = 75
        # cities_obj[city] -> Node('Arad').neighbours[Node('Zerind')] = 75
        """
        cities_obj[city].neighbours[cities_obj[neighbour]] = distance

'''
Arad -> {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140}
Zerind -> {'Arad': 75, 'Oradea': 71}
'''



def dfs(node_start, node_end, path=None):
    if path is None:
        path = []

    # Add current node to path
    path = path + [node_start]

    # Destination reached
    if node_start == node_end:
        return path

    node_start.visited = True

    # Visit each unvisited neighbour recursively
    for neighbour in node_start.neighbours:
        if not neighbour.visited:
            new_path = dfs(neighbour, node_end, path)
            if new_path:  # Path found
                return new_path

    # If no path found, return None
    return None


# Reset the visited attr
def reset_visited(cities_obj):
    for node in cities_obj.values():
        node.visited = False


start_city = "Arad"
end_city = "Bucharest"
path_result = dfs(cities_obj[start_city], cities_obj[end_city])

reset_visited(cities_obj)

print("Path from", start_city, "to", end_city, ":", path_result)


