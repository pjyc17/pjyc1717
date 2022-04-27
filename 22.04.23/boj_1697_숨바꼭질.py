N,K = map(int, input().split())
cnt = 0
while N != K:
    dir = [+ 1, - 1, * 2]
    if N == K:
        print(cnt)
        break
    for cal in dir:
        N = N