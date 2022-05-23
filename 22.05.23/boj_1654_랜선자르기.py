N, M = map(int, input().split())

lst = [int(input()) for _ in range(N)]

for i in range(max(lst), 0, -1):
    ans = 0
    for j in range(N):
        ans += lst[j] // i
    if ans == M:
        print(i)
        break