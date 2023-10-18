def twoColorable(edges):
    colours = [None for _ in edges]
    colours[0] = True
    stack = [0]
    while len(stack):
        current = stack.pop()
        for node in edges[current]:
            if colours[node] is None:
                colours[node] = not colours[current]
                stack.append(node)
            elif colours[node] == colours[current]:
                return False

    return True


edges = [[1], [0]]

colourable = twoColorable(edges)
print(colourable)
