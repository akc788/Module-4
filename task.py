from collections import deque

def reverse_first_three(queue):
    stack = []
    # Step 1: Remove first 3 elements and push to stack
    for _ in range(min(3, len(queue))):
        stack.append(queue.popleft())
    
    # Step 2: Pop from stack and append back to queue
    while stack:
        queue.appendleft(stack.pop())
    
    # Step 3: Move the rest of the queue to the end to keep order
    for _ in range(len(queue) - 3):
        queue.append(queue.popleft())
    
    return list(queue)

# Example
q = deque([1, 2, 3, 4, 5])
print(reverse_first_three(q))  # Output: [3, 2, 1, 4, 5]