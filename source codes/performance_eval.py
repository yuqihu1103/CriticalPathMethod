from critical_path_method import calculate_critical_path
from critical_path_brute_force import calculate_critical_path_brute
from critical_path_dijkstra import calculate_critical_path_dijkstra
from generate_random_tasks import generate_random_test
import time
import random

test_case_example = [
    {'id': 'A', 'duration': 7},
    {'id': 'B', 'duration': 9},
    {'id': 'C', 'duration': 12, 'dependencies': ['A']},
    {'id': 'D', 'duration': 8, 'dependencies': ['A', 'B']},
    {'id': 'E', 'duration': 9, 'dependencies': ['D']},
    {'id': 'F', 'duration': 6, 'dependencies': ['C', 'E']},
    {'id': 'G', 'duration': 5, 'dependencies': ['E']}
]

#generate 100 random test cases with 1-50 tasks.
random_test_cases = []
num_test_cases = 100
max_duration = 15
for _ in range(num_test_cases):
    num_tasks = random.randint(50, 100)
    test_case = generate_random_test(num_tasks, max_duration)
    random_test_cases.append(test_case)

# Define a function to measure execution time for a given method and test case
def measure_execution_time(method, test_case):
    start_time = time.time()
    critical_path = method(test_case)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Measure execution time for each method and each test case
results = []
for test_case in random_test_cases:
    result = {}
    result['test_case'] = test_case
    result['path_execution_time'] = measure_execution_time(calculate_critical_path, test_case)
    #result['brute_execution_time'] = measure_execution_time(calculate_critical_path_brute, test_case)
    result['optimized_execution_time'] = measure_execution_time(calculate_critical_path_dijkstra, test_case)
    results.append(result)

# Print the comparison results for each test case
for i, result in enumerate(results, 1):
    print(f"Test Case {i}:")
    print("Execution Time (Standard Method):", result['path_execution_time'])
    #print("Execution Time (Brute Force Method):", result['brute_execution_time'])
    print("Execution Time (Dijkstra's Method):", result['optimized_execution_time'])
    print()

# Accumulate execution times for each method
total_path_execution_time = 0
total_brute_execution_time = 0
total_optimized_execution_time = 0

for result in results:
    total_path_execution_time += result['path_execution_time']
    #total_brute_execution_time += result['brute_execution_time']
    total_optimized_execution_time += result['optimized_execution_time']

# Calculate average execution time for each method
average_path_execution_time = total_path_execution_time / len(results)
#average_brute_execution_time = total_brute_execution_time / len(results)
average_optimized_execution_time = total_optimized_execution_time / len(results)

# Print average execution times
print("Average Execution Time (Standard Method):", average_path_execution_time)
#print("Average Execution Time (Brute Force Method):", average_brute_execution_time)
print("Average Execution Time (Dijkstra's Method):", average_optimized_execution_time)
