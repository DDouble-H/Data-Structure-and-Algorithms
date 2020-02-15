def bfs(graph, start):
    visited = []
    queue = []

    queue.append(start)

    while queue:
        print('Q', queue)
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


def dfs(graph, start):
    visited = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited


if __name__ == '__main__':
    graph = {'A': ['E'],
             'B': ['C', 'E'],
             'C': ['B', 'D', 'E'],
             'D': ['C', 'E'],
             'E': ['A', 'D']}

    print(graph)

    print('BFS', bfs(graph, 'A'))
    print('DFS', dfs(graph, 'A'))
