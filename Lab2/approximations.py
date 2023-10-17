import graph
import copy
import random

# =================================================================
# =======================Helper Functions==========================
# =================================================================

def remove_edges(G, vertex):
    l = G.adj[vertex].copy()
    for node in l:
        G.adj[vertex].remove(node)
        G.adj[node].remove(vertex)

def get_highest_degree_vertex(G):
    highest_degree = 0
    highest_degree_node = None
    for node in G.adj:
        if len(G.adj[node]) > highest_degree:
            highest_degree = len(G.adj[node])
            highest_degree_node = node
    return highest_degree_node

def get_random_edge(G):
    random_node = random.randint(0, G.number_of_nodes() - 1)
    while len(G.adj[random_node]) == 0:
        random_node = random.randint(0, G.number_of_nodes() - 1)
    random_edge = random.choice(list(G.adj[random_node]))
    return (random_node, random_edge)

# =================================================================
# ==================Vertex Cover Approximations====================
# =================================================================

def approx1(G):
    # 1. Start with empty set C = {}
    # 2. Find the vertex with the highest degree in G, call this vertex v
    # 3. Add v to C
    # 4. Remove all edges incident to node v from G
    # 5. If C is a Vertex Cover return C, else go to step 2
    C = []
    temp_G = copy.deepcopy(G)
    while not graph.is_vertex_cover(temp_G, C):
        v = get_highest_degree_vertex(temp_G)
        C.append(v)
        remove_edges(temp_G, v)
    return C

def approx2(G):
    # 1. Start with empty set C = {}
    # 2. Select a vertex randomly from G which is not in C, call this vertex v
    # 3. Add v to C
    # 4. If C is a Vertex Cover return C, else go to step 2
    C = []
    while not graph.is_vertex_cover(G, C):
        v = random.randint(0, G.number_of_nodes() - 1)
        while v in C:
            v = random.randint(0, G.number_of_nodes() - 1)
        C.append(v)
    return C

def approx3(G):
    # 1. Start with empty set C = {}
    # 2. Select an edge randomly from G, call this edge (u,v)
    # 3. Add u and v to C
    # 4. Remove all edges incident to nodes u and v from G
    # 5. If C is a Vertex Cover return C, else go to step 2
    C = []
    temp_G = copy.deepcopy(G)
    while not graph.is_vertex_cover(temp_G, C):
        edge = get_random_edge(temp_G)
        C.append(edge[0])
        C.append(edge[1])
        remove_edges(temp_G, edge[0])
        remove_edges(temp_G, edge[1])
    return C

g = graph.Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

print(graph.MVC(g))
print(approx1(g))
print(approx2(g))
print(approx3(g))
