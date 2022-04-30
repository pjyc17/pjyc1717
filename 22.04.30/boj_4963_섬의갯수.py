from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        dx = [0, 0, 1, -1, 1,1,-1,-1]
        dy = [1, -1, 0, 0, -1,1,1,-1]
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx< m and 0<= ny < n and not visited[nx][ny] and lst[nx][ny] == 1: 
                visited[nx][ny] = 1
                q.append((nx, ny))
while True:
    cnt = 0
    q = deque([])
    n, m = map(int, input().split())
    visited = [[0] * n for _ in range(m)]
    if n == 0 and m == 0:
        break
    lst = [list(map(int, input().split())) for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if lst[i][j] == 1 and visited[i][j] == 0:
                q.append((i,j))
                bfs()
                cnt += 1

    print(cnt)
