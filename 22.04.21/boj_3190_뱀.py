dir = {0 : (1,0), 1 : (0,-1), 2 : (-1,0), 3 : (0,1)}

N = int(input())
applePoint = int(input())
graph = [[0] * N for _ in range(N)]

for i in range(applePoint):
    x, y = map(int, input().split())
    graph[x][y] = -1

L = int(input())
time_to_do = []
for _ in range(L):
    X, C = map(str, input().split())
    X = int(X)
    time_to_do.append((X,C))

graph[0][0] = 1
while True:
    for i in range(4):
        nr = x + dr[i]
    if 0 > nr or nr >= N or 0 > nc or nc >= N or graph[nr][nc] == 1:
        
        break
for i in range(time_to_do[0][0]+1):
    x += dir[3][0]; y += dir[3][1]
    if graph[x][y] == -1:
        graph[x-dir[3][0]][y-dir[3][1]] = 1

