from collections import deque
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
cnt = 0
graph = [[] for _ in range(n+1)]
for i in lst:
    a, b = i[0],i[1]
    graph[a].append(b)
    graph[b].append(a)
print(graph)

    
visited = [0] * (n+1)
print(visited)
def bfs(x):
    q = deque([])
    q.append(x)

    while q:
        x = q.popleft()
        visited[x] = 1
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)

