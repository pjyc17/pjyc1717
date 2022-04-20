from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited2):
    queue = deque([start])
    visited2[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True


N, M, v = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
visited2 = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
dfs(graph, v, visited)
print()
bfs(graph, v, visited2)