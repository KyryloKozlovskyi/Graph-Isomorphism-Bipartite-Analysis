import numpy as np # Import numpy library for matrix operations

# Graph 1 consists of a list of vertices and a list of sets of edges
V1 = [ "a", "b", "c", "d", "e", "f" ]
E1 = [ {"a", "b"}, {"a", "c"}, {"a", "f"}, {"b", "c"}, {"b", "d"}, {"b", "f"}, {"c", "d"}, {"d", "e"}, {"d",
"f"}, {"e", "f"} ]

# Graph 1 consists of a list of vertices and a list of sets of edges
V2 = ["g", "h", "k", "m", "n", "p"]
E2 = [ {"g", "h"}, {"g", "m"}, {"g", "p"}, {"h", "k"}, {"h", "m"}, {"h", "p"}, {"k", "p"}, {"k", "m"}, {"m",
"n"}, {"n", "p"} ]

# Create the graphs as tuples
G1 = (V1, E1)
G2 = (V2, E2)

# Part 1 – Likely Isomorphic
# Create a number of methods to address the following problem.
# Determine whether two graphs are likely to be isomorphic to one another.

# a. They have an equal number of vertices.
# b. They have an equal number of edges.
# c. They have the same degree sequences.
# d. They produce the same sorted list of lists of degrees of adjacent vertices

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

# Function to check if two graphs are isomorphic
# Considering the graphs are tuples with the first (0) element being the list of vertices
# and the second (1) element being the list of edges
def areGraphsIsomorphic(G1, G2):
    dtmp1 = getDegree(G1[0], G1[1])
    dtmp2 = getDegree(G2[0], G2[1])
    
    if getNumberOfVertices(G1) != getNumberOfVertices(G2):
        return False
    
    if getNumberOfEdges(G1) != getNumberOfEdges(G2):
        return False
    
    if getDegreeSequence(dtmp1) != getDegreeSequence(dtmp2):
        return False
    
    return True

# Test cases
print("Number of vertices in G1:", getNumberOfVertices(G1))
print("Number of edges in G1:", getNumberOfEdges(G1))
print("Degree of vertices in G1:", getDegree(G1[0], G1[1]))
print("Degree sequence of G1:", getDegreeSequence(getDegree(G1[0], G1[1])))
print("----------------------------------------------------------------")
print("Number of vertices in G2:", getNumberOfVertices(G2))
print("Number of edges in G2:", getNumberOfEdges(G2))
print("Degree of vertices in G2:", getDegree(G2[0], G2[1]))
print("Degree sequence of G2:", getDegreeSequence(getDegree(G2[0], G2[1])))
print("----------------------------------------------------------------")
print("Are G1 and G2 isomorphic?", areGraphsIsomorphic(G1, G2))