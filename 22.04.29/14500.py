import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

max_ = 4
dx, dy = [0,0,1,-1], [1,-1,0,0]
def DFS(x,y, cnt, total):
    global max_
    if cnt == 4:
        max_ = max(max_, total)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx, ny, cnt+1, total + lst[nx][ny])
            visited[nx][ny] = 0
# def fuc(x,y):
#     global max_
#     max_ = max(max_, (lst[i][j]+lst[i-1][j]+lst[i-1][j-1]+lst[i-1][j+1]),(lst[i][j]+lst[i+1][j]+lst[i+1][j-1]+lst[i+1][j+1]),(lst[i+1][j]+lst[i+1-1][j]+lst[i+1-1][j-1]+lst[i+1-1][j+1]),(lst[i-1][j]+lst[i-1+1][j]+lst[i-1+1][j-1]+lst[i-1+1][j+1]),(lst[i][j]+lst[i][j-1]+lst[i-1][j-1]+lst[i+1][j-1]),(lst[i][j]+lst[i-1][j+1]+lst[i][j+1]+lst[i+1][j+1]),(lst[i][j+1]+lst[i][j+1-1]+lst[i-1][j+1-1]+lst[i+1][j+1-1]),(lst[i][j-1]+lst[i-1][j-1+1]+lst[i][j-1+1]+lst[i+1][j-1+1]))
#     return
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def exce(i, j):
    global max_
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = lst[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n+k)%4
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += lst[ni][nj]
        # 최대값 계산
        max_ = max(max_, tmp)
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = 1
            DFS(i, j, 1, lst[i][j])
            visited[i][j] = 0
            exce(i,j)
# for i in range(N-1):
#     for j in range(M-1):
#         fuc(i,j)
print(max_)