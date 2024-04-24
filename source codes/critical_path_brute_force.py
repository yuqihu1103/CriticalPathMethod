def build_graph(tasks):
    graph = {}
    for task in tasks:
        graph[task['id']] = {'duration': task['duration'], 'neighbors': [], 'incoming': 0}
    for task in tasks:
        if task.get('dependencies'):
            for dependency in task['dependencies']:
                graph[dependency]['neighbors'].append(task['id'])
                graph[task['id']]['incoming'] += 1
    return graph

def find_longest_path(graph, current_node, visited):
    visited.add(current_node)
    max_duration = 0
    critical_path = [current_node]
    for neighbor in graph[current_node]['neighbors']:
        duration, path = find_longest_path(graph, neighbor, visited)
        if duration + graph[current_node]['duration'] > max_duration:
            max_duration = duration + graph[current_node]['duration']
            critical_path = [current_node] + path
    return max_duration, critical_path

def calculate_critical_path_brute(tasks):
    graph = build_graph(tasks)
    longest_duration = 0
    critical_path = []
    for node in graph:
        for node in graph:
            duration, path = find_longest_path(graph, node, set())
            if duration > longest_duration:
                longest_duration = duration
                critical_path = path
    return critical_path

tasks = [
    {'id': 'A', 'duration': 7},
    {'id': 'B', 'duration': 9},
    {'id': 'C', 'duration': 12, 'dependencies': ['A']},
    {'id': 'D', 'duration': 8, 'dependencies': ['A', 'B']},
    {'id': 'E', 'duration': 9, 'dependencies': ['D']},
    {'id': 'F', 'duration': 6, 'dependencies': ['C', 'E']},
    {'id': 'G', 'duration': 5, 'dependencies': ['E']}
]


critical_path = calculate_critical_path_brute(tasks)
print("Critical Path:", critical_path)
