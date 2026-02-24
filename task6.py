def simplify_path(path):
    stack = []
    parts = path.split("/")
    
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
path = "/home//user/.././docs"
print(simplify_path(path))  # Output: /home/docs