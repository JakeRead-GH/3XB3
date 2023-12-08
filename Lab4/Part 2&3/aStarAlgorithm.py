import min_heap
import final_project_part1


def a_star(g, s, d, h):
    # g is a directed weighted graph from final_project_part1.py
    # s is the source node
    # d is the destination node
    # h is the heuristic function in the form of a map from nodes to floats

    pred = {}
    dist = {}
    q = min_heap.MinHeap([])
    nodes = list(g.adj.keys())


    for node in nodes:
        q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")

    q.decrease_key(s, 0 + h[s])


    while not q.is_empty():
        current_element = q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key - h[current_node]

        for neighbour in g.adj[current_node]:
            if dist[current_node] + g.w(current_node, neighbour) < dist[neighbour]:
                dist[neighbour] = dist[current_node] + g.w(current_node, neighbour)
                pred[neighbour] = current_node

                q.decrease_key(neighbour, dist[neighbour] + h[neighbour])
        if current_node == d:
            break
    return pred, dist[d]

if __name__ == "__main__":
    g = final_project_part1.DirectedWeightedGraph()
    g.add_node("a")
    g.add_node("b")
    g.add_node("c")
    g.add_node("cleft1")
    g.add_node("cleft2")
    g.add_node("cright1")
    g.add_node("cright2")
    g.add_node("d")

    g.add_edge("a", "b", 1)
    g.add_edge("b", "c", 1)
    g.add_edge("c", "cleft1", 1)
    g.add_edge("cleft1", "cleft2", 1)
    g.add_edge("c", "cright1", 1)
    g.add_edge("cright1", "cright2", 1)
    g.add_edge("cright2", "d", 1)

    h = {"a": 5, "b": 4, "c": 3, "cleft1": 4, "cleft2": 5, "cright1": 2, "cright2": 1, "d": 0}

    pred, dist = a_star(g, "a", "b", h)

    print(pred)
    print(dist)
