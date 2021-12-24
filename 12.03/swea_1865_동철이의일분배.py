def bfs(y):
    global res, Res
    if res <= Res:
        return
    if y == N:
        Res = res
        return
    for x in range(N):
        if not visited[x]:
            if arr[y][x] == 0:
                continue
            else:
                res *= arr[y][x]/100
                visited[x] = 1
                bfs(y+1)
                res /= arr[y][x]/100
                visited[x] = 0



for tc in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    res, Res = 1, 0
    bfs(0)
    print('#{} {:.6f}'.format(tc, Res*100))

