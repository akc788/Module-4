def undo_actions(actions, n):
    undone = []
    for _ in range(n):
        if actions:
            undone.append(actions.pop())
    return undone, actions

# Example
actions = ["open", "edit", "save", "close"]
n = 2
undone, remaining = undo_actions(actions, n)
print("Undone:", undone)          # ['close', 'save']
print("Remaining stack:", remaining)  # ['open', 'edit']
