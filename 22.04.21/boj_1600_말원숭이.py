from sys import stdin
input = stdin.readline
K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

hr = [2, 2, 1, -1, -2, -2, -1, 1]
hc = [1, -1, -2, -2, -1, 1, 2, 2]

visited = [[[0] * W for _ in range(H)] for __ in range(K+1)]

from collections import deque
q = deque()
q.append([0,0,0,0])
visited[0][0][0] = 1
ans = -1

while q:
    x, y, cnt, horse = q.popleft()
    if x == H - 1 and y == W -1:
        ans = cnt
        break
    for i in range(4):
        nr, nc = x + dr[i], y + dc[i]
        if 0 <= nr < H and 0 <= nc < W and board[nr][nc] != 1 and visited[horse][nr][nc] == 0:
            visited[horse][nr][nc] = 1
            q.append([nr, nc, cnt+1, horse])
    if (horse < K):
        for i in range(8):
            nr, nc = x + hr[i], y + hc[i]
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] != 1 and visited[horse+1][nr][nc] == 0:
                visited[horse+1][nr][nc] = 1
                q.append([nr, nc, cnt+1, horse+1])

print(ans)