n = int(input())
lst = list(map(int, input().split()))
print(lst)
cnt = 0
ans = 0
print(int(lst[0]**(0.5))+1)
for i in range(n):
    for j in range(2, int(lst[i]**(0.5))+1):
        if lst[i]%j == 0:
            cnt += 1
    if cnt >= 2:
        ans += 1
print(ans)