import networkx as nx

def calculate_critical_path(tasks):
    
    # establish a graph with each task as a node and dependencies as directed edges
    G = nx.DiGraph()
    for task in tasks:
        G.add_node(task['id'], duration=task['duration'])
        for dependency in task.get('dependencies', []):
            G.add_edge(dependency, task['id'])
    
    # earliest start times
    for node in nx.topological_sort(G):
        # if first task(no predecessors), start at 0
        if len(list(G.predecessors(node))) == 0:
            G.nodes[node]['earliest_start'] = 0
        else:
            max_earliest = max([G.nodes[p]['earliest_start'] + G.nodes[p]['duration'] for p in G.predecessors(node)])
            G.nodes[node]['earliest_start'] = max_earliest
    
    # whole project finishing time
    finishing_time = max([G.nodes[node]['earliest_start'] + G.nodes[node]['duration'] for node in G.nodes])
        
    # latest finishing time in reverse order
    for node in reversed(list(nx.topological_sort(G))):
        # if last task(no successors), latest finishing = whole project finishing time
        if len(list(G.successors(node))) == 0:
            G.nodes[node]['latest_finish'] = finishing_time
        else:
            min_latest = min([G.nodes[s]['latest_finish'] - G.nodes[s]['duration'] for s in G.successors(node)])
            G.nodes[node]['latest_finish'] = min_latest
    
    # critical path -> zero slack time
    critical_path = []
    for node in G.nodes:
        if G.nodes[node]['earliest_start'] == G.nodes[node]['latest_finish'] - G.nodes[node]['duration']:
            critical_path.append(node)
    
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


critical_path = calculate_critical_path(tasks)
print("Critical Path:", critical_path)