import graph
import graphHelper



def is_independent_set(g, set):
    for start in g.adj:
        for end in g.adj[start]:
            if (start in set and end in set):
                return False
    return True


def MIS(g):
    nodes = [i for i in range(g.number_of_nodes())]
    subsets = graph.power_set(nodes)
    max_set = {}
    for subset in subsets:
        if is_independent_set(g, subset):
            if len(subset) > len(max_set):
                max_set = subset
    return max_set


g = graphHelper.random_graph(10, 10)
print(g.adj)

print("MIS:", MIS(g))
print("MVC:", graph.MVC(g))
