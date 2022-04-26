from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n,m = map(int,input().split())
lst = list(map(int, input().split()) for _ in range(n))
visited = [[0] * m for _ in range(n)]
def bfs(x, y, cnt):
    q = deque([(x,y)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1
                cnt -= 1
