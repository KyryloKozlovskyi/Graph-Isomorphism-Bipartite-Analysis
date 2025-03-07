# Graph pairs for isomorphism check

# 1. Pair that satisfies criteria a and b, but fails on criterion c (different degree sequences)
# Graph 1a consists of a list of vertices and a list of sets of edges
V_test1a = ["a", "b", "c", "d", "e"]
E_test1a = [{"a", "b"}, {"b", "c"}, {"c", "d"}, {"d", "e"}, {"e", "a"}]

# Graph 1b consists of a list of vertices and a list of sets of edges
V_test1b = ["v", "w", "x", "y", "z"]
E_test1b = [{"v", "w"}, {"v", "x"}, {"v", "y"}, {"v", "z"}, {"w", "x"}] 

# Create graphs for test 1 as tuples
G_test1a = (V_test1a, E_test1a)
G_test1b = (V_test1b, E_test1b)

# 2. Pair that satisfies criteria a, b, and c but not isomorphic
# Graph 2a consists of a list of vertices and a list of sets of edges
V_test2a = ["a", "b", "c", "d", "e", "f"]
E_test2a = [{"a", "b"}, {"b", "c"}, {"c", "d"}, {"d", "e"}, {"e", "f"}, {"f", "a"}]  

# Graph 2b consists of a list of vertices and a list of sets of edges
V_test2b = ["v", "w", "x", "y", "z", "t"]
E_test2b = [{"v", "w"}, {"v", "x"}, {"w", "y"}, {"x", "z"}, {"y", "t"}, {"z", "t"}] 

# Create graphs for test 2 as tuples
G_test2a = (V_test2a, E_test2a)
G_test2b = (V_test2b, E_test2b)

# 3. Pair that satisfies criteria a, b, and c but not isomorphic
# Graph 3a consists of a list of vertices and a list of sets of edges
V_test3a = ["a", "b", "c", "d", "e", "f"]
E_test3a = [{"a", "b"}, {"a", "c"}, {"a", "d"}, {"b", "e"}, {"c", "e"}, {"d", "f"}, {"e", "f"}]

# Graph 3b consists of a list of vertices and a list of sets of edges
V_test3b = ["v", "w", "x", "y", "z", "t"]
E_test3b = [{"v", "w"}, {"v", "x"}, {"w", "y"}, {"x", "y"}, {"y", "z"}, {"z", "t"}, {"v", "t"}]

# Create graphs for test 3 as tuples
G_test3a = (V_test3a, E_test3a)
G_test3b = (V_test3b, E_test3b)

# 4. Pair that satisfies all criteria and is isomorphic
# Graph 4a consists of a list of vertices and a list of sets of edges
V_test4a = [ "a", "b", "c", "d", "e", "f" ]
E_test4a = [ {"a", "b"}, {"a", "c"}, {"a", "f"}, {"b", "c"}, {"b", "d"}, {"b", "f"}, {"c", "d"}, {"d", "e"}, {"d",
"f"}, {"e", "f"} ]

# Graph 4b consists of a list of vertices and a list of sets of edges
V_test4b = ["g", "h", "k", "m", "n", "p"]
E_test4b = [ {"g", "h"}, {"g", "m"}, {"g", "p"}, {"h", "k"}, {"h", "m"}, {"h", "p"}, {"k", "p"}, {"k", "m"}, {"m",
"n"}, {"n", "p"} ]

# Create graphs for test 4 as tuples
G_test4a = (V_test4a, E_test4a)
G_test4b = (V_test4b, E_test4b)

# 5. Pair that satisfies all criteria and is isomorphic
# Graph 5a consists of a list of vertices and a list of sets of edges
V_test5a = ["a", "b", "c", "d"]
E_test5a = [{"a", "b"}, {"b", "c"}, {"c", "d"}, {"d", "a"}] 

# Graph 5b consists of a list of vertices and a list of sets of edges
V_test5b = ["w", "x", "y", "z"]
E_test5b = [{"w", "x"}, {"x", "y"}, {"y", "z"}, {"z", "w"}]

# Create graphs for test 5 as tuples
G_test5a = (V_test5a, E_test5a)
G_test5b = (V_test5b, E_test5b)

# Function to get the number of vertices in a graph
# Considering the graph is a tuple with the first (0) element being the list of vertices
def getNumberOfVertices(graph):
    return len(graph[0])

# Function to get the number of edges in a graph
# Considering the graph is a tuple with the second (1) element being the list of edges
def getNumberOfEdges(graph):
    return len(graph[1])

# Function to get the degree of each vertex in a graph
# Considering the graph is a tuple with the first (0) element being the list of vertices
# and the second (1) element being the list of edges
def getDegree(V, E):
    # Create a dictionary to store the degree of each vertex and initialize it with 0
    counts = {v: 0 for v in V}
    # Iterate over the vertices
    for v in V:
        # Iterate over the edges
        for e in E:
            # If the vertex is in the edge, increment the count
            if v in e:
                counts[v] += 1
    # Return the dictionary with the degree (a number of times a vertex appears in edges)
    return counts

# Function to get the degree sequence of a graph
# Considering the degree is a dictionary with the vertex as the key and the degree as the value
def getDegreeSequence(D):
    # Return the sorted list of degrees in descending order by getting the values of the dictionary and sorting them in reverse
    return sorted(D.values(), reverse=True)

# Function to get the Adjacency List of a graph
def getAdjacencyList(V, E):
    adjacency_list = {v: set() for v in V}
    for e in E:
        v1, v2 = e
        adjacency_list[v1].add(v2)
        adjacency_list[v2].add(v1)
    return adjacency_list

# Function to get the degree sequence of a graph
def getAdjacentDegrees(V, E):
    adjacency_list = getAdjacencyList(V, E)
    degrees = getDegree(V, E)
    
    adjacent_degrees = {}
    for v in V:
        adjacent_degrees[v] = sorted([degrees[adj] for adj in adjacency_list[v]], reverse=True)
    
    return adjacent_degrees

# ---
def dictToList(degree_dict):
    # Extract the values (lists) from the dictionary
    values = list(degree_dict.values())
    
    # Sort the lists in descending order based on their first element or length
    ordered_list = sorted(values, reverse=True)
    
    return ordered_list

# Function to check if two graphs are isomorphic
# Considering the graphs are tuples with the first (0) element being the list of vertices
# and the second (1) element being the list of edges
def areGraphsIsomorphic(G1, G2):
    dtmp1 = getDegree(G1[0], G1[1])
    dtmp2 = getDegree(G2[0], G2[1])

    adjacent_degrees_G1 = getAdjacentDegrees(G1[0], G1[1])
    adjacent_degrees_G2 = getAdjacentDegrees(G2[0], G2[1])

    ordered_list_G1 = dictToList(adjacent_degrees_G1)
    ordered_list_G2 = dictToList(adjacent_degrees_G2)

    print("Ordered list of adjacent degrees for G1:", ordered_list_G1)
    print("Ordered list of adjacent degrees for G2:", ordered_list_G2)
    
    if getNumberOfVertices(G1) != getNumberOfVertices(G2):
        return False
    
    if getNumberOfEdges(G1) != getNumberOfEdges(G2):
        return False
    
    if getDegreeSequence(dtmp1) != getDegreeSequence(dtmp2):
        return False

    if ordered_list_G1 != ordered_list_G2:
        return False
    
    return True

# Function to test the graphs 
def testGraphs():
    print("\n\n======= TEST CASES ========")
    
    print("\n1. Pair satisfying criteria a and b, but failing on criterion c:")
    print("Are G_test1a and G_test1b isomorphic?", areGraphsIsomorphic(G_test1a, G_test1b))
    
    print("\n2. First pair satisfying criteria a, b, and c but not isomorphic:")
    print("Are G_test2a and G_test2b isomorphic?", areGraphsIsomorphic(G_test2a, G_test2b))
    
    print("\n3. Second pair satisfying criteria a, b, and c but not isomorphic:")
    print("Are G_test3a and G_test3b isomorphic?", areGraphsIsomorphic(G_test3a, G_test3b))
    
    print("\n4. First pair that passes all criteria (isomorphic):")
    print("Are G_test4a and G_test4b isomorphic?", areGraphsIsomorphic(G_test4a, G_test4b))
    
    print("\n5. Second pair that passes all criteria (isomorphic):")
    print("Are G_test5a and G_test5b isomorphic?", areGraphsIsomorphic(G_test5a, G_test5b))

# Run the tests
testGraphs()