import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
cnt = 0
# def dfs(x):
#     global cnt
#     visited[x] = 1
#     for i in lst[x]:
#         if not visited[i]:
#             visited[i] = 1
#             dfs(i)
#             cnt += 1
#     return cnt
from collections import deque
def bfs(x):
    global cnt
    q = deque([x])
    while q:
        p = q.popleft()
        visited[p] = 1
        for i in lst[p]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                cnt += 1
    return cnt
bfs(1)
    






# dfs(1)
print(cnt)
