from sys import stdin, stdout
input = stdin.readline
print = stdout.write
K = int(input())
W, H = map(int, input().split())
board = [map(int, input().split()) for _ in range(H)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

hr = [2, 2, 1, -1, -2, -2, -1, 1]
hc = [1, -1, -2, -2, -1, 1, 2, 2]

visited = [[0] * W for _ in range(H)]

def dfs(x, y, cnt):
    visited[x][y] = 1
    for i in range(4):
        nr, nc = x + dr[i], y + dc[i]
        if 0 <= nr < H and 0 <= nc < W and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            cnt = dfs(nr, nc, cnt+1)
    return cnt

for i in range(H):
    for j in range(W):
        if board[i][j] == 0 and visited[i][j] == 0:
            dfs(i,j,1)

            

def dfs_h(x, y, k)