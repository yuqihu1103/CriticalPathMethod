## What are in the source codes

### critical_path_method.py
Contains the implementation of **calculate_critical_path(tasks)**
The function takes an array of tasks and finds the critical path using the Critical Path Method.
Main program will calculate and print the critical path of an example input.

### critical_path_brute_force.py
Contains the implementation of **calculate_critical_path_brute(tasks)**
The function takes an array of tasks and finds the critical path using Brute Force.
Main program will calculate and print the critical path of an example input.

### critical_path_dijkstra.py
Contains the implementation of **critical_path_dijkstra(tasks)**
The function takes an array of tasks and finds the critical path using Brute Force with optimization with Dijkstra's.
Main program will calculate and print the critical path of an example input.

### generate_random_tasks.py
Contains the implementation of **generate_random_test(num_tasks, max_duration)**
The function generates a random list of tasks with given size and max_duration.
Main program will generate and print a list of tasks of size 20 and max_duration 15.

### performance_eval.py
Imports the functions from the files above. Uses generate_random_test to test the performance of the 3 methods.
The main program generates 100 test cases with 1-50 tasks and use each of the 3 methods on test cases.
The execution of each method will be timed.

## How to use the code

### Prerequisites
You need to have the latest version of Python installed.
You need to install the networkx package in addition if you haven't done so already.
You can do it by running `pip install networkx`

### Usage
To try the three methods independently, you can open the corresponding .py file, create a project with certain tasks, and call the calculate_critical_path method. 
The `tasks` need to be in a certain format. You can copy the example input and modify from it.
The length of the critical path and the path itself will be printed on the terminal.

To test the performance of the methods, use performance_eval.py (open using python path/to/file/performance_eval.py in terminal, something's wrong with packages if openned with IDLE).
You can adjust the number of test case or the range of size of test cases. 
For each test case, the execution time for all methods will be printed. The average time will also be printed out.
Note: brute force will be extremely slow with larger inputs.
It's commented out for now.