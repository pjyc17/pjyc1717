# N, M = map(int,input().split())
# lst = [list(map(int, input())) for _ in range(N)]

# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]

# visited = [[0] * M for _ in range(N)]
# from collections import deque
# ans = 0
# def bfs(x, y, cnt):
#     global ans
#     q = deque([(x, y)])
#     while q:
#         r, c = q.popleft()
#         visited[r][c] = 1
#         if r == N - 1 and c == M -1:
#             ans = cnt
#             break
                        
#         for i in range(4):
#             nr, nc = r + dr[i], c + dc[i]
#             if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and lst[nr][nc] == 1:
#                 visited[nr][nc] = 1
#                 q.append((nr, nc))
#                 cnt += 1

# bfs(0, 0, 0)
# print(ans)
#######################################################################################
from collections import deque
N, M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]
def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny))
    return graph[N-1][M-1]
print(bfs(0,0))