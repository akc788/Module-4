from collections import deque

# ------------------- QUEUE EXERCISES -------------------

# 1. Reverse the first 3 elements of a queue
def reverse_first_k(queue, k=3):
    stack = []
    for _ in range(min(k, len(queue))):
        stack.append(queue.popleft())
    while stack:
        queue.appendleft(stack.pop())
    return queue

# Example
queue1 = deque([1, 2, 3, 4, 5])
print("Original queue:", list(queue1))
print("After reversing first 3:", list(reverse_first_k(queue1)))


# 2. Rolling queue (keep only last 5 numbers)
def rolling_queue():
    q = deque()
    while True:
        num = input("Enter a number (or empty to stop): ")
        if num == "":
            break
        q.append(int(num))
        if len(q) > 5:
            q.popleft()
    return list(q)

# Uncomment to test
# print("Final rolling queue:", rolling_queue())


# 3. Round-robin time processing
def round_robin(tasks, time_slice=2):
    q = deque(tasks)
    finished = []
    while q:
        name, time_needed = q.popleft()
        time_needed -= time_slice
        if time_needed > 0:
            q.append((name, time_needed))
        else:
            finished.append(name)
    return finished

# Example
tasks = [("A", 3), ("B", 6), ("C", 1)]
print("Round-robin completion order:", round_robin(tasks))


# 1. Find the minimum value in a stack
def min_in_stack(stack):
    if not stack:
        return None
    return min(stack)

# Example
stack1 = [5, 2, 9, 1, 7]
print("Minimum in stack:", min_in_stack(stack1))


# 2. Undo last N actions
def undo_actions(stack, n):
    undone = []
    for _ in range(n):
        if stack:
            undone.append(stack.pop())
    return undone

# Example
actions = ["open", "edit", "save", "close"]
n = 2
undone_actions = undo_actions(actions, n)
print("Undone actions:", undone_actions)
print("Remaining stack:", actions)


# 3. Simplify a file path using a stack
def simplify_path(path):
    parts = path.split('/')
    stack = []
    for part in parts:
        if part == "" or part == ".":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)

# Example
path_input = "/home//user/.././docs"
print("Simplified path:", simplify_path(path_input))