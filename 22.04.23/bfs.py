def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(graph, i, visited)
from collections import deque
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


