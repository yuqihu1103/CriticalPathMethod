import heapq

def calculate_critical_path_dijkstra(tasks):
    #helper function to model the tasks as a graph
    def build_graph(tasks):
        graph = {}
        for task in tasks:
            graph[task['id']] = {'duration': task['duration'], 'neighbors': []}
        for task in tasks:
            if 'dependencies' in task:
                for dep_id in task['dependencies']:
                    graph[dep_id]['neighbors'].append(task['id'])
        return graph

    #modified dijkstra's algorithms
    #given a start node, find shortest time to complete each task (if possible)
    #also keep record of the previous node to find path later
    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        queue = [(0, start)]
        previous = {node: None for node in graph}
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor in graph[current_node]['neighbors']:
                distance = current_distance + graph[current_node]['duration']
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))
        for node in distances.keys():
            distances[node] += graph[node]["duration"]
        return distances, previous

    #helper function to find critical path given distances and previous
    def get_critical_path(distances, previous):
        max_distance = -1
        for node, distance in distances.items():
            if distance != float("inf") and distance > max_distance:
                max_distance, critical_node = distance, node
        path = [critical_node]
        while previous[critical_node]:
            path.append(previous[critical_node])
            critical_node = previous[critical_node]
        return max_distance, path[::-1]

    #build graph from tasks
    graph = build_graph(tasks)

    #for each task, suppose begin with it and find critical path
    #and find and return the longest of such path
    paths = []
    for task in tasks:
        start_node = task['id']
        distances, previous = dijkstra(graph, start_node)
        paths.append(get_critical_path(distances, previous))
    paths.sort()
    return paths[-1]

tasks = [
    {'id': 'A', 'duration': 7},
    {'id': 'B', 'duration': 9},
    {'id': 'C', 'duration': 12, 'dependencies': ['A']},
    {'id': 'D', 'duration': 8, 'dependencies': ['A', 'B']},
    {'id': 'E', 'duration': 9, 'dependencies': ['D']},
    {'id': 'F', 'duration': 6, 'dependencies': ['C', 'E']},
    {'id': 'G', 'duration': 5, 'dependencies': ['E']}
]


critical_path = calculate_critical_path_dijkstra(tasks)
print("Critical Path:", critical_path)
