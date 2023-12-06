from final_project_part1 import DirectedWeightedGraph
from aStarAlgorithm import a_star
from final_project_part1 import dijkstra
import csv
import timeit
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

stations = {}

class Station:
    def __init__(self, name, latitude, longitude, line):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.line = line

    @staticmethod
    def getDistance(station1, station2):
        return ((station1.latitude - station2.latitude)**2 + (station1.longitude - station2.longitude)**2)**0.5

def generateLondonSubwayGraph():
    graph = DirectedWeightedGraph()
    # Load all the stations
    with open("london_stations.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            # Store stations in a dictionary for easy access
            stations[row[0]] = Station(row[3], float(row[1]), float(row[2]), int())
            graph.add_node(row[3])

    # Load all the connections
    with open("london_connections.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            station1 = stations[row[0]]
            station2 = stations[row[1]]
            dist = Station.getDistance(station1, station2)
            graph.add_edge(station1.name, station2.name, dist)
            graph.add_edge(station2.name, station1.name, dist)
            # if station1.name not in heuristics:
            #     heuristics[station1.name] = {}
            # if station2.name not in heuristics:
            #     heuristics[station2.name] = {}

    # Calculate the heuristics for each node
    # for station1 in stations:
    #     for station2 in stations:
    #         dist = Station.getDistance(stations[station1], stations[station2])
    #         if station1 not in heuristics:
    #             heuristics[station1] = {}
    #         heuristics[stations[station1].name][stations[station2].name] = dist

    return graph

def generateHeuristicForTarget(graph, target):
    h = {}
    # get target station object
    target_station = None
    for station in stations:
        if stations[station].name == target:
            target_station = stations[station]
    for station in stations:
        # Calculate the distance from the station to the target
        h[stations[station].name] = Station.getDistance(stations[station], target_station)
    return h

def all_combinations_experiment():
    g = generateLondonSubwayGraph()
    # Make a 3d graph with x = source, y = destination, z = time

    # x = []
    # y = []
    # z = []
    # for source in g.adj:
    #     for destination in g.adj:
    #         if source != destination:
    #             x.append(source)
    #             y.append(destination)
    #             start = timeit.default_timer()
    #             dijkstra(g, source, destination)
    #             end = timeit.default_timer()
    #             z.append(end - start)
    #             print(source, destination)
    
    # fig = plt.figure()
    # ax = plt.axes(projection='3d')
    # ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')
    # ax.set_title('Dijkstra')
    # ax.set_xlabel('Source')
    # ax.set_ylabel('Destination')
    # ax.set_zlabel('Time (s)')
    # plt.show()

    # plt.title("London Subway: Dijkstra vs A*")
    # plt.xlabel("Iteration")
    # plt.ylabel("Time (s)")

    
    # combinations = []
    # for source in g.adj:
    #     for destination in g.adj:
    #         if source != destination:
    #             combinations.append((source, destination))

    # # Dijkstra
    # print("Dijkstra")
    # time = []
    # i = 0
    # for source in g.adj:
    #     for destination in g.adj:
    #         if source != destination:
    #             start = timeit.default_timer()
    #             dijkstra(g, source, destination)
    #             end = timeit.default_timer()
    #             time.append(end - start)
    #     print(i)
    #     i+=1
    # plt.plot(combinations, time)
    # # A*
    # print("A*")
    # time = []
    # i = 0
    # for source in g.adj:
    #     for destination in g.adj:
    #         if source != destination:
    #             start = timeit.default_timer()
    #             a_star(g, source, destination, heuristics[destination])
    #             end = timeit.default_timer()
    #             time.append(end - start)
        
    #     print(i)
    #     i+=1
    # plt.plot(combinations, time)
    # plt.legend(["Dijkstra", "A*"])
    # plt.show()

SOURCE = "Greenford"
DESTINATION = "North Ealing"

g = generateLondonSubwayGraph()
h = generateHeuristicForTarget(g, DESTINATION)

# Run A* on the graph
pred, dist = a_star(g, SOURCE, DESTINATION, h)

print(pred)
print(dist)

pred, dist = dijkstra(g, SOURCE, DESTINATION)
print(pred)
print(dist)

# all_combinations_experiment()