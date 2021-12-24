M = N = 100
for tc in range(1, int(input())+1):
    m, n = map(int, input().split())
    if m > n:
        N = N - m
    elif m < n:
        M = M - n
    else:
        pass
print(M)
print(N)