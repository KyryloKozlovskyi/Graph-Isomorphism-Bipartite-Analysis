# Kyrylo Kozlovskyi G00425385
# https://github.com/KyryloKozlovskyi/Graph-Isomorphism-Bipartite-Analysis
# Function to create an adjacency list for the given vertices and edges
def create_adjacency_map(V, E):
    # Initialize adjacency map with empty sets
    adj_map = {v: set() for v in V}
    # Iterate over the edges
    # For each edge, initialize value as empty set if not present in the adjacency map 
    for u, v in E:
        if u not in adj_map:
            adj_map[u] = set()
        if v not in adj_map:
            adj_map[v] = set()
        # Add the vertices to the adjacency list of each other
        adj_map[u].add(v)
        adj_map[v].add(u)
    # Return the adjacency map
    return adj_map


# Function to check if the graph is bipartite or not using BFS for given vertices and edges
def is_bipartite(V, E):
    adj_map = create_adjacency_map(V, E)  # Create adjacency map
    color = {}  # Dictionary to store colors (0 or 1)
    V1, V2 = set(), set()  # Initialize two sets for bipartition

    # Iterate over all vertices in V to handle disconnected graphs
    for start in V:
        if start in color:
            continue  # Skip already visited nodes

        # Manually initialize queue 
        queue = [start]  # Use list as queue
        front = 0  # Use index for efficiency O(1)
        color[start] = 0
        V1.add(start)  # Add to first set

        # BFS traversal of the graph to assign colors to nodes 
        while front < len(queue):
            node = queue[front]
            front += 1
            # Iterate over neighbors of the node
            for neighbor in adj_map.get(node, []):
                if neighbor not in color:  # Not visited
                    color[neighbor] = 1 - color[node]  # Assign opposite color
                    # Add to corresponding set based on color
                    if color[neighbor] == 0:
                        V1.add(neighbor)
                    else:
                        V2.add(neighbor)
                    # Add to queue for further traversal
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict detected
                    return False, None  # Graph is NOT bipartite

    # Returns Tuple (bool, (V1, V2)) if bipartite or (False, None)
    return True, (V1, V2)  # Graph is bipartite


# Graph 1: Bipartite (Simple Cycle)
V_test1 = {"a", "b", "c", "d"}
E_test1 = {("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")}

# Graph 2: Bipartite (Star Graph) 
V_test2 = {"1", "2", "3", "4", "5"}
E_test2 = {("1", "2"), ("1", "3"), ("1", "4"), ("1", "5")}  # Star graph with center "1"

# Graph 3: Non-Bipartite (Odd Cycle)
V_test3 = {"x", "y", "z"}
E_test3 = {("x", "y"), ("y", "z"), ("z", "x")}  # Triangle (odd cycle)

# Graph 4: Non-Bipartite (Complete K4)
V_test4 = {"p", "q", "r", "s"}
E_test4 = {("p", "q"), ("p", "r"), ("p", "s"), ("q", "r"), ("q", "s"), ("r", "s")}  # K4 (fully connected)

# Graph 5: Edge order affects classification
V_test5 = {"m", "n", "o", "p"}
E_test5 = {("m", "o"), ("n", "p"), ("o", "p")}  # Can be bipartite but depends on edge processing

# Test graphs
test_graphs = {
    "Graph 1 (Bipartite)": (V_test1, E_test1),
    "Graph 2 (Bipartite)": (V_test2, E_test2),
    "Graph 3 (Non-Bipartite)": (V_test3, E_test3),
    "Graph 4 (Non-Bipartite)": (V_test4, E_test4),
    "Graph 5 (Bipartite (Depends on Order))": (V_test5, E_test5)
}

# Run testss
print("\n\n=============================== TEST CASES ================================")
for name, (V, E) in test_graphs.items():
    print(f"Testing {name}")
    print("Graph nodes:", V)
    print("Graph edges:", E)

    result, bipartition = is_bipartite(V, E)
    if result:
        print(f"{name} is bipartite: {bipartition}")
    else:
        print(f"{name} is NOT bipartite")
    print("===========================================================================")
