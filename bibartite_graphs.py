# Kyrylo Kozlovskyi G00425385
# https://github.com/KyryloKozlovskyi/Graph-Isomorphism-Bipartite-Analysis


# Function to create an adjacency list for the given vertices and edges
def create_adjacency_map(V, E):
    # Initialize an empty adjacency map where each vertex points to an empty set.
    adj_map = {v: set() for v in V}
    # Iterate over each edge (u, v) in the edge E.
    for u, v in E:
        # If either vertex is not already in the adjacency map, initialize it with an empty set.
        if u not in adj_map:
            adj_map[u] = set()
        if v not in adj_map:
            adj_map[v] = set()
        # Add each vertex to the adjacency list of the other vertex.
        adj_map[u].add(v)
        adj_map[v].add(u)
    # Return the final adjacency map containing all vertices and their adjacent nodes.
    return adj_map


# Function to check if the graph is bipartite using BFS for given vertices and edges
def is_bipartite(V, E):
    # Step 1: Create an adjacency list representation of the graph.
    adj_map = create_adjacency_map(V, E)
    # Dictionary to store the color assigned to each vertex.
    # Color 0 and 1 represent the two partitions, -1 means unvisited.
    color = {}
    # Two sets to store the two partitions of the bipartite graph.
    V1, V2 = set(), set()
    # Step 2: Iterate over all vertices to ensure disconnected graphs are checked.
    for start in V:
        if start in color:
            continue  # If the vertex is already visited, skip it.
        # Step 3: Initialize the BFS queue and start coloring.
        queue = [start]  # Using a list as a queue
        front = 0  # Pointer to track front of the queue
        color[start] = 0  # Assign the first color
        V1.add(start)  # Place the starting node in the first set
        # Step 4: Perform BFS traversal
        while front < len(queue):
            node = queue[front]  # Get the current node from the queue
            front += 1  # Move the front pointer
            # Iterate over all adjacent nodes
            for neighbor in adj_map.get(node, []):
                if neighbor not in color:  # If the neighbor is unvisited
                    color[neighbor] = 1 - color[node]  # Assign opposite color
                    # Add to the corresponding partition set
                    if color[neighbor] == 0:
                        V1.add(neighbor)
                    else:
                        V2.add(neighbor)
                    # Get the neighbor for further processing
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # If a conflict occurs
                    return False, None  # The graph is NOT bipartite
    # Step 5: If no conflicts were found, return the two bipartite sets
    return True, (V1, V2)

# Graph 1: Bipartite (Simple Cycle)
V_test1 = {"a", "b", "c", "d"}
E_test1 = {("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")} # Even-length cycle

# Graph 2: Bipartite (Star Graph) 
V_test2 = {"1", "2", "3", "4", "5"}
E_test2 = {("1", "2"), ("1", "3"), ("1", "4"), ("1", "5")}  # Star graph with center "1"

# Graph 3: Non-Bipartite (Odd Cycle)
V_test3 = {"x", "y", "z"}
E_test3 = {("x", "y"), ("y", "z"), ("z", "x")}  # Triangle (odd cycle)

# Graph 4: Non-Bipartite (Complete K4)
V_test4 = {"p", "q", "r", "s"}
E_test4 = {("p", "q"), ("p", "r"), ("p", "s"), ("q", "r"), ("q", "s"), ("r", "s")}  # K4 (fully connected)

# Graph 5: Bipartite (Depends on Order)
V_test5 = {"m", "n", "o", "p"}
E_test5 = {("m", "o"), ("n", "p"), ("o", "p")}  # Can be bipartite but depends on edge order

# Test graphs
test_graphs = {
    "Graph 1 (Bipartite)": (V_test1, E_test1),
    "Graph 2 (Bipartite)": (V_test2, E_test2),
    "Graph 3 (Non-Bipartite)": (V_test3, E_test3),
    "Graph 4 (Non-Bipartite)": (V_test4, E_test4),
    "Graph 5 (Bipartite/Non-Bipartite (Depends on Order))": (V_test5, E_test5)
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