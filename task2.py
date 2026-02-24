from collections import deque

def round_robin(tasks):
    queue = deque(tasks)
    finished = []
    
    while queue:
        name, time_needed = queue.popleft()
        time_needed -= 2
        if time_needed > 0:
            queue.append((name, time_needed))
        else:
            finished.append(name)
    
    return finished

# Example
tasks = [("A", 3), ("B", 6), ("C", 1)]
print(round_robin(tasks))  # Output: ['A', 'C', 'B']