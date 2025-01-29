#!/usr/bin/python3
class minimax_Coffee:
    def __init__(self, graph, utilities):
        """
        Initialize the search problem.
        :param graph: Dictionary representing the connections between locations (graph).
        :param utilities: Dictionary of utility values for terminal nodes.
        :param initial_state: The starting state of the agent.
        """
        self.graph = graph
        self.utilities = utilities
        
        
    def minimax(self, current_node, is_maximizer, path=[]):
        # Base Case: return the utility value when you reach a leaf node
        if current_node not in self.graph or not self.graph[current_node]:  # Check if the node has no children (leaf)
            return self.utilities.get(current_node, 0), path
                    
        if is_maximizer: # Agents turn 
            max_utility = float('-inf')
            best_path = path
            for neighbor in self.graph.get(current_node, []):
                value, new_path = self.minimax(neighbor, False, path + [current_node])
                max_utility = max(value, max_utility)
                best_path = new_path
            return max_utility, best_path
        
        else: # Adversaries turn
            min_utility = float('inf')
            best_path = path
            for neighbor in self.graph.get(current_node, []):
                
                value, new_path = self.minimax(neighbor, True, path + [current_node])
                min_utility = min(value, min_utility)  
                best_path = new_path
            return (min_utility, best_path)         
# Example Usage
if __name__ == "__main__":
    # Graph of Ethiopia's cities
    graph = {
    "Addis Ababa": ["Ambo", "Adama", "Buta Jirra"],
    "Ambo": ["Gedo", "Nekemte"],
    "Adama": ["Bredawe", "Mojo"],
    "Buta Jirra": ["Woliso", "Worabe"],
    "Woliso": [],  # Add Woliso as a terminal node
    "Gedo": ["Shambu", "Fincha"],
    "Bredawe": ["Harar", "Chiro"],
    "Mojo": ["Dilla"],
    "Worabe": ["Hossana", "Durame"],
    "Durame": ["Bench Naji"],
    "Bench Naji": ["Tepi"],
    "Dilla": ["Kaffa"],
    "Nekemte": [],
    }

    utilities = {
        "Shambu": 4,
        "Fincha": 5,
        "Gimbi": 8,
        "Harar": 10,
        "Chiro": 6,
        "Dilla": 9,
        "Tepi": 6,
        "Kaffa": 7,
        "Hossana": 6,
        "Durame": 5,
        "Bench Naji": 5,
        "Nekemte": 8,
        "Woliso": 0,  # Assign utility for Woliso
    }
    


    # Starting state
    root = "Addis Ababa"

    # Create the search problem instance
    problem = minimax_Coffee(graph, utilities)

    # Run MiniMax algorithm
    best_utility, path = problem.minimax(root, True)
    print(best_utility)
    print(path)
    # Output the results
   
    # def minimax(self, state, is_maximizing, depth=0):
    # """
    # Perform the MiniMax algorithm to determine the best path.
    # :param state: Current state (location).
    # :param is_maximizing: True if it's the agent's turn; False for the adversary's turn.
    # :param depth: Current depth in the search tree.
    # :return: Tuple of (best utility value, best path).
    # """
    #     # Base case: terminal node
    #     if state in self.utilities:
    #         return self.utilities[state], [state]
    #     # Recursive case
    #     best_utility = float('-inf') if is_maximizing else float('inf')
    #     best_path = []
    #     for neighbor in self.graph[state]:
    #         utility, path = self.minimax(neighbor, not is_maximizing, depth + 1)
    #         if is_maximizing:  # Agent's turn (maximize utility)
    #             if utility > best_utility:
    #                 best_utility = utility
    #                 best_path = [state] + path
    #         else:  # Adversary's turn (minimize utility)
    #             if utility < best_utility:
    #                 best_utility = utility
    #                 best_path = [state] + path
    #     return best_utility, best_path
    
    