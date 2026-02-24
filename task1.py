from collections import deque

def rolling_queue():
    queue = deque()
    while True:
        num = input("Enter a number (or empty to stop): ")
        if num == "":
            break
        queue.append(int(num))
        if len(queue) > 5:
            queue.popleft()
    return list(queue)

# Example run
# User enters: 1,2,3,4,5,6,7 -> Output: [3,4,5,6,7]
print(rolling_queue())