n, m = map(int, input().split())
lst = list(map(int,input().split()))
max_ = max(lst)
ans = 0
for j in range(max_+1):
    for i in range(n):
        if max_ - j > lst[i]:
            ans += 0
        else:
            ans += 1
    if ans == m:
        print(max_ - j - 1)
        break
