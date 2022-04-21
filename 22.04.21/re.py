from sys import stdin
input = stdin.readline
K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

hr = [2, 2, 1, -1, -2, -2, -1, 1]
hc = [1, -1, -2, -2, -1, 1, 2, 2]

visited = [[0] * W for _ in range(H)]


from collections import deque
q = deque()
q.append([0,0,0,0])
visited[0][0] = 1

ans = -1
while q:
    idx1, idx2, distance, horse = q.popleft()
    if idx1 == H-1 and idx2 == W-1:
        ans = distance
        break
    else:
        for i in range(4):
            r = idx1 + dr[i]; c = idx2 + dc[i]
            if 0<=r<H and 0<=c<W and board[r][c] != 1 and visited[r][c] == 0:
                visited[r][c] = 1
                q.append([r,c,distance+1,horse])
        if (horse<K):
            for i in range(8):
                r = idx1 + hr[i]; c = idx2 + hc[i]
                if 0<=r<H and 0<=c<W and board[r][c] != 1 and visited[r][c] == 0:
                    visited[r][c] = 1
                    q.append([r,c,distance+1,horse+1])

print(ans)