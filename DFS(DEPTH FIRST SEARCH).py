# Representing the graph using an adjacency list
graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    4: [8],
    2: [],
    8: []
}

# DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Start DFS from node 5
print("DFS traversal starting from node 5:")
dfs(graph, 5)
