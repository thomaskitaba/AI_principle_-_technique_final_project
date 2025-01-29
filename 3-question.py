#!/usr/bin/python3
import heapq

class Informedsearch:
    def __init__(self, graph, goal, heuristic):
        self.graph = graph
        self.goal = goal
        self.heuristic = heuristic
    
    def A(self, start):
        # initialize priority queue and visited variables 
        pri_queue = []
        visited = set()
        
        # add the start city and information related to it, into the priority queue
        # f(n) = g(n) + h(n)  -> imidiate cost + expected utility to the goal
        heapq.heappush(pri_queue, (self.heuristic.get(start), 0, start, []))
        
        while pri_queue:
            
            # unpack variable of the the smallest element which infact is a tuple that contains the smallest f(n) 
            f, g, current_node, path = heapq.heappop(pri_queue)  
            
            # check if goal city is reached
            if current_node == self.goal:
                return path + [current_node], f
            
            # create a new path, by adding the current city to the previous path
            new_path = path + [current_node]
            
            neighbor = self.graph.get(current_node, [])
            # check if the city is visited or not
            if current_node not in visited:
                path = path + [current_node]
                visited.add(current_node)
                
                # loop accross the adjecent cities and add them to the priority queue
                for city, cost in neighbor:
                    heapq.heappush(pri_queue, (g + cost + self.heuristic.get(city),  g + cost, city, new_path))
        return ['Path not Found']
# adjecency list representation for cities
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
# utitlity expected to reach the goal city from a specific city
heuristic = {
    "Addis Ababa": 26,
    "Ambo": 31,
    "Adama": 23,
    "Debre Berhan": 31,
    "Holeta": 21, 
    "Woliso": 25,
    "Jimma": 33,
    "Bonga": 13,
    "Gore": 46,
    "Gambela": 51,
    "Assella": 22,
    "Dodola": 19, 
    "Bale": 22, 
    "Goba": 40,
    "Liben": 11, 
    "Moyale": 0,
    "Batu": 19,
    "Shashemene": 16,
    "Hawassa": 15,
    "Dilla": 12,
    "Yabelo": 6,
    "Konso": 9,
    "Arba Minch": 13,
    "Debre Sina": 33,
    "Kemise": 40,
    "Dessie": 44,
    "Woldia": 30,
    "Lalibela": 57,
    "Sekota": 59,
    "Axum": 66,
    "Shire": 67,
    "Humera": 65,
    "Kartum": 81,
}

start = 'Addis Ababa'
goal = 'Moyale'
search = Informedsearch(graph, goal, heuristic)
result = search.A(start)
print(f"Path: {result[0]}")
print(f"Total Utility: {result[1]}")

# print(search.A(start))

