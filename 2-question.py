#!/usr/bin/python3
import heapq
class Uninformedsearch:
    def __init__(self, graph, goal):
        self.graph = graph
        self.goal = goal
    
    # add function that loops accross goal states and finds
    def find_optimal_city(self, start):
        # return ["a", 0]
        path, cost = self.ucs(start, self.goal)
        return path, cost
        # iterate across each goal
    def ucs(self, start, goal):
        # initialize and add start city to a priority queue  (f(n), start, path)
        pri_queue = []
        heapq.heappush(pri_queue, (0,  start, []))
        
        visited = set()

        while pri_queue:
            # unpack the pri_queue
            f, current_city, path = heapq.heappop(pri_queue)
            
            if current_city == goal:
                return path + [current_city], f
            
            if current_city not in visited:
                new_path = path + [current_city]
                visited.add(current_city)
                for city, cost in graph.get(current_city, []):
                    heapq.heappush(pri_queue, (f + cost, city, new_path))
        return ["Path Not found", 0]
                    
                
                
                
        
        
        
        
graph = {
    "Addis Ababa": [("Ambo", 5), ("Adama", 3), ("Debre Berhan", 5)],
    "Ambo": [("Addis Ababa", 5), ("Woliso", 6)],
    "Adama": [("Addis Ababa", 3), ("Assella", 4), ("Batu", 4)],
    "Debre Berhan": [("Addis Ababa", 5), ("Debre Sina", 3)],
    "Holeta": [("Addis Ababa", 1)],
    "Woliso": [("Ambo", 3), ("Jimma", 6)],
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
    "Batu": [("Adama", 3), ("Shashemene", 4)],
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
heuristic = {
    "Addis Ababa": 0,
    "Ambo": 0,
    "Adama": 0,
    "Debre Berhan": 0,
    "Holeta": 0, 
    "Woliso": 0,
    "Jimma": 0,
    "Bonga": 0,
    "Gore": 0,
    "Gambela": 0,
    "Assella": 0,
    "Dodola": 0, 
    "Bale": 0, 
    "Goba": 0,
    "Liben": 0, 
    "Moyale": 0,
    "Batu": 0,
    "Shashemene": 0,
    "Hawassa": 0,
    "Dilla": 0,
    "Yabelo": 0,
    "Konso": 0,
    "Arba Minch": 0,
    "Debre Sina": 0,
    "Kemise": 0,
    "Dessie": 0,
    "Woldia": 0,
    "Lalibela": 0,
    "Sekota": 0,
    "Axum": 0,
    "Shire": 0,
    "Humera": 0,
    "Kartum": 0,
}


start = 'Addis Ababa'
goal = 'Moyale'
search = Uninformedsearch(graph, goal)
# result = search.ucs(start, goal) disabled temporarly
result = search.find_optimal_city(start)
print(result)
print(f"Path: {result[0]}")
print(f"Total Utility: {result[1]}")

# print(search.A(start))


# graph = {
#     "Addis Ababa": [("Ambo", 5), ("Adama", 3), ("Debre Berhan", 5)],
#     "Ambo": [("Addis Ababa", 5), ("Woliso", 6)],
#     "Adama": [("Addis Ababa", 3), ("Assella", 4), ("Batu", 4)],
#     "Debre Berhan": [("Addis Ababa", 5), ("Debre Sina", 3)],
#     "Holeta": [("Addis Ababa", 1)],
#     "Woliso": [("Ambo", 3), ("Jimma", 6)],
#     "Jimma": [("Woliso", 6), ("Bonga", 4)],
#     "Bonga": [("Jimma", 4), ("Gore", 5)],
#     "Gore": [("Bonga", 5), ("Gambela", 6)],
#     "Gambela": [("Gore", 6)],
#     "Assella": [("Adama", 4), ("Dodola", 3)],
#     "Dodola": [("Assella", 3), ("Bale", 4)],
#     "Bale": [("Dodola", 4), ("Goba", 6)],
#     "Goba": [("Bale", 6), ("Liben", 13)],
#     "Liben": [("Goba", 13), ("Moyale", 11)],
#     "Moyale": [("Liben", 11)],
#     "Batu": [("Adama", 3), ("Shashemene", 4), ("Arsi Negele", 3)],
#     "Shashemene": [("Batu", 4), ("Awasa", 3)],
#     "Awasa": [("Shashemene", 3), ("Dilla", 4)],
#     "Dilla": [("Awasa", 4), ("Yabelo", 6)],
#     "Yabelo": [("Dilla", 6), ("Konso", 3)],
#     "Konso": [("Yabelo", 3), ("Arba Minch", 6)],
#     "Arba Minch": [("Konso", 6)],
#     "Debre Sina": [("Debre Berhan", 3), ("Kemise", 4)],
#     "Kemise": [("Debre Sina", 4), ("Dessie", 3)],
#     "Dessie": [("Kemise", 3), ("Woldia", 4)],
#     "Woldia": [("Dessie", 4), ("Lalibela", 11)],
#     "Lalibela": [("Woldia", 11), ("Sekota", 8)],
#     "Sekota": [("Lalibela", 8), ("Axum", 6)],
#     "Axum": [("Sekota", 6), ("Shire", 8)],
#     "Shire": [("Axum", 8), ("Humera", 7)],
#     "Humera": [("Shire", 7), ("Kartum", 21)],
#     "Kartum": [("Humera", 21)]
# }
