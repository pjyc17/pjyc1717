import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
lst = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque([])
def bfs():

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<M and 0<=ny<N and not lst[nx][ny]:
                q.append((nx, ny))
                lst[nx][ny] = lst[x][y] + 1

for i in range(M):
    for j in range(N):
        if lst[i][j] == 1:
            q.append((i,j))
bfs()
# flag = 0 
# ans = 0
# for i in range(M):
#     if flag == 1:
#         break
#     if ans < max(lst[i]):
#         ans = max(lst[i])
#     for j in range(N):
#         if lst[i][j] == 0:
#             print(-1)
#             flag = 1
#             break
# print(ans-1)
res = 0
isTrue = False
for i in lst:
    for j in i:
        if j == 0:
            isTrue = True
    res = max(res, max(i))
if isTrue == True:
    print(-1)
else:
    print(res - 1)