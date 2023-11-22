import min_heap


def dijkstra_approx(g, source, k):
    pred = {}
    dist = {}
    times_relaxed = {}
    q = min_heap.MinHeap([])
    nodes = list(g.adj.keys())

    for node in nodes:
        q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
        times_relaxed[node] = 0

    q.decrease_key(source, 0)

    while not q.is_empty():
        current_element = q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in g.adj[current_node]:
            if times_relaxed[neighbour] < k and dist[current_node] + g.w(current_node, neighbour) < dist[neighbour]:
                q.decrease_key(neighbour, dist[current_node] + g.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + g.w(current_node, neighbour)
                pred[neighbour] = current_node
                times_relaxed[neighbour] += 1

    return dist


def bellman_ford_approx(g, source, k):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    times_relaxed = {}
    nodes = list(g.adj.keys())

    # Initialize distances
    for node in nodes:
        dist[node] = float("inf")
        times_relaxed[node] = 0
    dist[source] = 0

    # Meat of the algorithm
    for _ in range(g.number_of_nodes()):
        for node in nodes:
            for neighbour in g.adj[node]:
                if times_relaxed[neighbour] < k and dist[neighbour] > dist[node] + g.w(node, neighbour):
                    dist[neighbour] = dist[node] + g.w(node, neighbour)
                    pred[neighbour] = node
                    times_relaxed[neighbour] += 1

    return dist
