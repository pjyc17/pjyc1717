from collections import deque
from sys import stdin
input = stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x,y):
    q = deque([(x,y)])
    visited = [[0] * M for _ in range(N)]
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 0 and not visited[nx][ny]:
                lst[nx][ny] = 2
                visited[nx][ny] = 1
                q.append((nx,ny))

N, M = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(N)]



lst_0 = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            lst_0.append((i,j))
print(lst[lst_0[1][0]][lst_0[1][1]])
# for a in range(len(lst_0)-2):
#     lst[lst_0[a][0]][lst_0[a][1]] = 1
#     for b in range(a+1, len(lst_0)-1):
#         lst[lst_0[b][0]][lst_0[b][1]] = 1
#         for c in range(b+1, len(lst_0)):
#             lst[lst_0[c][0]][lst_0[c][1]] = 1
            
#             for i in range(N):
#                 for j in range(M):
#                     if lst[i][j] == 2 and not visited[i][j]:
#                         bfs(i, j)
#                         print(lst)
#                     visited = [[0] * M for _ in range(N)]
#             lst[lst_0[c][0]][lst_0[c][1]] = 0
#         lst[lst_0[b][0]][lst_0[b][1]] = 0
#     lst[lst_0[a][0]][lst_0[a][1]] = 0



