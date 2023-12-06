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

    return graph

def generateHeuristicForTarget(target):
    h = {}
    # Get target station object
    target_station = None
    for station in stations:
        if stations[station].name == target:
            target_station = stations[station]
            break

    # Calculate the heuristic for each node
    for station in stations:
        h[stations[station].name] = Station.getDistance(stations[station], target_station)

    return h

def all_combinations_experiment():
    g = generateLondonSubwayGraph()

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