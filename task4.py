def min_in_stack(stack):
    if stack:
        print(min(stack))
    else:
        print("Stack is empty")

# Example
stack = [5, 2, 9, 1, 7]
min_in_stack(stack)  # Output: 1