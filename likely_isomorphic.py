# Kyrylo Kozlovskyi G00425385
# https://github.com/KyryloKozlovskyi/Graph-Isomorphism-Bipartite-Analysis
# Function to get the number of vertices in a graph
def getNumberOfVertices(graph):
    # Return the number of vertices by getting the length of the first element of the graph
    return len(graph[0])


# Function to get the number of edges in a graph
def getNumberOfEdges(graph):
    # Return the number of edges by getting the length of the second element of the graph
    return len(graph[1])


# Function to get the degree of each vertex in a graph
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
def getDegreeSequence(D):
    # Return the degree sequence by sorting the values of the degree dictionary in descending order
    return sorted(D.values(), reverse=True)


# Function to get the Adjacency List of a graph
def getAdjacencyList(V, E):
    # Create a dictionary to store the adjacency list of each vertex and initialize it with an empty set
    adjacency_list = {v: set() for v in V}
    # Iterate over the edges
    for e in E:
        # Add the vertices to the adjacency list of each other
        v1, v2 = e
        adjacency_list[v1].add(v2)
        adjacency_list[v2].add(v1)
    # Return the adjacency list
    return adjacency_list


# Function to get the degree sequence of a graph
def getAdjacentDegrees(V, E):
    # Get the adjacency list and the degree of each vertex
    adjacency_list = getAdjacencyList(V, E)
    # Get the degree of each vertex
    degrees = getDegree(V, E)
    # Create a dictionary to store the adjacent degrees of each vertex
    adjacent_degrees = {}
    # Iterate over the vertices
    for v in V:
        # Get the degrees of adjacent vertices and sort them in descending order
        adjacent_degrees[v] = sorted([degrees[adj] for adj in adjacency_list[v]], reverse=True)
    # Return the dictionary with the adjacent degrees
    return adjacent_degrees


# Function to convert a dictionary to a list of lists
def dictToList(degree_dict):
    # Extract the values (lists) from the dictionary
    values = list(degree_dict.values())
    # Sort the lists in descending order based on their first element or length
    ordered_list = sorted(values, reverse=True)
    # Return the ordered list
    return ordered_list


# Function to check if two graphs are isomorphic
def areGraphsIsomorphic(G1, G2):
    # Get the number of vertices for both graphs
    v1 = getNumberOfVertices(G1)
    v2 = getNumberOfVertices(G2)
    # Get the number of edges for both graphs
    e1 = getNumberOfEdges(G1)
    e2 = getNumberOfEdges(G2)
    # Calculate degrees for both graphs
    d1 = getDegree(G1[0], G1[1])
    d2 = getDegree(G2[0], G2[1])
    # Get the degree sequence for both graphs
    ds1 = getDegreeSequence(d1)
    ds2 = getDegreeSequence(d2)
    # Get the adjacent degrees for both graphs
    ad1 = getAdjacentDegrees(G1[0], G1[1])
    ad2 = getAdjacentDegrees(G2[0], G2[1])
    # Convert the adjacent degrees to list format for comparison
    o_ad1 = dictToList(ad1)
    o_ad2 = dictToList(ad2)
    # Print the results
    print("Number of vertices in G1:", v1)
    print("Number of vertices in G2:", v2)
    print("Number of edges in G1:", e1)
    print("Number of edges in G2:", e2)
    print("Degree of G1:", d1)
    print("Degree of G2:", d2)
    print("Degree sequence of G1:", ds1)
    print("Degree sequence of G2:", ds2)
    print("Adjacent degrees of G1:", o_ad1)
    print("Adjacent degrees of G2:", o_ad2)

    # Check for equal number of vertices
    if v1 != v2:
        print("(a) Failed: Different number of vertices")
        return False

    # Check for equal number of edges
    if e1 != e2:
        print("(b) Failed: Different number of edges")
        return False

    # Check for the same degree sequences
    if ds1 != ds2:
        print("(c) Failed: Different degree sequences")
        return False

    # Check for the same sorted list of lists of degrees of adjacent vertices
    if o_ad1 != o_ad2:
        print("(d) Failed: Different ordered lists of adjacent degrees")
        return False

    # All criteria passed
    return True


# 1. Pair satisfying criteria a and b, but failing on criteria c
# Graph 1
V_test1a = ["a", "b", "c", "d", "e"]
E_test1a = [{"a", "b"}, {"b", "c"}, {"c", "d"}, {"d", "e"}, {"e", "a"}]
# Graph 2
V_test1b = ["v", "w", "x", "y", "z"]
E_test1b = [{"v", "w"}, {"v", "x"}, {"v", "y"}, {"v", "z"}, {"w", "x"}]
# Create the graphs
G_test1a = (V_test1a, E_test1a)
G_test1b = (V_test1b, E_test1b)

# 2. Pair satisfying criteria a, b, and c but not isomorphic
# Graph 1
V_test2a = ["a", "b", "c", "d", "e", "f"]
E_test2a = [{"a", "b"}, {"a", "c"}, {"a", "f"}, {"b", "c"}, {"b", "d"}, {"b", "f"}, {"c", "d"}, {"d", "e"}, {"d", "f"},
            {"e", "f"}]
# Graph 2
V_test2b = ["g", "h", "k", "m", "n", "p"]
E_test2b = [{"g", "h"}, {"g", "m"}, {"g", "p"}, {"h", "k"}, {"h", "m"}, {"h", "p"}, {"k", "p"}, {"k", "m"}, {"m", "n"},
            {"n", "p"}]
# Create the graphs
G_test2a = (V_test2a, E_test2a)
G_test2b = (V_test2b, E_test2b)

# 3. Pair satisfying criteria a, b, and c but not isomorphic
# Graph 1
V_test3a = ["a", "b", "c", "d", "e", "f"]
E_test3a = [{"a", "b"}, {"a", "c"}, {"a", "f"}, {"b", "c"}, {"c", "d"}, {"d", "e"}, {"e", "f"}]
# Graph 2
V_test3b = ["v", "w", "x", "y", "z", "t"]
E_test3b = [{"v", "w"}, {"w", "x"}, {"x", "y"}, {"y", "z"}, {"z", "t"}, {"t", "v"}, {"v", "y"}]
# Create the graphs
G_test3a = (V_test3a, E_test3a)
G_test3b = (V_test3b, E_test3b)

# 4. Pair that passes all criteria (isomorphic)
# Graph 1
V_test4a = ["a", "b", "c", "d", "e", "f"]
E_test4a = [{"a", "b"}, {"a", "c"}, {"a", "f"}, {"b", "c"}, {"b", "d"}, {"b", "f"}, {"c", "d"}, {"d", "e"}, {"d", "f"},
            {"e", "f"}]
# Graph 2
V_test4b = ["g", "h", "k", "m", "n", "p"]
E_test4b = [{"g", "h"}, {"g", "k"}, {"g", "p"}, {"h", "k"}, {"h", "m"}, {"h", "p"}, {"k", "m"}, {"m", "n"}, {"m", "p"},
            {"n", "p"}]
# Create the graphs
G_test4a = (V_test4a, E_test4a)
G_test4b = (V_test4b, E_test4b)

# 5. Pair that passes all criteria (isomorphic)
# Graph 1
V_test5a = ["a", "b", "c", "d"]
E_test5a = [{"a", "b"}, {"b", "c"}, {"c", "d"}, {"d", "a"}]
# Graph 2
V_test5b = ["w", "x", "y", "z"]
E_test5b = [{"w", "x"}, {"x", "y"}, {"y", "z"}, {"z", "w"}]
# Create the graphs
G_test5a = (V_test5a, E_test5a)
G_test5b = (V_test5b, E_test5b)


# Function to test the graphs
def testGraphs():
    print("\n\n=============================== TEST CASES ================================")
    print("1. Pair satisfying criteria a and b, but failing on criteria c:")
    print("Are G1a and G1b isomorphic?", areGraphsIsomorphic(G_test1a, G_test1b))
    print("===========================================================================")
    print("2. Pair 1 satisfying criteria a, b, and c but not isomorphic:")
    print("Are G2a and G2b isomorphic?", areGraphsIsomorphic(G_test2a, G_test2b))
    print("===========================================================================")
    print("3. Pair 2 satisfying criteria a, b, and c but not isomorphic:")
    print("Are G3a and G3b isomorphic?", areGraphsIsomorphic(G_test3a, G_test3b))
    print("===========================================================================")
    print("4. Pair 1 that passes all criteria (isomorphic):")
    print("Are G4a and G4b isomorphic?", areGraphsIsomorphic(G_test4a, G_test4b))
    print("===========================================================================")
    print("5. Pair 2 that passes all criteria (isomorphic):")
    print("Are G5a and G5b isomorphic?", areGraphsIsomorphic(G_test5a, G_test5b))
    print("===========================================================================")


# Run the tests
testGraphs()
