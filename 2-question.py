#!/usr/bin/python3
""" 

"""
import heapq

class UninformedSearch:
    """
    
    """
    def __init__(self, graph, goals):
        self.graph = graph
        self.goals = set(goals)  # Ensure goals are a set
    
    def ucs(self, start):
        # Initialize the priority queue with (cost, current_city, path)
        pri_queue = []
        heapq.heappush(pri_queue, (0, start, []))
        visited = set()
        found_goals = set()  # To track reached goals
        total_cost = 0
        final_path = []  # Complete path visiting all goals

        while pri_queue:
            # Unpack the priority queue
            f, current_city, path = heapq.heappop(pri_queue)

            if current_city in visited:
                continue
            visited.add(current_city)
            path = path + [current_city]

            # Check if the current city is a goal
            if current_city in self.goals and current_city not in found_goals:
                found_goals.add(current_city)
                total_cost += f
                final_path.extend(path if not final_path else path[1:])
                print(f"Reached goal '{current_city}' with cost {f}, total cost so far: {total_cost}")

                # Check if all goals are reached
                if found_goals == self.goals:
                    return final_path, total_cost

            # Add adjacent cities to the priority queue
            for city, cost in self.graph.get(current_city, []):
                if city not in visited:
                    heapq.heappush(pri_queue, (f + cost, city, path))

        # If not all goals are reached
        return final_path, total_cost if found_goals else ([], 0)


# Example Graph
graph = {
    "Addis Ababa": [("Ambo", 5), ("Adama", 3), ("Debre Berhan", 5)],
    "Ambo": [("Addis Ababa", 5), ("Woliso", 6)],
    "Adama": [("Addis Ababa", 3), ("Assella", 4), ("Batu", 4)],
    "Debre Berhan": [("Addis Ababa", 5), ("Debre Sina", 3)],
    "Holeta": [("Addis Ababa", 1)],
    "Woliso": [("Ambo", 6), ("Jimma", 6)],
    "Jimma": [("Woliso", 6), ("Bonga", 4)],
    "Bonga": [("Jimma", 4), ("Gore", 5)],
    "Gore": [("Bonga", 5), ("Gambela", 6)],
    "Gambela": [("Gore", 6)],
    "Assella": [("Adama", 4), ("Dodola", 3)],
    "Dodola": [("Assella", 3), ("Bale", 4)],
    "Bale": [("Dodola", 4), ("Goba", 6)],
    "Goba": [("Bale", 6), ("Liben", 13)],
    "Liben": [("Goba", 13), ("Moyale", 11)],
    "Moyale": [("Liben", 11)],
    "Batu": [("Adama", 4), ("Shashemene", 4)],
    "Shashemene": [("Batu", 4), ("Hawassa", 3)],
    "Hawassa": [("Shashemene", 3), ("Dilla", 4)],
    "Dilla": [("Hawassa", 4), ("Yabelo", 6)],
    "Yabelo": [("Dilla", 6), ("Konso", 3)],
    "Konso": [("Yabelo", 3), ("Arba Minch", 6)],
    "Arba Minch": [("Konso", 6)],
    "Debre Sina": [("Debre Berhan", 3), ("Kemise", 4)],
    "Kemise": [("Debre Sina", 4), ("Dessie", 3)],
    "Dessie": [("Kemise", 3), ("Woldia", 4)],
    "Woldia": [("Dessie", 4), ("Lalibela", 11)],
    "Lalibela": [("Woldia", 11), ("Sekota", 8)],
    "Sekota": [("Lalibela", 8), ("Axum", 6)],
    "Axum": [("Sekota", 6), ("Shire", 8)],
    "Shire": [("Axum", 8), ("Humera", 7)],
    "Humera": [("Shire", 7), ("Kartum", 21)],
    "Kartum": [("Humera", 21)]
}

start = "Addis Ababa"
goals = {"Lalibela", "Axum", "Bale", "Jimma", "Arba Minch"}
search = UninformedSearch(graph, goals)

# Perform Uniform Cost Search
result = search.ucs(start)
print("\nFinal Result:", result)
# 
