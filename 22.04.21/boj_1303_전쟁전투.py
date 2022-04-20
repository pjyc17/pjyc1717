import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(M)]

def dfs(x, y, std, count):
    graph[x][y] = 'visited'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] != 'visited' and graph[nx][ny] == std:
                count = dfs(nx, ny, std, count+1)
    return count
white, blue = 0, 0

for i in range(M):
    for j in range(N):
        if graph[i][j] != 'visited':
            if graph[i][j] == 'W':
                white += dfs(i, j, 'W', 1) ** 2
            else:
                blue += dfs(i, j, 'B', 1) ** 2
print(white, blue)