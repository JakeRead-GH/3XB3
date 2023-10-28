import graph
from collections import deque


def BetterDFS1(G, node1, node2):    # An improvement on the broken dfs provided in the graph.py file
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if not marked[node]:            # Added this line, which should have been in the original
                    if node == node2:
                        return True
                    S.append(node)
    return False


def BFS2(g, n1, n2):
    Q = deque([[n1]])
    marked = {n1: True}

    for node in g.adj:
        if node != n1:
            marked[node] = False

    while len(Q) != 0:
        current_path = Q.popleft()

        for node in g.adj[current_path[-1]]:
            if node == n2:
                current_path.append(node)
                return current_path

            if not marked[node]:
                new_path = current_path.copy()
                new_path.append(node)
                Q.append(new_path)
                marked[node] = True

    return []


def DFS2(g, n1, n2):
    S = [[n1]]
    marked = {}

    for node in g.adj:
        marked[node] = False

    while len(S) != 0:
        current_path = S.pop()
        current_node = current_path[-1]

        if not marked[current_node]:
            marked[current_node] = True
            for node in g.adj[current_node]:
                if node == n2:
                    current_path.append(node)
                    return current_path

                if not marked[node]:
                    new_path = current_path.copy()
                    new_path.append(node)
                    S.append(new_path)

    return []


def BFS3(g, n):
    pred_dict = {}
    Q = deque([n])
    marked = {n: True}

    for node in g.adj:
        if node != n:
            marked[node] = False

    while len(Q) != 0:
        current_node = Q.popleft()

        for node in g.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                pred_dict[node] = current_node

    return pred_dict


def DFS3(g, node1):
    pred_dict = {}
    S = [node1]
    marked = {}

    for node in g.adj:
        marked[node] = False

    while len(S) != 0:
        current_node = S.pop()

        if not marked[current_node]:
            marked[current_node] = True

            for node in g.adj[current_node]:
                if not marked[node]:
                    S.append(node)
                    pred_dict[node] = current_node

    return pred_dict
