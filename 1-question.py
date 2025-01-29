#!/usr/bin/python3
# Represent the state-space graph for the Traveling Ethiopia problem as an adjacency list.
graph = {
    'Addis Ababa': ['Ambo', 'Adama', 'Debre Berhan', 'Holeta'],
    'Ambo': ['Addis Ababa', 'Woliso'],
    'Adama': ['Addis Ababa', 'Assella', 'Batu'],
    'Debre Berhan': ['Addis Ababa', 'Debre Sina'],
    'Holeta': ['Addis Ababa'],
    'Woliso': ['Ambo', 'Jimma'],
    'Jimma': ['Woliso', 'Bonga'],
    'Bonga': ['Jimma', 'Gore'],
    'Gore': ['Bonga', 'Gambela'],
    'Gambela': ['Gore'],
    'Assella': ['Adama', 'Dodola'],
    'Dodola': ['Assella', 'Bale'],
    'Bale': ['Dodola', 'Goba'],
    'Goba': ['Bale', 'Liben'],
    'Liben': ['Goba', 'Moyale'],
    'Moyale': ['Liben'],
    'Batu': ['Adama', 'Shashemene', 'Arsi Negele'],
    'Shashemene': ['Batu', 'Awasa'],
    'Awasa': ['Shashemene', 'Dilla'],
    'Dilla': ['Awasa', 'Yabelo'],
    'Yabelo': ['Dilla', 'Konso'],
    'Konso': ['Yabelo', 'Arba Minch'],
    'Arba Minch': ['Konso'],
    'Debre Sina': ['Debre Berhan', 'Kemise'],
    'Kemise': ['Debre Sina', 'Dessie'],
    'Dessie': ['Kemise', 'Woldia'],
    'Woldia': ['Dessie', 'Lalibela'],
    'Lalibela': ['Woldia', 'Sekota'],
    'Sekota': ['Lalibela', 'Axum'],
    'Axum': ['Sekota', 'Shire'],
    'Shire': ['Axum', 'Humera'],
    'Humera': ['Shire', 'Kartu'],
    'Kartu': ['Humera'],
}

# Define a class for searching paths in the graph using BFS and DFS.
class TravelingEthiopia:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start, goal):
        """Perform Breadth-First Search."""
        queue = [(start, [start])]
        visited = set()
        # loop until all elements of the queue are poped
        while queue:
            (node, path) = queue.pop(0)
            # if the city is visited do not go through it
            
            if node in visited:
                continue
            # add city to the visited set
            visited.add(node)

            # add the adjecent cities of the current_city to a queue
            for neighbor in self.graph.get(node, []):
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))

        return None  # No path found

    def dfs(self, start, goal):
        """Perform Depth-First Search."""
        stack = [(start, [start])]
        visited = set()

        while stack:
            (node, path) = stack.pop()
            if node in visited:
                continue

            visited.add(node)
            # add the adjecent cities of the current_city to a queue
            for neighbor in self.graph.get(node, []):
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    stack.append((neighbor, path + [neighbor]))

        return None  # No path found

# Example Usage
uniformedsearch = TravelingEthiopia(graph)

# Set start and goal cities
start_city = 'Addis Ababa'
goal_city = 'Bale'

# assign bfs and dfs methods of the uniformedsearch object to their respective variables
bfs_path = uniformedsearch.bfs(start_city, goal_city)
dfs_path = uniformedsearch.dfs(start_city, goal_city)

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)

