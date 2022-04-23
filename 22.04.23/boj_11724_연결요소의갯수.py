import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (N+1)
cnt = 0
# def dfs(x):
#     for node in graph[x]:
#         if not visited[node]:
#             visited[node] = 1
#             dfs(node)


q = deque()


for i in range(1, N+1):
    if not visited[i]:
        q.append(i)
        cnt += 1
        visited[i] = 1
        while q:
            p = q.popleft()
            for node in graph[p]:
                if not visited[node]:
                    visited[node] = 1
                    q.append(node)
print(cnt)