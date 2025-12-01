from collections import deque

# Representing the graph using an adjacency list
graph = {
    0: [1, 2, 3],
    1: [],
    2: [4],
    3: [],
    4: []
}

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Start BFS from node 0
print("BFS traversal starting from node 0:")
bfs(graph, 0)
