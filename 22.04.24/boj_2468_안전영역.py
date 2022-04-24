from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst1 = []
for i in range(N):
    for j in range(N):
        if lst[i][j] not in lst1:
            lst1.append(lst[i][j])
lst1.sort()
def bfs(x, y, k):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and lst[nx][ny] > k:
                visited[nx][ny] = 1
                q.append((nx, ny))
ans = 1
for k in lst1:
    visited = [[0] * (N) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and 0 <= i < N and 0 <= j < N and lst[i][j] > k:
                visited[i][j] = 1
                bfs(i, j, k)
                cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)