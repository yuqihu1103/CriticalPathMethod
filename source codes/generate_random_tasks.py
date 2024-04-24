import random

def generate_random_test(num_tasks, max_duration):
    tasks = []
    while True:
        tasks = []
        for i in range(num_tasks):
            task_id = chr(ord('A') + i)
            duration = random.randint(1, max_duration)
            dependencies = random.sample([chr(ord('A') + j) for j in range(i)], random.randint(0, i))
            tasks.append({'id': task_id, 'duration': duration, 'dependencies': dependencies})
        if is_executable(tasks):
            break
    return tasks

def is_executable(tasks):
    task_ids = {task['id'] for task in tasks}
    for task in tasks:
        for dependency in task.get('dependencies', []):
            if dependency not in task_ids:
                return False
    return True

# Example usage:
num_tasks = 20
max_duration = 15
random_test = generate_random_test(num_tasks, max_duration)
print("Random Test Case:")
for task in random_test:
    print(task)
