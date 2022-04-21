from collections import deque
N, M = map(int, input().split())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

board = [list(map(int,input())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for __ in range(2)]


q = deque()
q.append([0,0,1,1])
visited[1][0][0] = 1
ans = -1
while q:
    idx1, idx2, cnt, isPunched = q.popleft()
    if idx1 == N -1 and idx2 == M - 1:
        ans = cnt
        break
    else:
        for i in range(4):
            nr, nc = idx1 + dr[i], idx2 + dc[i]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 1 and visited[isPunched][nr][nc] == 0:
                visited[isPunched][nr][nc] = 1
                q.append([nr, nc, cnt+1, isPunched])
            elif (isPunched):
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 1 and visited[0][nr][nc] == 0:
                    visited[0][nr][nc] = 1
                    q.append([nr, nc, cnt+1, 0])
print(ans)