import min_heap
from final_project_part1 import DirectedWeightedGraph
from aStarAlgorithm import a_star
from final_project_part1 import dijkstra
import csv
import timeit
import matplotlib.pyplot as plt

class Station:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        # self.line = line

    @staticmethod
    def getDistance(station1, station2):
        return ((station1.latitude - station2.latitude)**2 + (station1.longitude - station2.longitude)**2)**0.5
    
    def getDistanceByAxis(station1, station2):
        return (abs(station1.latitude - station2.latitude), abs(station1.longitude - station2.longitude))
    
class Connection:
    def __init__(self, station1, station2, line):
        self.station1 = station1
        self.station2 = station2
        self.line = line
    
    def getLine(self):
        return self.line

class LondonSubwayGraph(DirectedWeightedGraph):
    stations = {}
    connections = {}

    def __init__(self):
        super().__init__()

        # Load all the stations
        with open("london_stations.csv") as f:
            csv_reader = csv.reader(f, delimiter=",")
            next(csv_reader, None)
            for row in csv_reader:
                # Store stations in a dictionary for easy access
                self.stations[row[0]] = Station(row[3], float(row[1]), float(row[2]))
                self.add_node(row[3])

        # Load all the connections
        with open("london_connections.csv") as f:
            csv_reader = csv.reader(f, delimiter=",")
            next(csv_reader, None)
            for row in csv_reader:
                station1 = self.stations[row[0]]
                station2 = self.stations[row[1]]
                dist = Station.getDistance(station1, station2)
                self.add_edge(station1.name, station2.name, dist)
                self.add_edge(station2.name, station1.name, dist)
                self.connections[(station1.name, station2.name)] = row[2]
                self.connections[(station2.name, station1.name)] = row[2]

    def generateHeuristicForTarget(self, target):
        h = {}
        # Get target station object
        target_station = None
        for station in self.stations:
            if self.stations[station].name == target:
                target_station = self.stations[station]
                break

        # Calculate the heuristic for each node
        for station in self.stations:
            h[self.stations[station].name] = Station.getDistance(self.stations[station], target_station)

        return h
    
    def generateHeuristicForSource(self, source):
        h = {}
        # Get source station object
        source_station = None
        for station in self.stations:
            if self.stations[station].name == source:
                source_station = self.stations[station]
                break

        # Calculate the heuristic for each node
        for station in self.stations:
            h[self.stations[station].name] = Station.getDistance(self.stations[station], source_station)

        return h
    
    def getName(self, id):
        return self.stations[id].name
    
    def number_of_stations(self):
        return len(self.stations)

g = LondonSubwayGraph()

# SOURCE = "Greenford"
# DESTINATION = "North Ealing"

# # Run A* on the graph
# pred, dist = a_star(g, SOURCE, DESTINATION, g.generateHeuristicForTarget(DESTINATION))
# print(pred)
# print(dist)

# pred, dist = dijkstra(g, SOURCE, DESTINATION)
# print(pred)
# print(dist)

def get_all_stations_on_line(graph, source, destination, line):
    stations = []

    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(graph.adj.keys())

    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        # want to only go through the stations on the same line
        for neighbour in graph.adj[current_node]:
            if (current_node, neighbour) not in graph.connections or graph.connections[(current_node, neighbour)] != line:
                continue
            if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                if neighbour not in stations:
                    stations.append(neighbour)
        if current_node == destination:
            break

    if neighbour not in stations:
        stations.append(neighbour)

    return stations

# Function to perform the experiment for all combinations and plot the results
def run_experiment_and_plot():
    graph = LondonSubwayGraph()

    dijkstra_runtimes = []
    a_star_runtimes = []

    source_id = '1'

    steps = 50

    stations_range = range(2, graph.number_of_stations()+2)
    # Station 189 doesn't exist
    stations_range = list(stations_range)
    stations_range.remove(189)

    for destination_id in stations_range:
        print(f"Running Dijkstra experiment for {source_id} to {destination_id}")
        dijkstra_runtimes_step = []

        # Measure Dijkstra's algorithm runtime
        for _ in range(steps):
            dijkstra_time = timeit.timeit(lambda: dijkstra(graph, graph.getName(source_id), graph.getName(str(destination_id))), number=1)
            dijkstra_runtimes_step.append(dijkstra_time)
        
        dijkstra_runtimes.append(sum(dijkstra_runtimes_step)/len(dijkstra_runtimes_step))

    for destination_id in stations_range:
        print(f"Running A* experiment for {source_id} to {destination_id}")
        a_star_runtimes_step = []

        h = graph.generateHeuristicForSource(graph.getName(source_id))

        # Measure A* algorithm runtime
        for _ in range(steps):
            a_star_time = timeit.timeit(lambda: a_star(graph, graph.getName(source_id), graph.getName(str(destination_id)), h), number=1)
            a_star_runtimes_step.append(a_star_time)

        a_star_runtimes.append(sum(a_star_runtimes_step)/len(a_star_runtimes_step))

    # Plot the results
    plt.plot(dijkstra_runtimes, label='Dijkstra')
    plt.plot(a_star_runtimes, label='A*')
    plt.xlabel('Destination Station')
    plt.ylabel('Runtime (seconds)')
    plt.xticks(range(len(stations_range)), stations_range, rotation=90, fontsize=5)
    plt.legend()
    plt.title('Dijkstra vs A* Runtimes for Subway Station Pairs')
    plt.show()

    # Find which algorithm is faster on average
    dijkstra_average = sum(dijkstra_runtimes)/len(dijkstra_runtimes)
    a_star_average = sum(a_star_runtimes)/len(a_star_runtimes)

    print(f"Dijkstra average: {dijkstra_average*1000}")
    print(f"A* average: {a_star_average*1000}")

def one_line_experiment(runs_per_step):
    # LINE_NUM = '8'
    # SOURCE = 'Amersham'
    # FINAL_DESTINATION_ID = 'Aldgate'

    LINE_NUM = '2'
    SOURCE = 'West Ruislip'
    FINAL_DESTINATION_ID = 'Epping'
    
    graph = LondonSubwayGraph()

    dijkstra_runtimes = []
    a_star_runtimes = []

    stations_range = get_all_stations_on_line(graph, SOURCE, FINAL_DESTINATION_ID, LINE_NUM)

    for destination in stations_range:
        print(f"Running Dijkstra experiment for {SOURCE} to {destination}")
        dijkstra_runtimes_step = []

        # Measure Dijkstra's algorithm runtime
        for _ in range(runs_per_step):
            dijkstra_time = timeit.timeit(lambda: dijkstra(graph, SOURCE, destination), number=1)
            dijkstra_runtimes_step.append(dijkstra_time)
        
        dijkstra_runtimes.append(sum(dijkstra_runtimes_step)/len(dijkstra_runtimes_step))

    for destination in stations_range:
        print(f"Running A* experiment for {SOURCE} to {destination}")
        a_star_runtimes_step = []

        h = graph.generateHeuristicForSource(SOURCE)

        # Measure A* algorithm runtime
        for _ in range(runs_per_step):
            a_star_time = timeit.timeit(lambda: a_star(graph, SOURCE, destination, h), number=1)
            a_star_runtimes_step.append(a_star_time)

        a_star_runtimes.append(sum(a_star_runtimes_step)/len(a_star_runtimes_step))

    # Plot the results
    plt.plot(dijkstra_runtimes, label='Dijkstra')
    plt.plot(a_star_runtimes, label='A*')
    plt.xlabel('Destination Station')
    plt.ylabel('Runtime (seconds)')
    plt.xticks(range(len(stations_range)), stations_range, rotation=90, fontsize=5)
    plt.legend()
    plt.title('Dijkstra vs A* Runtimes for Subway Station Pairs')
    plt.show()

    # Find which algorithm is faster on average
    dijkstra_average = sum(dijkstra_runtimes)/len(dijkstra_runtimes)
    a_star_average = sum(a_star_runtimes)/len(a_star_runtimes)

    print(f"Dijkstra average: {dijkstra_average*1000}")
    print(f"A* average: {a_star_average*1000}")

def adjacent_lines_experiment(runs_per_step):
    SOURCE = 'Hatton Cross'
    LINE_ONE = '10'
    LINE_TWO = '4'
    FINAL_DEST_ONE = 'Russell Square'
    FINAL_DEST_TWO = 'Tower Hill'
    
    graph = LondonSubwayGraph()

    dijkstra_runtimes = []
    a_star_runtimes = []
    dijkstra_runtimes_2 = []
    a_star_runtimes_2 = []

    stations_range = get_all_stations_on_line(graph, SOURCE, FINAL_DEST_ONE, LINE_ONE)

    for destination in stations_range:
        print(f"Running Dijkstra experiment for {SOURCE} to {destination}")
        dijkstra_runtimes_step = []

        # Measure Dijkstra's algorithm runtime
        for _ in range(runs_per_step):
            dijkstra_time = timeit.timeit(lambda: dijkstra(graph, SOURCE, destination), number=1)
            dijkstra_runtimes_step.append(dijkstra_time)
        
        dijkstra_runtimes.append(sum(dijkstra_runtimes_step)/len(dijkstra_runtimes_step))

    for destination in stations_range:
        print(f"Running A* experiment for {SOURCE} to {destination}")
        a_star_runtimes_step = []

        h = graph.generateHeuristicForSource(SOURCE)

        # Measure A* algorithm runtime
        for _ in range(runs_per_step):
            a_star_time = timeit.timeit(lambda: a_star(graph, SOURCE, destination, h), number=1)
            a_star_runtimes_step.append(a_star_time)

        a_star_runtimes.append(sum(a_star_runtimes_step)/len(a_star_runtimes_step))

    # Plot the results
    plt.plot(dijkstra_runtimes, label='Dijkstra (Line {})'.format(LINE_ONE))
    plt.plot(a_star_runtimes, label='A* (Line {})'.format(LINE_ONE))
    plt.xlabel('Destination Station')
    plt.ylabel('Runtime (seconds)')
    plt.xticks(range(len(stations_range)), stations_range, rotation=90, fontsize=5)
    plt.legend()
    plt.title('Dijkstra vs A* Runtimes for Subway Station Pairs')
    plt.show()

    dijkstra_average = sum(dijkstra_runtimes)/len(dijkstra_runtimes)
    a_star_average = sum(a_star_runtimes)/len(a_star_runtimes)

    print(f"Dijkstra average ({LINE_ONE}): {dijkstra_average*1000}")
    print(f"A* average ({LINE_ONE}): {a_star_average*1000}")

    get_all_stations_on_line(graph, SOURCE, FINAL_DEST_TWO, LINE_TWO)

    for destination in stations_range:
        print(f"Running Dijkstra experiment for {SOURCE} to {destination}")
        dijkstra_runtimes_step = []

        # Measure Dijkstra's algorithm runtime
        for _ in range(runs_per_step):
            dijkstra_time = timeit.timeit(lambda: dijkstra(graph, SOURCE, destination), number=1)
            dijkstra_runtimes_step.append(dijkstra_time)
        
        dijkstra_runtimes_2.append(sum(dijkstra_runtimes_step)/len(dijkstra_runtimes_step))

    for destination in stations_range:
        print(f"Running A* experiment for {SOURCE} to {destination}")
        a_star_runtimes_step = []

        h = graph.generateHeuristicForSource(SOURCE)

        # Measure A* algorithm runtime
        for _ in range(runs_per_step):
            a_star_time = timeit.timeit(lambda: a_star(graph, SOURCE, destination, h), number=1)
            a_star_runtimes_step.append(a_star_time)

        a_star_runtimes_2.append(sum(a_star_runtimes_step)/len(a_star_runtimes_step))

    # Plot the results
    plt.plot(dijkstra_runtimes_2, label='Dijkstra (Line {})'.format(LINE_TWO))
    plt.plot(a_star_runtimes_2, label='A* (Line {})'.format(LINE_TWO))
    plt.xlabel('Destination Station')
    plt.ylabel('Runtime (seconds)')
    plt.xticks(range(len(stations_range)), stations_range, rotation=90, fontsize=5)
    plt.legend()
    plt.title('Dijkstra vs A* Runtimes for Subway Station Pairs')
    plt.show()

    # Find which algorithm is faster on average
    dijkstra_average = sum(dijkstra_runtimes_2)/len(dijkstra_runtimes_2)
    a_star_average = sum(a_star_runtimes_2)/len(a_star_runtimes_2)

    print(f"Dijkstra average ({LINE_TWO}): {dijkstra_average*1000}")
    print(f"A* average ({LINE_TWO}): {a_star_average*1000}")

def many_transfers_experiment(runs_per_step):
    # SOURCE_ID = '116' # Hatton Cross
    SOURCE_ID = '108' # Gunnersbury
    
    graph = LondonSubwayGraph()

    dijkstra_runtimes = []
    dijkstra_pred_len = []
    a_star_runtimes = []
    a_star_pred_len = []
    stations_range = []
    
    # Create a bounding box based off the source station and
    # only include stations outside of that box.
    # Targeting top left as that is the furthest from lin
    min_dist_y, _ = Station.getDistanceByAxis(graph.stations[SOURCE_ID], graph.stations['239']) # South Ruislip
    _, max_dist_x = Station.getDistanceByAxis(graph.stations[SOURCE_ID], graph.stations['157']) # London Bridge
    
    for station in graph.stations:
        y, x = Station.getDistanceByAxis(graph.stations[SOURCE_ID], graph.stations[station])
        if y > min_dist_y and x < max_dist_x:
            stations_range.append(station)

    print("Stations range:", stations_range)

    source = graph.getName(SOURCE_ID)

    for destination_id in stations_range:
        print(f"Running Dijkstra experiment for {SOURCE_ID} to {destination_id}")
        dijkstra_runtimes_step = []

        dijkstra_pred_len.append(len(dijkstra(graph, source, graph.getName(str(destination_id)))[0]))

        # Measure Dijkstra's algorithm runtime
        for _ in range(runs_per_step):
            start = timeit.default_timer()
            dijkstra(graph, source, graph.getName(str(destination_id)))
            end = timeit.default_timer()
            dijkstra_runtimes_step.append(end - start)
        
        dijkstra_runtimes.append(sum(dijkstra_runtimes_step)/len(dijkstra_runtimes_step))

    for destination_id in stations_range:
        print(f"Running A* experiment for {SOURCE_ID} to {destination_id}")
        a_star_runtimes_step = []

        h = graph.generateHeuristicForTarget(graph.getName(destination_id))

        a_star_pred_len.append(len(a_star(graph, source, graph.getName(str(destination_id)), h)[0]))

        # Measure A* algorithm runtime
        for _ in range(runs_per_step):
            start = timeit.default_timer()
            a_star(graph, source, graph.getName(str(destination_id)), h)
            end = timeit.default_timer()
            a_star_runtimes_step.append(end - start)

        a_star_runtimes.append(sum(a_star_runtimes_step)/len(a_star_runtimes_step))
    
    # Average pred len
    dijkstra_pred_average = sum(dijkstra_pred_len)/len(dijkstra_pred_len)
    a_star_pred_average = sum(a_star_pred_len)/len(a_star_pred_len)
    print(f"Dijkstra pred average: {dijkstra_pred_average}")
    print(f"A* pred average: {a_star_pred_average}")

    # Plot the results
    plt.plot(dijkstra_runtimes, label='Dijkstra')
    plt.plot(a_star_runtimes, label='A*')
    plt.xlabel('Destination Station')
    plt.ylabel('Runtime (seconds)')
    plt.xticks(range(len(stations_range)), stations_range, rotation=90, fontsize=5)
    plt.legend()
    plt.title('Dijkstra vs A* Runtimes for Subway Station Pairs')
    plt.show()

    # Find which algorithm is faster on average
    dijkstra_average = sum(dijkstra_runtimes)/len(dijkstra_runtimes)
    a_star_average = sum(a_star_runtimes)/len(a_star_runtimes)

    print(f"Dijkstra average: {dijkstra_average*1000}")
    print(f"A* average: {a_star_average*1000}")

if __name__ == "__main__":
    one_line_experiment(500)
    # adjacent_lines_experiment(1000)
    # many_transfers_experiment(500)