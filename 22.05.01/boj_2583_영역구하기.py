n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            arr[r][c] = 1
visited = [[0] * m for _ in range(n)]
from collections import deque
q = deque()
ans_list = []
def bfs(): 
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    global cnt
    while q:
        x, y = q.popleft()
        arr[x][y] = 1
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    ans_list.append(cnt)
    return ans_list

for i in range(n):
    for j in range(m):
        cnt = 1
        if arr[i][j] == 0 and visited[i][j] == 0:
            q.append((i, j))
            bfs()
ans_list.sort()
print(len(ans_list))
for i in ans_list:
    print(i)