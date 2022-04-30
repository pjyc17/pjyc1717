from collections import deque
import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

def wall(cnt):
    if cnt == 0:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0:
                lst[i][j] = 1
                wall(cnt-1)
                lst[i][j] = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0
def bfs():
    q = deque([])
    tmp_lst = copy.deepcopy(lst)
    for i in range(n):
        for j in range(m):
            if tmp_lst[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and tmp_lst[nx][ny] == 0:
                tmp_lst[nx][ny] = 2
                q.append((nx,ny))
    global ans
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_lst[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)
wall(3)
print(ans)