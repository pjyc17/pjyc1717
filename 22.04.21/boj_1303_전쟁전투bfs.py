from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(M)]

def bfs(x,y,std):
    queue = deque([(x,y)])
    graph[x][y] = 'visited'
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] != 'visited' and graph[nx][ny] == std:
                    graph[nx][ny] = 'visited'
                    queue.append((nx, ny))
                    cnt += 1
    return cnt



white, blue = 0, 0

for i in range(M):
    for j in range(N):
        if graph[i][j] != 'visited':
            if graph[i][j] == 'W':
                white += bfs(i, j, 'W') ** 2
            else:
                blue += bfs(i, j, 'B') ** 2
print(white, blue)