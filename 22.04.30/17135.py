import sys
input = sys.stdin.readline
N, M, D = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.append([0]*M)

# def shot():



def archor(cnt):
    if cnt == 3:
        # shot()
        print(lst)
        return
    for i in range(M):
        if lst[N][i] == 0:
            lst[N][i] = 1
            archor(cnt + 1)
            lst[N][i] = 0

archor(0)