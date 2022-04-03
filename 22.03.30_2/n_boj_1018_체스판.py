a, b = map(int,input().split())
ans = ''
cnt1 = 0
cnt2 = 0

for i in range(a):
    ans += str(input())
if b%2 == 1:
    for i in range(len(ans)//2):
        if ans[2*i+1] != 'B':
            cnt1 += 1
        if ans[2*i] != 'W':
            cnt1 += 1

    for i in range(len(ans)//2):
        if ans[2*i+1] != 'W':
            cnt2 += 1
        if ans[2*i] != 'B':
            cnt2 += 1

print(ans[1])
print(min(cnt1, cnt2))