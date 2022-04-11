n = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in range(n):
    cnt = 0
    if lst[i] == 1:
        continue
    for j in range(2, int(lst[i])+1):
        if lst[i]%j == 0:
            cnt += 1
    if cnt == 1:
        ans += 1
    
print(ans)